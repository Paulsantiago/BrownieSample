#from numpy import sometrue
from brownie import accounts, config, SimpleStorage
import os
def deploy_simple_storage():
    account = accounts[0]
    # accountPaul = accounts.load("paulkey")
    # print(accountPaul)
    #account = accounts.add(os.getenv("PRIVATE_KEY"))
    #account =accounts.add(config["wallets"]["from_key"])
    print("account: ",account)
    simple_storage = SimpleStorage.deploy({"from":account})
    print(simple_storage)
    storedValue = simple_storage.retrieve()
    print(storedValue)
    transaction = simple_storage.store(35,{"from": account})
    transaction.wait(1)
    print("transaction:",transaction)
    updateValue = simple_storage.retrieve()
    print("updated  value :",updateValue)


def main():
    print("initializating..")
    deploy_simple_storage()

