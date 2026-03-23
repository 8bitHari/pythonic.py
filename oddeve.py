#num = int(input("Enter a number: "))
#results = {0: "even", 1: "odd"}
#print(f"The number {num} is {results[num % 2]}.")



print("Enter a number: ")
num = int(input())
if num % 2 == 0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")