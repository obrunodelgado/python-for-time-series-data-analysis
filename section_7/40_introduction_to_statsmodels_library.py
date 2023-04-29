import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.filters.hp_filter import hpfilter

df = pd.read_csv('../Data/macrodata.csv', index_col=0, parse_dates=True)

print(df.head())

df['realgdp'].plot(figsize=(12, 5))

plt.show()

gdp_cycle, gdp_trend = hpfilter(df['realgdp'], lamb=1600)

print(type(gdp_cycle))
print(type(gdp_trend))

df['trend'] = gdp_trend
df['cycle'] = gdp_cycle

# total
df[['trend', 'realgdp']].plot(figsize=(12, 5))

# great resession
df[['trend', 'realgdp']]['2005-01-01':].plot(figsize=(12, 5))

plt.show()

gdp_cycle.plot(figsize=(12, 5))

plt.show()