import time
import random
import string
print("This is a random password generator")
length = int(input("Enter the required password length: "))
password = "".join(random.choice(string.ascii_letters + string.digits) for i in range(length))
print(f"Random password: {password} ")