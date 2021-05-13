
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import concurrent.futures
import json, os
import logging
import re
import threading
import time
from sys import argv
from dotenv import load_dotenv
load_dotenv()

# t0 = time.time()

def main(symbol):
  """Calls the coinmarketcap API to grab the coins values

  Args:
      symbol {str}: Coin's Symbol

  Returns:
      {str}: Coin's description grabbed from the API
  """
  api_key = os.getenv("API_KEY")

  # url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  # parameters = {
  #   'start':'1',
  #   'limit':'2',
  #   'convert':'USD'
  # }

  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
  parameters = {
    'symbol': symbol
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    logging.debug(response)
    data = json.loads(response.text)
    logging.debug(data)

    # with open("crypto_request_log.json", "a+") as f:
    #     json.dump(data, f, indent=4, sort_keys=True)
    # with open("crypto_request_log_list.json", "a+") as f:
    #     json.dump(data, f)
    price_data = data['data'][symbol]['description']
    logging.debug(price_data)

    coin_object = {
      'price_data': price_data,
      'symbol': symbol
    }

    return (coin_object)

  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

def find_key_values(coin_object):
  """Runs REGEX to find  coins price in description
     Passes price to a few conditional checks 

  Args:
      price_data {str}: coins description 
  """

  pattern = re.compile('[0-9]*,?[0-9]*\.[0-9]+\s+USD')
  price = pattern.search(coin_object['price_data']).group(0)
  logging.debug(f"Price after re search {price}")
  price = price.replace(" USD","")
  logging.info(f"{coin_object['symbol']}: ${price}")

  #remove commas from price
  price = price.replace(",","")

  if float(price) > 400:
    logging.debug(f"Dont buy you fucking nut | PRICE:{price}")
  else:
    logging.debug(f"Buy it now! | PRICE:{price}")

  """
  Create function to send request to coinbase, pancakeswap, binance
  Use Chris's Card to buy coins
  """



if __name__ == '__main__':
  format='%(asctime)s | %(name)s | %(levelname)s : %(message)s'
  logging.basicConfig(
      format=format, 
      level=logging.DEBUG,
      handlers=[
          logging.FileHandler("coinmarketcap.log"),
          logging.StreamHandler()
      ]
  )
  
  with open("config.json") as f:
      coin_dict = json.load(f)

  for coin in (coin_dict['coins']):
      # results = main(argv[1].upper())
      results = main(coin.upper())
      find_key_values(results)

  # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
  #   executor.map(find_key_values(results), range(3))


  ### Execution time 
  # t1 = time.time()
  # total = t1-t0
  # print(f"EXECUTION TIME: {total}")

