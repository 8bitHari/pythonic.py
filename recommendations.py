import time
def main():
    print("Do you prefer Difficult or Casual games? ")
    difficulty = input()
    if not(difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return
    time.sleep(1)
    print("\nMultiplayer or Single-player? ")
    type = input()
    if not(type == "Multiplayer" or type == "Single-player"):
        print("Enter a valid number of players")
        return
    if difficulty == "Difficult" and type == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and type == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and type == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")
    
        

def recommend(game):
    print("You might like", game)


main()