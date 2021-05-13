import re
import json


with open("config.json") as f:
    coin_dict = json.load(f)

for coin in (coin_dict['coins']):
    print(coin)

print(f"ORIG DICT  |  {coin_dict}")
print(f"DICT ITEMS |  {coin_dict.items()}")
print(f"DICT KEYS  |  {coin_dict.keys()}")

# text = "Internet Computer (ICP) is a cryptocurrency . Internet Computer has a current supply of 469,213,710 with 123,747,067.82 in circulation. The last known price of Internet Computer is 374.14056282 USD and is down -18.89 over the last 24 hours. It is currently trading on 26 active market(s) with $1,605,536,287.43 traded over the last 24 hours. More information can be found at https://dfinity.org."

# pattern = re.compile('[0-9]*\.[0-9]+\s+USD')
# # pattern = re.compile('ICP')

# print(f"PATTERN: {pattern}")
# price = pattern.search(text).group(0)
# print(f"PRICE: {type(price)}")

# price = price.replace(" USD","").split()
# print(f"CONVERT PRICE: {price}")

