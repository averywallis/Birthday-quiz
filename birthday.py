"""
birthday.py
Author: Avery Wallis
Credit: Payton Stearns
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:
  You were born on Halloween!
If the user's birthday fell on today's date, then respond with:
  Happy birthday!
Otherwise respond with a statement like this:
  Peter, you are a winter baby of the nineties.
Example Session:
  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
todayyear= datetime.today().year

name= input('Hello, what is your name?')
month= input('Hi ' +name+ ', what was the name of the month you were born in?')
list= ['thing','January','Febraury','March','April','May','June','July','August','September','October','November','December']
year= int(input('And what year were you born in, '+name+'?'))
day= int(input('And the day?'))

month_name[list.index('October')]
if month in ['October'] and day==31:
        print('You were born on Halloween!')

elif month==todaymonth and day==todayday:
    print('Happy birthday!')
elif year < 1980:
    if month in ['December', 'January', 'February']:
        print(name + ', you are a winter baby of the stone age.')
    if month in ['March', 'April', 'May']:
        print(name + ', you are a spring baby of the stone age.')
    if month in ['June', 'July', 'August']:
        print(name + ', you are a summer baby of the stone age.')
    if month in ['September', 'October', 'November', 'December']:
        print(name + ', you are a fall baby of the stone age.')
elif year >= 1980 and year <= 1989:
    if month in ['December', 'January', 'February']:
        print(name + ', you are a winter baby of the eighties.')
    if month in ['March', 'April', 'May']:
        print(name + ', you are a spring baby of the stone age.')
    if month in ['June', 'July', 'August']:
        print(name + ', you are a summer baby of the stone age.')
    if month in ['September', 'October', 'November', 'December']:
        print(name + ', you are a fall baby of the stone age.')
if year >=1990 and year <= 1999:
    print('stuff')
if year >= 200 and year<= todayyear:
    print('right')
print(todaymonth)
print(month_name[list.index('October')])