import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../Data/starbucks.csv', index_col='Date', parse_dates=True)

df.plot()

plt.show()

df['Close'].plot()

plt.show()

df['Volume'].plot()

plt.show()

title = 'Starbucks Closing Stock Prices'
ylabel = 'Closing Price (USD)'
xlabel = 'Closing Date'

ax = df['Close'].plot(figsize=(12, 6), title=title)
ax.autoscale(axis='both', tight=True)
ax.set(xlabel=xlabel, ylabel=ylabel)

plt.show()

df['Close']['2017-01-01':'2017-12-31'].plot(figsize=(12, 4)).autoscale(axis='x', tight=True)

plt.show()

df['Close'].plot(figsize=(12, 4), xlim=['2017-01-01', '2017-12-31'])

plt.show()

df['Close'].plot(figsize=(12, 4), ylim=[0,70])

plt.show()