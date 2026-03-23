#x = float(input("Enter x: "))
#y = float(input("Enter y: "))
#z = int(x) + int(y) 
#print(f"Answer: {round(x / y, 2):,}")
#print(f"Answer: {x / y:.2f}")
#print(int(input("Enter x: ")) + int(input("Enter y: ")))
def main():
    x = int(input("Enter value of x: "))
    print("x sqaured is", square(x))
    print("x divided by 2 is", half(x))

def square(n):
    return pow(n, 2)   

def half(n):
    return n / 2  #can use n * n or n**2
    


main()