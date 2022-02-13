# working with date and time in python
# the datetime.date class
print("==DATETIME.DATE==")
import datetime as dt
from math import nextafter
from time import time

date1= dt.date.today()
print("year:", date1.year)
print("month:", date1.month)
print("day:", date1.day)

# the datetime.time class
print("\n==DATETIME.TIME==")
import datetime as dt

time1 = dt.time(11, 59, 59, 99999)
print(time1)

print("hour:", time1.hour)
print("minute:", time1.minute)
print("second:", time1.second)
print("microseconds:", time1.microsecond)

# the datetime.datetime class
print("\n==DATETIME.DATETIME CLASS==")
import datetime as dt

datetime_obj = dt.datetime(2022, 2, 13, 11, 59, 59)
print(datetime_obj)
print(datetime_obj.date())
print(datetime_obj.time())

# getting current date and time
print("\n==CURRENT DATE AND TIME==")
import datetime as dt

current_datetime = dt.datetime.now()
print(current_datetime)

# the datetime.timedelta class
print("\n==DATETIME.TIME DELTA CLASS==")
import datetime as dt

current_time = dt.datetime.now()
next_new_year = dt.datetime(2023, 1, 1)

time_remaining = next_new_year - current_time
print(time_remaining)
print(type(time_remaining))

# python strftime() method
print("\n==STRFTIME METHOD==")
import datetime as dt

current_time = dt.datetime.now()
print(current_time)

string_date = current_time.strftime("%A, %B %d, %Y")
print(string_date)

# python strptime() method
print("\n==STRPTIME METHOD==")
import datetime as dt

date_string = "21 May, 2003"

date_object = dt.datetime.strptime(date_string, "%d %B, %Y")
print("date_object:", date_object)