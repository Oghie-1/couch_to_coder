#!/usr/bin/python3


user = "Amara"

balance = int(1000)
pin = int(2345)
new_bal = []


def account(user):

    print("\nHi, User\n")
    print("Please insert your pin\n")
    x = int(input())
    if x == pin:
        print("\nWelcome " + user)
    else:
        print("\nWrong Pin\n" + "Try again")
        return account(user)


def display_bal():
    print("Your account balance is: ", balance)

def savings():
    savings = int(input("How much would you like to save? "))
    saved_amt = balance + savings
    new_bal.append(saved_amt)
    print("\nSaved Successfully")
    print("\n Your current balance is:", new_bal[0])

def account_withdrawal(balance, new_bal):
    withdraw = int(input("\nHow much would you like to withdraw: \n"))
    if withdraw > balance:
        print("\nInsufficient funds")
    else:
        transfer = balance - withdraw
        new_bal.append(transfer)
        print("\nWithdrawal Successful")
        print("\n Your current balance is:", new_bal[0])

def main_operations():
    print("\nwelcome to couch bank ltd\n")
    x = int(input("\npress 1 to login and 2 to exit: \n"))
    if x == 1:
        account(user)
        display_bal()
        inp = int(input("\nPress 1 for Savings or 2 to Withdraw: \n"))
        if inp == 1:
            savings()
        else:
            account_withdrawal(balance, new_bal)

    else:
        print("\nThank You for using Couch Bank" + "\n Would You Like to open an account")


if __name__ == "__main__":
    inp = int(input("\n\npress 1 to run app or 2 to cancel\n: "))

    if inp == 1:
        main_operations()
    else:
        print("\n\nThank You for Banking with us!")


    
