import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.holtwinters import SimpleExpSmoothing, ExponentialSmoothing

df = pd.read_csv('../Data/airline_passengers.csv', index_col='Month', parse_dates=True)
df.dropna(inplace=True)

print(df.index)

df.index.freq = 'MS'  # 'MS' is month start

span = 12
alpha = 2 / (span + 1)

df['EWMA12'] = df['Thousands of Passengers'].ewm(alpha=alpha, adjust=False).mean()

model = SimpleExpSmoothing(df['Thousands of Passengers'])
fitted_model = model.fit(smoothing_level=alpha, optimized=False)
df['SES12'] = fitted_model.fittedvalues.shift(-1)

df['DESadd12'] = ExponentialSmoothing(df['Thousands of Passengers'], trend='add').fit().fittedvalues.shift(-1)
df['DESmul12'] = ExponentialSmoothing(df['Thousands of Passengers'], trend='mul').fit().fittedvalues.shift(-1)

df[['Thousands of Passengers', 'SES12', 'DESadd12', 'DESmul12']].iloc[-24:].plot(figsize=(12, 8))

plt.show()

df['TESmul12'] = ExponentialSmoothing(df['Thousands of Passengers'], trend='mul', seasonal='mul', seasonal_periods=12).fit().fittedvalues
df['TESadd12'] = ExponentialSmoothing(df['Thousands of Passengers'], trend='add', seasonal='add', seasonal_periods=12).fit().fittedvalues

df[['Thousands of Passengers', 'DESmul12', 'TESmul12']].iloc[:24].plot(figsize=(12, 8))

plt.show()