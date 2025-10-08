import sys
import json
import requests

if len(sys.argv) != 2:
	sys.exit('Missing command-line argument')

if sys.argv[1].isalpha():
	sys.exit('Command-line argument is not a number')

coins = sys.argv[1]

bit = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
bitcoin = bit.json()

print("${:,.4f}".format (float(bitcoin['bpi']['USD']['rate_float']) * float(coins)))
	
