import requests
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
from datetime import datetime
import time
time.sleep(1)

def get_crypto_data(coin_id="bitcoin", days="max", currency="usd"):
    """It pulls historical cryptocurrency prices from the CoinGecko API."""
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"

    params = {
        "vs_currency": currency,
        "days": days,
        "interval": "daily"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if "prices" not in data:
            print("The API response does not contain the 'prices' key")
            return None
        
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error on API call: {e}")
        return None

def prepare_data(data):
    """Prepares data for visualization"""
    # Data processing by using Pandas""
    df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("date", inplace=True)

    # For candlestick - we need to simulate OHLC data
    df['open'] = df['price'].shift(1)
    df['high'] = df['price'].rolling(24).max()
    df['low'] = df['price'].rolling(24).min()
    df['close'] = df['price']
    df.dropna(inplace=True)

      # Calculate 7-day moving average
    df['7_day_MA'] = df['close'].rolling(window=7).mean()

    return df

def visualize_data(df, coin_id="bitcoin"):
    """Creates visualizations of cryptocurrency data."""
    ohlc = df[['open', 'high', 'low', 'close']]
    mpf.plot(ohlc, type='candle', style='charles',
             title=f'Candlestick chart for {coin_id.upper()}',
             ylabel='Price (USD)',
             volume=False,
             figsize=(12,6))


if __name__ == "__main__":
    # Get data
    coin = "ethereum"  
    data = get_crypto_data(coin_id=coin, days="365")
    
    if data:
        # Prepare data
        df = prepare_data(data)
        
        # Visualize
        visualize_data(df, coin_id=coin)
        
        # Save to CSV
        df.to_csv(f"{coin}_prices.csv")
        print(f"Data stored in {coin}_prices.csv")
