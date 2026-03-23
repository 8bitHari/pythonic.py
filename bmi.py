def main():
    weight = body_weight(input("What is your weight in KGs?: "))
    height = body_height(input("What is your height in cm?: "))
    height_m = height / 100
    bmi = weight / height_m ** 2 
    if bmi < 18.5:
        print("Underweight!")
    elif 18.5 <= bmi <= 24.9:
        print("Normal weight!")
    elif 25 <= bmi <= 29.9:
        print("Overweight!")
    else:
        print("Obese!")

def body_weight(w):
    return float(w)
def body_height(h):
    return float(h)

main()