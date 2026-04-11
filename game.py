import random

def main():
    while True:
        try:
            level = input("Level: ")
            number = random.randint(1, int(level))
        except ValueError:
            continue
        
        while True:
            try:
                guess = int(input("Guess: "))
            except ValueError:
                continue
            if guess == number:
                print("Just right!")
                break   
            elif guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
        break

main()
