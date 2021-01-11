import pandas as pd
import numpy as np

window_size = 2

# Example 1, inversely correlated short series
sample_series_1 = [1, 1.97 ,2.97 ,3.975]
sample_series_2 = [8, 7, 6, 5]

#Example 2, inversely correlated large series
#sample_series_1 = range(1, 100)
#sample_series_2 = range(100, 1, -1)
data = {'ham': sample_series_1, 'burger': sample_series_2}
df = pd.DataFrame(data=data)

df1 = df['ham']
df2 = df['burger']

#print(df)

rolling_sum = df.rolling(window_size).sum()

#print(rolling_sum)

rolling_mean = df.rolling(window_size).mean()

#print(rolling_mean)

ewm = df.ewm(alpha=0.97).corr()

#print(ewm)

ewm_mean = df.ewm(alpha=0.97).mean()

#print(ewm_mean)

rolling_ewm_corr = df1.rolling(window_size).mean().ewm(alpha=0.97).corr(df2)

print(rolling_ewm_corr)
