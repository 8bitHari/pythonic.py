import time
def main():
    print("welcome to Hari's Quiz! ")
    time.sleep(1)
    print("\nToday's topic is about F1!\n\nThe Quiz consists of 5 questions in total.\n\nNote: Each question is worth 1 point.\n")
    time.sleep(1)
    print("Are you ready? Type Yes or No below!\n ")
    score = 0
    while True: 
        answer = input()
        if answer == "No":
            print("\nCome back when you're ready!\n ")
            print("Are you ready now?\n ")
            continue
        elif not (answer == "Yes" or answer == "No"):
            print("\nPlease enter a valid option.\n ")
            continue
        elif answer == "Yes":
            break
    print("\nQuestion 1: Who is the current World Champion?\n ")
    answer1 = input("Answer: ")
    if not (answer1 == "Lando Norris"):
        print("\nIncorrect!")
        print(f"Score: {score}/5")
    else:
        print("\nCorrect!")
        score += 1
        print(f"Score: {score}/5")
    print("\nQuestion 2: Who is also know as the \"Honey Badger\" in F1?\n")
    answer2 = input("Answer: ")
    if not (answer2 == "Daniel Ricciardo"):
        print("\nIncorrect! ")
        print(f"Score: {score}/5")
    else:
        print("\nCorrect! ")
        score += 1
        print(f"Score: {score}/5")
    print("\nQuestion 3: What is the home circuit of RedBull Racing F1? ")
    answer3 = input("Answer: ")
    if not(answer3 == "RedBull Ring"):
        print("\nIncorrect!")
    else:
        print("\nCorrect!")
        score += 1
        print(f"Score: {score}/5")
    print("\nQuestion 4: Which active F1 driver has won 7x WDCs in total? ")
    answer4 = input("Answer: ")
    if not(answer4 == "Lewis Hamilton"):
        print("\nIncorrect! ")
    else:
        print("\nCorrect")
        score +=1
        print(f"Score: {score}/5")
    print("\nQuestion 5: Who is the team principal of Audi F1 Team? ")
    answer5 = input("Answer: ")
    if not(answer5 == "Mattia Binotto"):
        print("\nIncorrect")
    else:
        print("\nCorrect!")
        score += 1
        print(f"Score: {score}/5")
    print(f"Total score: {score} ")
    if score == 5:
        print("\nYou are a true F1 fan! ")
    elif score >= 3:
        print("Nice one!")
    elif score <= 2:
        print("Booo... you're a DTS fan! ")

main()