import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../Data/starbucks.csv', index_col='Date', parse_dates=True)

df['Close'].plot(figsize=(12,5))

df.rolling(window=30).mean()['Close'].plot()

df['Close: 30 Day Mean'] = df['Close'].rolling(window=30).mean()

df[['Close', 'Close: 30 Day Mean']].plot(figsize=(12,5))

df['Close'].expanding().mean().plot(figsize=(12,5))

plt.show()

