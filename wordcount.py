print("Enter a sentence below: ")
word = input()
print(f"The number of words in \"{word}\" is: ", len(word.split()))
print(f"The number of characters in \"{word}\" is: ", len(word.replace(" ", "")))