import time
import getpass
print("Welcome to the ATM! ")
time.sleep(1)
print("Enter your PIN below: ")
while True:
    pin = int(getpass.getpass("PIN: "))
    if pin == 8888:
        print("Welcome! ")
        break
    else:
        print("Incorrect PIN! ")
balance = 1000
while True:
    time.sleep(1)
    print("Please enter the amount you would like to withdraw: ")
    withdraw = int(input())
    if withdraw > balance:
        print("Insufficient Balance!")
    else:
        print("Withdrawal complete! ")
        time.sleep(1)
        balance = balance - withdraw
        print(f"Your balance is {balance} ")
    time.sleep(1)
    print("Do you want to transact again? Y/N")
    again = input()
    if again == "Y":
        continue
    elif again == "N":
        print("Thank you for banking with us! ")
    break

    

    