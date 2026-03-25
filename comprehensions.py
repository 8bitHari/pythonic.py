import csv

def main():
    words = get_words("address.txt")
    lowercase_words = [word.lower() for word in words if len(word)>4]
    counts = {word: lowercase_words.count(word) for word in lowercase_words}
    save_counts(counts)

def get_words(counts):
    with open(counts) as f:
        return f.read().split()
    
def save_counts(counts):
    with open ("counts.csv", "w") as f:
        for word, count in counts.items():
            f.write(f"{word},{count}\n")

main()