from web3 import Web3, Account
from threading import Thread
import time
import random

from config import routers, abi, Pandra_settings

with open('privates.txt', 'r') as file:
    private_keys = [line.strip() for line in file.readlines()]
    # print(private_keys)

with open('proxies.txt', 'r') as file:
    proxies = [proxy.strip() if proxy.strip() and proxy.strip() != '-' else None for proxy in file.readlines() ]
    # print(proxies)


def create_mint_transaction(private_key, route_config: Pandra_settings, proxy):
    # login, password, ip, port = proxy
    account = Account.from_key(private_key)
    if proxy:
        request_kwargs = {'proxies': {
            'https': proxy,
            'http': proxy
        }}
    else:
        request_kwargs = {}
    web3 = Web3(
        provider=Web3.HTTPProvider(
            endpoint_uri=route_config.rpc,
            request_kwargs=request_kwargs
        )
    )
    pandra_contract = web3.eth.contract(web3.to_checksum_address(route_config.contract), abi=abi)
    empty_transaction = pandra_contract.functions.mint().build_transaction(
        {
            'nonce': 0,
            'value': 0,
            'from': account.address,
            'gas': 0,
            'gasPrice': 0
        }
    )
    return empty_transaction, account, web3


def estimate_gas(transaction, account, web3: Web3):
    nonce = web3.eth.get_transaction_count(account.address)
    transaction['nonce'] = nonce
    gas_estimate = web3.eth.estimate_gas(transaction)
    transaction['gas'] = int(gas_estimate * 1.2)
    wei_estimate = web3.eth.gas_price
    print('wei', wei_estimate)
    transaction['gasPrice'] = int(wei_estimate)
    #input(transaction)
    return transaction


def broadcast_transaction(transaction, web3: Web3, account: Account):
    signed_transaction = account.sign_transaction(transaction)
    return web3.eth.send_raw_transaction(signed_transaction.rawTransaction)


def mint_pandras(route_name, route_config, pk, proxy):
    pk_logs = []
    account = Account.from_key(pk)
    print(f'{account.address} is now minting on ', route_name.upper())
    for i in range(6):
        time.sleep(random.randint(5,10))
        try:
            empty_transaction, account, web3 = create_mint_transaction(pk, route_config, proxy)
            transaction = estimate_gas(empty_transaction, account, web3)
            tx_id = broadcast_transaction(transaction, web3, account)
            while True:
                try:
                    web3.eth.get_transaction_receipt(tx_id.hex())
                    break
                except:
                    time.sleep(1)
                    continue
            log = f'ADDRESS - {account.address}\t\tTRANSACTION - {tx_id.hex()}\t\tROUTE - {route_name.upper()}\n'
            pk_logs.append(log)
        except Exception as e:
            log = f'ADDRESS - {account.address}\t\tROUTE - {route_name.upper()}\t\tERROR - {e}\n'
            pk_logs.append(log)
    with open('logs.txt', 'a') as file:
        file.write(''.join(pk_logs))
    return


total_threads = []

for index, private in enumerate(private_keys):
    try:
        proxy = proxies[index]
    except:
        proxy = None
    for route_name, route_config in routers.items():
        route_thread = Thread(target=mint_pandras, args=(route_name, route_config, private, proxy,))
        total_threads.append(route_thread)
print('Total transactions = ', len(total_threads))

current_threads = []
while total_threads:
    if len(current_threads) > 10:
        for index, started_thread in enumerate(current_threads):
            if not started_thread.is_alive():
                current_threads.pop(index)
        continue
    thread = total_threads.pop(0)
    current_threads.append(thread)
    thread.start()

for started_thread in current_threads:
    started_thread.join()

print('work finished')

