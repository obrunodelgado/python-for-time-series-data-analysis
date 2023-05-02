import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.holtwinters import SimpleExpSmoothing

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

df.plot(figsize=(12, 8))

plt.show()