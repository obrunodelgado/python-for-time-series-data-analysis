from datetime import datetime
import numpy as np

my_year = 2023
my_month = 5
my_day = 27
my_hour = 9
my_minute = 36
my_second = 45

my_date = datetime(my_year, my_month, my_day)
print(my_date)

my_date_time = datetime(my_year, my_month, my_day, my_hour, my_minute, my_second)
print(my_date_time)

print(my_date_time.year)
print(my_date_time.month)
print(my_date_time.day)

np_date = np.array(['2023-05-27', '2023-05-28', '2023-05-29'], dtype='datetime64')
print(type(np_date))

date_range = np.arange('2023-05-27', '2023-06-01', dtype='datetime64')
print(date_range)

date_range_2 = np.arange('2023-04-27', '2023-06-01', 7, dtype='datetime64[D]')
print(date_range_2)

date_range_3 = np.arange('1988', '2023', dtype='datetime64[h]')
print(date_range_3)