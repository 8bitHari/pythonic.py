def main():
    greeting = phrase(input("Greeting: "))
    return greeting

def phrase(p):
    p = p.lower().strip()
    if p.startswith("hello"):
        print("$0")
    elif p.startswith("hey"):
        print("$20")
    else:
        print("$100")
    
main()
    