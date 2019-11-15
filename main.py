# Creator:  Ryan Hawkins

# Title:  Millionaire Investor
"""
Classes
    Player
    Property
    Accounts
        Banks
        Stocks
"""

import random
import time
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def transition(seconds=1):
    time.sleep(seconds)
    clear()


def display_header(header):
    print(header)
    print("-" * len(header))


class Account:

    accounts = dict()

    def __init__(self, name, balance, int_rate):
        self.name = name
        self.balance = balance
        self.int_rate = int_rate

        Account.accounts[self.name] = [self.balance, self.int_rate]

    def __str__(self):
        return self.name

    def check_bal(self):
        print(f"{self.name}:  {round(self.balance, 2)}")

    def show_all_accounts():
        i = 0
        print()
        display_header("All Accounts")
        for name, balance in Account.accounts.items():
            i += 1
            print(
                f"{i}: {name}:\t\t$ {round(Account.accounts[name][0], 2)} \t\t{round(Account.accounts[name][1], 3)}%"
            )


class Bank(Account):

    bank_accounts = dict()
    bank_selections = {}

    def __init__(self, name, balance, int_rate):
        super().__init__(name, balance, int_rate)

        Bank.bank_accounts[self.name] = self.balance
        for i, name in enumerate(self.bank_accounts, 1):
            self.bank_selections[i] = name

    def bank_account_menu():
        for keys, values in Bank.bank_selections.items():
            print(f'{keys}:  {values}')

    def show_bank_accounts():
        i = 0
        print()
        display_header("Bank Accounts")
        for name, balance in Bank.bank_accounts.items():
            i += 1
            print(f"{i}: {name}:\t\t${round(Bank.accounts[name][0], 2)}")


class Investment(Account):
    def __init__(self):
        pass


def main():

    cycle = 0

    intro()
    Account.show_all_accounts()
    print(Bank.bank_selections)

    menu()


def intro():
    pass


def menu():
    display_header("\nOptions Menu")
    print("[1] Review Accounts")
    print("[2] Transfer Money ($)")
    print("[3] Invest - Current Account")
    print("[4] Research New Account")
    print()
    print("[5] Go to bed.")
    menu_selection()


def menu_selection():
    choice = input("\nChoose Option: ").lower()
    if choice == "1":
        Bank.bank_account_menu()
        menu()
    elif choice == "2":
        transfer_money()
        menu_selection()

    elif choice == "3":  # Invest in current account.
        print("This option is not yet available.")
        menu()
    elif choice == "4":
        print("This option is not yet available.")
        menu()
    elif choice == "5":
        update_account_bals()
        Account.show_all_accounts()
        menu()
    else:
        print("Invalid Entry. Try Again")
        menu()


def update_account_bals():

    for name, (balance, int_rate) in Account.accounts.items():
        Account.accounts[name] = [balance * int_rate, int_rate]


def transfer_money():
    Bank.bank_account_menu()
    print()
    start_acct = int(input("Which account would you like to transfer from? "))
    end_acct = int(input("Which account would you like to transfer to? "))
    trans_amt = int(input("How much would you like to transfer? "))

    Account.accounts[start_acct] = balance - trans_amt
    return start_acct
    return end_acct
    print(f"You transfered ${trans_amt} from {start_acct} to {end_acct}.")


bank_1 = Bank("United Bank", 1000, 1.05)
bank_2 = Bank("Bank of LP", 100, 1.045)
inv_1 = Account("Sophia's", 100, random.uniform(1.05, 1.5))

# bank.cycle_interest()
# bank.check_bal()

# inv_1.cycle_interest()
# inv_1.check_bal()

# for i in range (3):
#     bank.cycle_interest()
#     bank.check_bal()
#     inv_1.cycle_interest()
#     inv_1.check_bal()

# for i in range (10):
#     print(random.uniform(0,2))

# print(Account.accounts)

if __name__ == "__main__":
    main()

# for i in range(5):
#     bank_1.check_bal()
#     bank_1.cycle_interest()

#     print()

# for i in range(5):
#     bank_1.check_bal()
#     update_account_bals()
