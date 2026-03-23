print("What is the Answer to the Great Question of Life, the Universe and Everything? ")
answer = input()
if not (answer == "42" or answer == "forty-two" or answer == "forty two"):
    print("No")
else:
    print("Yes")

answer = input().lower().strip()
if answer in ["42", "forty-two", "forty two"]:
    print("Yes")
else:
    print("No")