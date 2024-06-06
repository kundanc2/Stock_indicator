import requests

class DataFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_news(self, stock_ticker):
        url = f'https://newsapi.org/v2/everything?q={stock_ticker}&apiKey={self.api_key}'
        response = requests.get(url)
        return response.json()
