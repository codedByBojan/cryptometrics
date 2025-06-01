import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_crypto_data(coin_id="bitcoin", days="max", currency="usd"):
    """It pulls historical cryptocurrency prices from the CoinGecko API."""
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"

    headers = {
        "currency": currency,
        "days": days,
        "interval": "daily"
    }

    response = requests.get(url, headers=headers)
    data = response.json()