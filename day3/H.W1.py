import requests

class CoinMarketCapAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        self.headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": self.api_key
        }

    def get_solana_data(self):
        params = {'symbol': 'SOL', 'convert': 'USD'}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            return self.extract_solana_data(data)

        else:
            return (f"{response.status_code}")

    def extract_solana_data(self, data):
        try:
            solana = next(item for item in data['data'] if item['symbol'] == 'SOL')
            return {

                def extract_solana_data(self, data):
        try:
            solana = next(item for item in data['data'] if item['symbol'] == 'SOL')
            return {
                solana['quote']['USD']['price'],
                solana['quote']['USD']['market_cap'],
                solana['quote']['USD']['percent_change_24h'],
                solana['circulating_supply'],
            }
        except StopIteration:
            return 
            
    api_key = "your_api_key_here" 
    cmc_api = CoinMarketCapAPI(api_key)
    solana_data = cmc_api.get_solana_data()

    print(solana_data)




