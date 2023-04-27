import numpy as np
import pandas as pd

date_range = pd.date_range('2023-05-27', periods=8, freq='D')
print(date_range)

date_range_2 = pd.to_datetime(['27/02/1997', '30/11/1988'], format='%d/%m/%Y')
print(date_range_2)

data = np.random.randn(8, 4)
cols = ['A', 'B', 'C', 'D']
idx = pd.date_range('2023-05-27', periods=8, freq='D')
df = pd.DataFrame(data, idx, cols)

print(df.index)
print(df.index.max())