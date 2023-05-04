import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.holtwinters import ExponentialSmoothing


df = pd.read_csv('../Data/airline_passengers.csv', index_col='Month', parse_dates=True)
df.index.freq = 'MS'

print(df.head())

train_data = df.iloc[:109]
test_data = df.iloc[108:]

fitted_model = ExponentialSmoothing(train_data['Thousands of Passengers'], trend='mul', seasonal='mul', seasonal_periods=12).fit()

test_predictions = fitted_model.forecast(36)

train_data['Thousands of Passengers'].plot(legend=True, label='TRAIN', figsize=(12, 8))
test_data['Thousands of Passengers'].plot(legend=True, label='TEST', figsize=(12, 8))
test_predictions.plot(legend=True, label='PREDICTION', figsize=(12, 8))

plt.show()