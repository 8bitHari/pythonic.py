def main():
    greeting = value(input("Greeting: "))
    print(greeting)

def value(p):
    p = p.lower().strip()
    if p.startswith("hello"):
        return(0)
    elif p.startswith("hey"):
        return(20)
    else:
        return(100)
    

if __name__=="__main__":
    main()
    