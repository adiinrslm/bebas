# date and time

import datetime as dt
today_data = dt.date.today()

print(today_data)
print(f"Today is = {today_data:%A}")

# or we can use this way
date_data = dt.date(2003,5,21)
print(date_data)
print(f"The day is = {date_data:%A}")

print("\n"+2*"="+"PLEASE INPUT YOUR BIRTHDAY DATA HERE"+"="*2)
date = int(input("Date \t:"))
month = int(input("Month \t:"))
year = int(input("Year \t:"))

born_date = dt.date(year,month,date)
print(f"You was born on = {born_date}")
print(f"The day you was born is = {born_date:%A}")

today = dt.date.today()
print(f"Today date is = {today}")
age = today - born_date
your_age = age.days // 365
print(f"Your age today is = {your_age} years old")