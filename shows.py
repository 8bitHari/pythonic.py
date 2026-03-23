SHOWS = [
    " Avatar : The Last Airbender",
    "ben 10",
    " Arthur",
    "Spongebob Squarepants",
    " phineas and ferb",
    "jimmy Neutron",
    "Family Guy",
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    print("\n ".join(cleaned_shows))

main()