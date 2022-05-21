

from polygon import RESTClient
import requests
from dotenv import load_dotenv
import os



def configure():
    load_dotenv()

def main():
    configure()
    # print(os.getenv('POLYGON_API_KEY'))
    client = RESTClient(api_key=os.getenv('POLYGON_API_KEY'))
    # financials = client.get_ticker_details('NFLX')
    # print(financials)
    aggs = client.get_aggs("AAPL", 1, "day", "2022-04-04", "2022-04-04")
    print(aggs)
    trades = []
    for t in client.list_trades("AAA", "2022-04-04", limit=5):
        trades.append(t)
    print(trades)

if __name__ == '__main__':
    main()

