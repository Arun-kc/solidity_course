import os
from brownie import Contract, accounts
from dotenv import load_dotenv
load_dotenv()

def main():
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    usdc_contract = Contract('0x8405173d81069D11bb778499c6A6130c0D320555')
    defi_contract = Contract('0xd4C03eB9079974D8511689cB6842524E13b2ebD0')
    #ausd_contract = Contract('0x8Cb1cBE9bBE44Be5FA08bC8D9Eb9FF7d8A6B0867')

    print(f"Before function call Current usdc token deposit balance is {defi_contract.depositBalance(account)}")

    usdc_contract.approve(defi_contract, 10000, {"from": account})
    defi_contract.depositToken(10000, {"from": account})

    print(f"After function call Current usdc token deposit balance is {defi_contract.depositBalance(account)}")

    defi_contract.withdraw(100, {"from": account})

    print(f"Current balance after Withdraw usdc token deposit balance is {defi_contract.depositBalance(account)}")

