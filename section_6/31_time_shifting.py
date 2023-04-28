import pandas as pd

df = pd.read_csv('../Data/starbucks.csv', index_col='Date', parse_dates=True)

print(df.head())

print(df.shift(1))

print(df.shift(periods=1, freq='M'))