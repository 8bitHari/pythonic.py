def main():
    time = convert(input("What time is it? : "))
    if 7 <= time <= 8:
        print("Breakfast time! ")
    elif 12 <= time <= 13:
        print("Lunch time! ")
    elif 18 <= time <= 19:
        print("Dinner time! ")

def convert(time):
    hours , minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60

if __name__ == "__main__":
    main()
