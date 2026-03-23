def main():
    print("Enter your number below: ")
    x = int(input())
    if is_even(x):
        print(f"{x} is Even.")
    else:
        print(f"{x} is Odd.")

def is_even(n):
   return (n % 2 == 0)


main()