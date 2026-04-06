def main():
    check = float(input("Bill amount: "))
    tip = int(input("Tip (in percentage): "))
    result = check * tip / 100
    print(f"Check: ${check:.2f}")
    print(f"Gratuity: ${result:.2f}")
    total = check + result
    print(f"Total: ${total:.2f}")
    answer = input(("Are you splitting the check? (Y/N)"))
    if answer == "N":
        print("Thank you! Visit again!")
        return
    elif answer == "Y":
        print("Split among how many people? ")
        persons = int(input("Persons: "))
        split_total = total / persons
        print(f"The split total per person is: ${split_total:.2f} ")
        print("Thank you! Visit again!")

main()