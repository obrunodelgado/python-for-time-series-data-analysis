import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from pylab import rcParams
rcParams['figure.figsize'] = 12, 10

airline = pd.read_csv('../Data/airline_passengers.csv', index_col='Month', parse_dates=True)
airline.dropna(inplace=True)

result = seasonal_decompose(airline['Thousands of Passengers'], model='multiplicative')

result.plot()

plt.show()