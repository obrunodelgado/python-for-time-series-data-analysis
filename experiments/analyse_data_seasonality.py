import pandas as pd
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima
from statsmodels.tsa.arima.model import ARIMA


# In this experiment I've tried to understand the seasonality of the data and how it affects the prediction.
# The results were not satisfactory. The prediction was not even close to the real data.

df = pd.read_csv('../Data/airline_passengers.csv', index_col='Month', parse_dates=True)

model = auto_arima(df['Thousands of Passengers'], stepwise=True, trace=True, m=12)
best_seasonal_period = model.seasonal_order[3]

train_data = df.iloc[:109]
test_data = df.iloc[108:]

arima = ARIMA(train_data['Thousands of Passengers'], order=(2, 1, 1))
fitted_model = arima.fit()

test_predictions = fitted_model.forecast(36)

train_data['Thousands of Passengers'].plot(legend=True, label='TRAIN', figsize=(12, 8))
test_data['Thousands of Passengers'].plot(legend=True, label='TEST', figsize=(12, 8))
test_predictions.plot(legend=True, label='PREDICTION', figsize=(12, 8))

plt.show()