import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates

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

ax = df['Close'].plot(xlim=['2017-01-01', '2017-03-01'], ylim=[50, 60], figsize=(12, 5))
ax.set(xlabel='')
ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=0))
ax.xaxis.set_major_formatter(dates.DateFormatter('%d'))

ax.xaxis.set_minor_locator(dates.MonthLocator())
ax.xaxis.set_minor_formatter(dates.DateFormatter('\n\n%b'))

ax.yaxis.grid(True)
ax.xaxis.grid(True)

plt.show()

