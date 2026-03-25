vowels = ["a", "e", "i", "o", "u"]
def main():
    vowel = input("Input: ")
    result = without_vowel(vowel)
    print(f"Output: {result}")

def without_vowel(v):
    v = v.lower()
    result = ""

    for char in v:
        if char not in vowels:
            result += char
    return result

main()
        

