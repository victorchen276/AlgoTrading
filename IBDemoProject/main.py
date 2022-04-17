
from ibapi.client import EClient
from ibapi.common import BarData
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

from datetime import datetime

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error {} {} {}".format(reqId, errorCode, errorString))

    def contractDetails(self, reqId, contractDetails):
        print("reqID: {}, contract:{}".format(reqId, contractDetails))

    def historicalData(self, reqId: int, bar: BarData):
        print("HostroicalData. RegId:", reqId, "BarData.", bar)

app = TradingApp()
app.connect("127.0.0.1", 7497, clientId=0)

contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange ="ISLAND"
# app.reqContractDetails(100, contract)

# app.reqHistoricalData(reqId=1,
#                       contract=contract,
#                       endDateTime='',
#                       durationStr='3 M',
#                       barSizeSetting='5 mins',
#                       whatToShow='MIDPOINT',
#                       useRTH=1,
#                       formatDate=1,
#                       keepUpToDate=0,
#                       chartOptions=[])

queryTime = (datetime.datetime.today() - datetime.timedelta(days=180)).strftime("%Y%m%d %H:%M:%S")
app.reqHistoricalData(4103, contract, queryTime, "1 M", "1 day", "SCHEDULE", 1, 1, False, [])

app.run()

print('aaaa')



# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
