from web3 import Web3, Account
from threading import Thread
import time
import random
from bridge.func import do_one_address
from config import routers, abi, Pandra_settings
from utils import *

with open('privates.txt', 'r') as file:
    private_keys = [line.strip() for line in file.readlines()]
    # print(private_keys)

with open('proxies.txt', 'r') as file:
    proxies = [proxy.strip() if proxy.strip() and proxy.strip() != '-' else None for proxy in file.readlines() ]
    # print(proxies)


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

def start_minting():
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


if __name__ == '__main__':
    while True:
        print('Choose.\n'
              '1 - mint pandas\n'
              '2 - bridge pandas\n'
              '0 - exit')
        response = input('Answer: ')
        if response not in ['1', '2']:
            import sys
            sys.exit()
        else:
            if response == '1':
                start_minting()
            else:
                do_one_address()

