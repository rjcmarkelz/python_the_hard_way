# import the libraries
import numpy as np 
import pandas as pd 
from pandas import DataFrame, Series
# these two are the workhorse data structures

#####
# Series
# single array of values
#####
s = Series([1, 2, 3, 4])
s

s2 = Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
s2

# look up by index
s2[['a', 'd']]
# or by numerical index
s2[[0,2]]
s2.index

# use series to introduce time series data
dates = pd.date_range('2014-08-01', '2014-08-06' )
dates

# must be the same length
temps1 = Series([80, 82, 85, 90, 83, 87], index = dates)
temps1

temps1.mean()

temps2 = Series([70, 75, 69, 83, 79, 77], index = dates)
temp_diffs = temps1 - temps2
temp_diffs

# or by date
temp_diffs['2014-08-03']
# or by integer position
temp_diffs[2]

#####
# DateFrame
# multiple columns of heterogenous data, but each column of same type
#####

temps_df = DataFrame({'Missoula': temps1, 'Philly' : temps2})
temps_df
temps_df['Missoula']
# change order in return
temps_df[['Philly', 'Missoula']] # notice two 
# or if no spaces
temps_df.Missoula

temp_diffs = temps_df.Missoula - temps_df.Philly

temps_df['Difference'] = temp_diffs
temps_df

# colnames 
temps_df.columns
# slice df

temps_df.Difference[1:4]

# get rows of df index
temps_df.iloc[1]

# index name
temps_df.loc['2014-08-02']

# using 0 indexing
temps_df.iloc[[1, 3, 5]].Difference

# logicals
temps_df.Missoula > 82  # 
temps_df[temps_df.Missoula > 82] # only subsetted rows

#####
# loading CSVs
#####

df = pd.read_csv('data/test1.csv')
df.date

df = pd.read_csv('data/test1.csv', parse_dates = ['date'])
type(df.date[0])

df.index # numeric

# reimport 
df = pd.read_csv('data/test1.csv', parse_dates = ['date'], index_col = 'date')

# load data from the web
from pandas.io.data import DataReader
from datetime import date
from dateutil.relativedelta import relativedelta

goog = DataReader("GOOG", "yahoo", date.today() + relativedelta(months = -3))
goog.head()
goog.tail()

goog.plot(y = 'Adj Close');
