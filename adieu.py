import inflect
p = inflect.engine()

def main():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            break

    print()    
    print(f"Adieu, adieu, to {p.join(names)}")

main()