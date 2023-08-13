from web3 import Account, Web3
from config import Pandra_settings, abi


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
    bnb_chain_id = 56
    nonce = web3.eth.get_transaction_count(account.address)
    transaction['nonce'] = nonce
    gas_estimate = web3.eth.estimate_gas(transaction)
    transaction['gas'] = int(gas_estimate * 1.2)
    wei_estimate = web3.eth.gas_price
    print('wei', wei_estimate)
    transaction['gasPrice'] = int(wei_estimate)
    if web3.eth.chain_id == bnb_chain_id:
        transaction['gasPrice'] = web3.to_wei('1.5', 'gwei')
    return transaction


def broadcast_transaction(transaction, web3: Web3, account: Account):
    signed_transaction = account.sign_transaction(transaction)
    return web3.eth.send_raw_transaction(signed_transaction.rawTransaction)