import sys
import csv
from tabulate import tabulate
 
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    filename = sys.argv[1]
    menu = []
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(menu, headers="keys", tablefmt="grid"))


main()