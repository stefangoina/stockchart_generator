import numpy as np
import matplotlib.pyplot as plt

def generate_stock_data(days=100, initial_price=340000, drift=0.0001, volatility=0.02):
    # Generate synthetic stock data using Geometric Brownian Motion
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

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(prices, marker='o', linestyle='-', color='b')
plt.title('Simulated Stock Prices using Geometric Brownian Motion')
plt.xlabel('Days')
plt.ylabel('Price')
plt.grid(True)
plt.savefig('stock_chart.png')
plt.show()