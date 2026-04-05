months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                month, day, year = date.split("/")
                print(f"{year}-{int(month):02}-{int(day):02}")
            else:
                month, day, year = date.replace(",", "").split(" ")
                print(f"{year}-{months.index(month) + 1}-{int(day):02}")
            break
        except ValueError:
            continue

main()