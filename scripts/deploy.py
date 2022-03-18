from brownie import accounts, config,SimpleStorage
#import os
def deploy_simple_storage():
    account = accounts[0]
    SimpleStorage.deploy({"from":account})
    # accountPaul = accounts.load("paulkey")
    # print(account)
    # print(accountPaul)
    #account = accounts.add(os.getenv("PRIVATE_KEY"))
    #account =accounts.add(config["wallets"]["from_key"])
    print(account)
def main():
    print("initializating..")
    deploy_simple_storage()

