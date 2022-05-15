

from polygon import RESTClient
import requests
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()

def main():
    configure()
    print("aaaaa"+os.getenv('api_key'))

# client = RESTClient()
#
# financials = client.get_ticker_details("NFLX")
# print(financials)

if __name__ == '__main__':
    main()

