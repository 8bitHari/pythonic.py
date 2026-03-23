print("Welcome to \"Can you guess the Number!\" ")
count = 0
while True:
    print("Enter your guess below: ")
    count += 1
    num = int(input())
    if num == 8:
        print("Correct! ")
        print(f"Total attempts: {count}") 
        break
    elif num < 8:
        print("Too low")
    elif num > 8:
        print("Too high")