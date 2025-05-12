import numpy as np
import pandas as pd
import mplfinance as mpf # mplfinance for candle plotting

def generate_stock_data(days=100, initial_price=340000, drift=0.0001, volatility=0.02):
    dt = 1  # Each step represents one day
    prices = [initial_price]
    for _ in range(days - 1):
        z = np.random.normal(0, 1)
        increment = (drift - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * z
        new_price = prices[-1] * np.exp(increment)
        prices.append(new_price)
    return prices

# Generate data
np.random.seed(42)
prices = generate_stock_data(days=12, initial_price=33920, drift=-0.005, volatility=0.005)

#OHLC Data
ohlc_data = []
for i in range(len(prices) - 1):
    open_price = prices[i] # open(current) = close(previous)
    close_price = prices[i + 1] # close = current
    high_price = max(open_price, close_price) * (1 + np.random.uniform(0, 0.01))
    low_price = min(open_price, close_price) * (1 - np.random.uniform(0, 0.01))
    ohlc_data.append([open_price, high_price, low_price, close_price]) #append the ohlc data for today

#Creating a DataFrame
dates = pd.date_range(start='2023-01-01', periods=len(ohlc_data), freq='D')
ohlc_df = pd.DataFrame(ohlc_data, columns=['Open', 'High', 'Low', 'Close'], index=dates)

# Candlestick Chart Plott:
mpf.plot(ohlc_df, type='candle', style='yahoo', title='Simulated Stock Prices using Geometric Brownian Motion', ylabel='Price')
