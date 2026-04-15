vowels = ["a", "e", "i", "o", "u"]
def main():
    word = input("Input: ")
    result = shorten(word)
    print(f"Output: {result}")
    
def shorten(word):

    result = ""

    for char in word:
        if char.lower() not in vowels:
            result += char
    return result

if __name__=="__main__":
    main()