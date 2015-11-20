%matplotlib qt
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 


url = "http://donnees.ville.montreal.qc.ca/storage/f/2014-01-20T20%3A48%3A50.296Z/2013.csv"

df = pd.read_csv(url, index_col = 'Date', parse_dates = True, dayfirst = True)
df.head(2)

# get summary
df.describe()

df[['Berri1', 'PierDup']].plot()

#get the weekday 
df.index.weekday

days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                 'Saturday', 'Sunday'])
df['Weekday'] = days[df.index.weekday]

#attendance as a function of weekday
df_week = df.groupby('Weekday').sum()
df_week

