import random

cards = ["Jack", "Queen", "King"]

def main():
    random.seed(1)
    print(random.choices(cards, weights=[25, 50, 25], k=2))


main()