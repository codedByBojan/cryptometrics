import requests
import pandas as pd
import matplotlib.pyplot as plt
import time
time.sleep(1)

def get_crypto_data(coin_id="bitcoin", days="max", currency="usd"):
    """It pulls historical cryptocurrency prices from the CoinGecko API."""
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"

    params = {
        "currency": currency,
        "days": days,
        "interval": "daily"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Greska pri: {e}")
        return None

def save_to_csv(data, filename="crypto_prices.csv")
    # Data processing by using Pandas
    df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.to_csv(filename, index=False)
    print(f"Podaci sačuvani u {filename}")

    # Visualization
    plt.style.use("seaborn")
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["price"], label=f"{coin_id.upper()} price in {currency.upper()}")
    plt.title(f"Price history: {coin_id.upper()}")
    plt.xlabel("Date")
    plt.ylabel(f"Price ({currency.upper()})")
    plt.legend()
    plt.grid()
    plt.show()

get_crypto_data(coin_id="bitcoin", days="365", currency="usd")