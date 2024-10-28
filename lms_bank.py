'''
Author: Rohan R
Date: 28-10-2024
Problem: Write a program that simulates a simple bank ATM system. The user has an initial balance of $1000.
The ATM should display a menu with options to:

    Check Balance
    Deposit Money
    Withdraw Money
    Exit
'''

balance=1000
while True:
    print("1.\tCheck Balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice=int(input("Enter your choice: "))

    if choice==1:
        print("Balance:$ ",balance)
    elif choice==2:
        deposited=int(input("Enter amount to be deposited: "))
        balance += deposited
        print("Balance:$ ",balance)
    elif choice==3:
        withdraw=int(input("Enter amount to be withdrawn: "))
        if withdraw<=balance:
            print("The amount withdrawn:$ ",withdraw)
            print("Balance:$ ",balance-withdraw)
        else:
            print("Insufficient balance")
    elif choice==4:
        break
    else:
        print("Invalid Entry")