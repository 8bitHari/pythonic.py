def main():
    expression = input("Expression: ")
    x, operator, y = expression.split(" ")
    x = int(x)
    y = int(y)

    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    elif operator == "*":
        print(x * y)
    elif operator == "/":
        print(x / y, 1)
main()