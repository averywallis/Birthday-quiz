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

name= input('Hello, what is your name? ')
month= input('Hi ' +name+ ', what was the name of the month you were born in? ')
list= ['thing','January','Febraury','March','April','May ','June','July','August','September','October','November','December']
year= int(input('And what year were you born in, '+name+'? '))
day= int(input('And the day?' ))

if month in ['October'] and day==31:
        print('You were born on Halloween!')
elif month==month_name[todaymonth] and day==todaydate:
    print('Happy birthday!')
elif year < 1980:
    if month in ['December', 'January', 'February']:
        print(name + ', you are a winter baby of the Stone age.')
    if month in ['March', 'April', 'May']:
        print(name + ', you are a spring baby of the Stone age.')
    if month in ['June', 'July', 'August']:
        print(name + ', you are a summer baby of the Stone age.')
    if month in ['September', 'October', 'November']:
        print(name + ', you are a fall baby of the Stone age.')
elif year >= 1980 and year <= 1989:
    if month in ['December', 'January', 'February']:
        print(name + ', you are a winter baby of the eighties.')
    if month in ['March', 'April', 'May']:
        print(name + ', you are a spring baby of the eighties.')
    if month in ['June', 'July', 'August']:
        print(name + ', you are a summer baby of the eighties.')
    if month in ['September', 'October', 'November']:
        print(name + ', you are a fall baby of the eighties.')
elif year >=1990 and year <= 1999:
    if month in ['December', 'January', 'February']:
        print(name + ', you are a winter baby of the nineties.')
    if month in ['March', 'April', 'May']:
        print(name + ', you are a spring baby of the nineties.')
    if month in ['June', 'July', 'August']:
        print(name + ', you are a summer baby of the nineties.')
    if month in ['September', 'October', 'November']:
        print(name + ', you are a fall baby of the nineties.')
elif year >= 2000 and year<= todayyear:
    if month in ['December', 'January', 'February']:
        print(name + ', you are a winter baby of the two thousands.')
    if month in ['March', 'April', 'May']:
        print(name + ', you are a spring baby of the two thousands.')
    if month in ['June', 'July', 'August']:
        print(name + ', you are a summer baby of the two thousands.')
    if month in ['September', 'October', 'November']:
        print(name + ', you are a fall baby of the two thousands.')
