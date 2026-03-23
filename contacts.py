import time
contacts = {}
print("Contacts")
time.sleep(1)
while True:
    print("\n \"Press 1\" to add a new Contact\n \"Press 2\" to Search for a contact by name\n \"Press 3\" to view all contacts\n \"Press 4\" to quit")
    option = int(input("\n Enter option: "))
    if option == 1:
        name = input("Enter name: ")
        time.sleep(1)
        number = input("Enter number: ")
        contacts[name] = number
        print(f"{name} has been saved. ")
    elif option == 2:
        search = input("Enter the name: " )
        print(f"{search}'s number is {contacts[search]}")
    elif option == 3:
        print(f"\n {contacts}")
    elif option == 4:
        break
    else:
        print("Incorrect option")
        
