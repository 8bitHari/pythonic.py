#Ask user for their name
#name = input("What's your name? ")
#age = input("How old are you? ")
#Say hello to user and say their age
#print("Hello,",name,"You are",age,"years old")
#print("Hello, " + name + " You are " + age + " years old")
#print("Hello, " + name,"You are", age, "years old")
#print("Hello, \"friend\"")
#print("Hello, {name}")
#import time
#print("Hello, what is your name? ")
#name = input("My name is ")    
#print("Hi "+name+"!")
#print(f"Hi {name}!")
#time.sleep(1)
#print("How old are you? ")
#age = input("Age: ")
#time.sleep(1)
#print("What is your gender? ")
#sex = input("Gender: ")
#import time
#import getpass
#username = input("Username: ")
#if username == "Hari":
    # password =getpass.getpass("What is your password? ")
    # while password != "12345":
        # print("Incorrect password!")
        # password = getpass.getpass("Try again! ")
    # print("Welcome Back!")    
#else:
    # print("Invalid user")
# Remove whitespace from string
#name = name.strip()
# Capitalize user's name
#name = name.capitalize()
#name = name.title().strip()
#Split user's name into first name and last name
#first, last = name.strip().title().split(" ")
#print("Hello, what is your name? ")
#first, last = input().strip().title().split(" ")
#print(f"Hello, {first}")
def main():
    name = input("Enter name: ")
    hello(name)

def hello(to="world"):
    print("Hello,", to)

if __name__ == "__main__":
    hello()