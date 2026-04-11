import requests
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        btc = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=f31ef1837d30beee90ae6c1ab55e57bf3134c6d85de882507fb881dcc02b40ca")
        price = float(response.json()["data"]["priceUsd"])
        print(f"${btc * price:,.4f}")
    except requests.RequestException:
        sys.exit("API request failed")

main()
