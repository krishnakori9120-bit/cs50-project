import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_API_KEY"
    )
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Request failed")

total = bitcoins * price

print(f"${total:,.4f}")
