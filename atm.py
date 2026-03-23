import time
import getpass
print("Welcome to .py bank! ")
time.sleep(1)
pin_correct = "8888"
amount = 1000
while True:
    pin = getpass.getpass("Please enter your PIN: ")
    if pin == pin_correct:
        break
    else:
        print("Incorrect PIN! ")
while True:
            print("Please enter the amount you would like to withdraw ")
            withdraw = int(input("Amount: "))   
            if withdraw > amount:
                print("Insufficient balance! ") 
            else: 
                print("Withdrawl complete! ")
                time.sleep(1)
                amount = amount - withdraw
                print(f"Remaining balance is {amount}")
            time.sleep(1)
            print("Would you like to make another withdrawal?  Y/N")
            again = input()
            if again == "Y":
                continue
            elif again == "N":
                 print("Thank you for banking with us! ")
            break                 