import warnings
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pandas.plotting import lag_plot
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import acovf, acf, pacf, pacf_yw, pacf_ols

warnings.filterwarnings('ignore')

# non-stationary data
df1 = pd.read_csv('../Data/airline_passengers.csv', index_col='Month', parse_dates=True)
df1.index.freq = 'MS'

# stationary data
df2 = pd.read_csv('../Data/DailyTotalFemaleBirths.csv', index_col='Date', parse_dates=True)
df2.index.freq = 'D'

lag_plot(df1['Thousands of Passengers'])
plt.show()

lag_plot(df2['Births'])
plt.show()

plot_acf(df1, lags=40)
plt.show()

plot_acf(df2, lags=40)
plt.show()

plot_pacf(df2, lags=40, title='Daily Female Births')
plt.show()