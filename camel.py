def main():
    camelCase = (snake_case(input("camelCase: ")))

def snake_case(s):
    s.lower()
    result =""
    for letter in s:
        if letter.isupper():
            result += "_" + letter.lower()
        else:
            result += letter
    print(f"snake_case: {result}")

main()