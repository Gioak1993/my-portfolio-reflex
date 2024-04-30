
import requests
import os
import dotenv
from datetime import datetime


dotenv.load_dotenv()

class FmpApi:

    

    FMP_API_KEY = os.environ.get("FMP_API_KEY")

    def get_info(self, stock:str):

        url = f'https://financialmodelingprep.com/api/v3/quote-order/{stock}?apikey={self.FMP_API_KEY}'
        stockrequest = requests.get(url)

        if stockrequest.status_code == 200:
            return stockrequest.json()
        else:
            return 'error'
        
    def historical_data(self, stock:str, from_date:str, to_date:str) -> dict:

        fromdate_time = datetime.strptime(from_date, '%Y-%m-%d')
        todate_time = datetime.strptime(to_date, '%Y-%m-%d')

        if fromdate_time > todate_time:
            return {}
        
        url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{stock}?from={from_date}&to={to_date}&apikey={self.FMP_API_KEY}'
        historicalrequest =  requests.get(url)

        if historicalrequest.status_code == 200:             
            return historicalrequest.json()

        else:
            return {}


# fmp_api = FmpApi()

# async def stock_change (stock:str, from_date:str, to_date:str):

    
#     data = await fmp_api.historical_data(stock, from_date, to_date)
#     return data


# print (stock_change('AAPL', '2024-04-01', '2024-04-11'))