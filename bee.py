import time     
WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}
def main():
    print("Welcome to the Spelling Bee! \n")
    time.sleep(1)
    print("Your words are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"\n{len(WORDS)} words left! \n")
        time.sleep(1)
        print("Guess the word! \n ")
        guess = input("Guess: ")
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!")       
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")

    time.sleep(1)
    print("\nThat's the game!")
        
    


main()