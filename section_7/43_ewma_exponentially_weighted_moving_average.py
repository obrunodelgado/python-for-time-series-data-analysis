import pandas as pd
import matplotlib.pyplot as plt

airline = pd.read_csv('../Data/airline_passengers.csv', index_col='Month')
airline.dropna(inplace=True)
airline.index = pd.to_datetime(airline.index)

print(airline.head())

airline['6-month-SMA'] = airline['Thousands of Passengers'].rolling(window=6).mean()
airline['12-month-SMA'] = airline['Thousands of Passengers'].rolling(window=12).mean()

airline.plot(figsize=(12, 8))

plt.show()

airline['EWMA-12'] = airline['Thousands of Passengers'].ewm(span=12).mean()

airline[['Thousands of Passengers', 'EWMA-12']].plot(figsize=(12, 8))

plt.show()