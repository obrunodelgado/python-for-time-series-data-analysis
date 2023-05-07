import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.tsa.statespace.tools import diff


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

mae = mean_absolute_error(test_data, test_predictions)
mse = mean_squared_error(test_data, test_predictions)
test_predictions_mean = test_predictions.mean()
sqrt = np.sqrt(mse)

print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'Square Root of Mean Squared Error vs Std: {sqrt} / {test_data.std().values[0]}')
print(f'Test Data Mean : {test_data.mean().values[0]}')

final_model = ExponentialSmoothing(df['Thousands of Passengers'], trend='mul', seasonal='mul', seasonal_periods=12).fit()

forecast_predictions = final_model.forecast(36)

df['Thousands of Passengers'].plot(legend=True, label='TRAIN', figsize=(12, 8))
forecast_predictions.plot(legend=True, label='PREDICTION', figsize=(12, 8))

plt.show()

df2 = pd.read_csv('../Data/samples.csv', index_col=0, parse_dates=True)
print(df2.head())

# stationary data
df2['a'].plot()
plt.show()

# non-stationary data
df2['b'].plot()
plt.show()

# first_order_difference = df2['b'] - df2['b'].shift(1) # same as below
diff(df2['b'], k_diff=1).plot()
plt.show()