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

    # Data processing by using Pandas
    prices = data["prices"]
    df = pd.DateFrame(prices, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("date", inplace=True)

    # Saving data to CSV format file
    df.to_csv(f"{coin_id}_historical_prices.csv")

    