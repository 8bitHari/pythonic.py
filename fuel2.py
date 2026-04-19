def main():
    while True:
        try:
            percentage = convert(input("Fraction: "))
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(s):
    x,y = s.split("/")
    x,y = int(x), int(y)
    if x < 0 or x > y:
        raise ValueError
    return round(x / y * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"

if __name__=="__main__":
    main()