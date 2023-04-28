import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../Data/starbucks.csv', index_col='Date', parse_dates=True)

print(df.head())

# daily --> yearly
print(df.resample(rule='A').mean())


def first_day(entry):
    if len(entry):
        return entry[0]


print(df.resample(rule='A').apply(first_day))

df['Close'].resample('A').mean().plot.bar()

title = 'Montlhly Max Closing Price for Starbucks'
df['Close'].resample('M').max().plot.bar(figsize=(16, 6), title=title)

plt.show()