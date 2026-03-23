# name = input("What's your name? ")
# if name == "Harry" or name == "Hermione" or name == "Ron":
    # print("Gryffindor")
# elif name == "Draco":
    # print("Slytherin")
# else:
    # print("Umm... who?")

print("What's your name? ")
name = input()
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Ummm... who?")