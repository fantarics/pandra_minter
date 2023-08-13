from web3 import Web3, Account
from config import Pandra_settings, Destination_config, abi, destinations, l0_abi, zkbridge_abi, routers
import requests
from utils import *
import time


def get_pandas(route_config: Pandra_settings, web3: Web3, pk):
    pandra_contract = web3.eth.contract(web3.to_checksum_address(route_config.contract), abi=abi)
    account = Account.from_key(pk)
    address = account.address
    explorer_url = route_config.explorer_url
    request_url = f"https://{explorer_url}/api" \
                  "?module=account" \
                  "&action=tokennfttx" \
                  f"&contractaddress={route_config.contract}" \
                  f"&address={address.lower()}" \
                  "&page=1" \
                  "&offset=100" \
                  "&startblock=0" \
                  "&endblock=999999999" \
                  "&sort=asc" \
                  f"&apikey={route_config.api_key}"
    response = requests.get(request_url)
    result = response.json()
    ids_list = [panda['tokenID'] for panda in result["result"] if panda['to'] == address.lower()]
    still_owned = [int(panda_id) for panda_id in ids_list if pandra_contract.functions.ownerOf(int(panda_id)).call().lower() == address.lower()]
    return still_owned


def approve_for_all(panda_contract, pk, bridge_contract, web3):
    account = Account.from_key(pk)
    transaction = panda_contract.functions.setApprovalForAll(
        web3.to_checksum_address(bridge_contract),
        True
    ).build_transaction(
        {
            'nonce': 0,
            'value': 0,
            'from': account.address,
            'gas': 0,
            'gasPrice': 0
        }
    )
    transaction = estimate_gas(transaction, account, web3)
    tx_id = broadcast_transaction(transaction, web3, account)
    while True:
        try:
            web3.eth.get_transaction_receipt(tx_id.hex())
            break
        except:
            time.sleep(1)
            continue
    return tx_id


def do_one_address():
    pk = input("Private key: ")
    pk_logs = []
    pk_pandas = {}
    account = Account.from_key(pk)
    for route_name, route_config in routers.items():
        if route_name.lower() == 'core':
            address = account.address
            panda_ids = [int(panda_id) for panda_id in input(f'введите через запятую id панд в сети CORE, которые нужно перекинуть.\n'
                              f'контракт панд: {route_config.contract}\n'
                              f'Искать тут: https://scan.coredao.org/token/0x36e5121618c0af89e81acd33b6b8f5cf5cdd961a?a={address}#transfers\n'
                              f'Ввод: ').split(',')]
        else:
            web3 = Web3(Web3.HTTPProvider(route_config.rpc))
            panda_ids = get_pandas(route_config, web3, pk)
        pk_pandas[route_name] = panda_ids

    for source, destination in destinations.items():
        chain_config = destination['network']
        pandas = pk_pandas.get(chain_config.name) or []
        account = Account.from_key(pk)
        web3 = Web3(Web3.HTTPProvider(chain_config.rpc))
        abi_choice = {
            'l0': l0_abi,
            'zkbridge': zkbridge_abi
        }
        if not pandas:
            continue
        bridge_contracts = set([value.send_trough_contract for key, value in [(key, value) for key, value in destination.items() if key != 'network']])
        print(bridge_contracts)
        assert len(bridge_contracts) == 2
        for bridge_contract in bridge_contracts:
            panda_contract = web3.eth.contract(chain_config.contract, abi=abi)
            approve_for_all(panda_contract, pk, bridge_contract, web3)
        for index, (chain_id, config) in enumerate([(key, value) for key, value in destination.items() if key != 'network']):
            if chain_id == 'network':
                continue
            try:
                panda_id = pandas[index]
            except:
                print('Панды закончились до рассылки во все сети')
                break
            config: Destination_config
            print('to chain id', chain_id, config.method)
            # print(config)

            send_contract = web3.eth.contract(
                web3.to_checksum_address(config.send_trough_contract),
                abi=abi_choice[config.method]
            )
            if config.method == 'zkbridge':
                value = send_contract.functions.fee(chain_id).call()
                payload = [
                    web3.to_checksum_address(chain_config.contract),
                    panda_id,
                    chain_id,
                    account.address.replace('0x', '0x000000000000000000000000')
                ]
            else:
                value = send_contract.functions.estimateFee(
                    web3.to_checksum_address(chain_config.contract),
                    panda_id,
                    chain_id,
                    account.address,
                    "0x00010000000000000000000000000000000000000000000000000000000000055730"
                ).call()
                payload = [
                    web3.to_checksum_address(chain_config.contract),
                    panda_id,
                    chain_id,
                    account.address,
                    "0x00010000000000000000000000000000000000000000000000000000000000055730"
                ]
            transaction = send_contract.functions.transferNFT(
                *payload
            ).build_transaction(
                {
                    'nonce': 0,
                    'value': value,
                    'from': account.address,
                    'gas': 0,
                    'gasPrice': 0
                }
            )
            try:
                transaction = estimate_gas(transaction, account, web3)
                tx_id = broadcast_transaction(transaction, web3, account)
                while True:
                    try:
                        web3.eth.get_transaction_receipt(tx_id.hex())
                        break
                    except:
                        time.sleep(1)
                        continue
                log = f'ADDRESS - {account.address}\t\tTRANSACTION - {tx_id.hex()}\t\tROUTE - {source.upper()} TO {chain_id} (chain_id) Method - {config.method}\n'
                pk_logs.append(log)
            except Exception as e:
                log = f'ADDRESS - {account.address}\t\tROUTE - {source.upper()} TO {chain_id} (chain_id) Method - {config.method}\t\tERROR - {e}\n'
                pk_logs.append(log)
    with open(f'{account.address}.txt', 'w') as file:
        file.write(''.join(pk_logs))







