import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return float(data["bpi"]["USD"]["rate_float"])
    except (requests.RequestException, KeyError):
        print("Failed to retrieve Bitcoin price.")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python bitcoin.py <amount>")
        sys.exit(1)

    try:
        amount = float(sys.argv[1])
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    total_price = amount * bitcoin_price
    formatted_price = "${:,.2f}".format(total_price)
    print(formatted_price)
main()
