def main():
    while True:
        try:
            x,y = (input("Fraction: ").split("/"))
            x,y = int(x), int(y)
            if x < 0 or x > y:
                raise ValueError
            fuel = get_level(x,y)
            if fuel == "E" or fuel == "F":
                print(fuel)
            else:
                print(f"{fuel}%")
            break
        except (ValueError, ZeroDivisionError):
            continue
        


def get_level(x,y):
    level = round(x / y * 100)
    if level <= 1:
        return "E"
    if level >= 99:
        return "F"
    return level

main()
    

    