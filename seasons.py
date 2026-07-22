import sys
from datetime import date

import inflect


def main():
    birth = input("Date of Birth: ")
    try:
        year, month, day = birth.split("-")
        birthdate = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")

    minutes = get_minutes(birthdate)
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    print(f"{words.capitalize()} minutes")


def get_minutes(birthdate):
    today = date.today()
    delta = today - birthdate
    return delta.days * 24 * 60


if __name__ == "__main__":
    main()
