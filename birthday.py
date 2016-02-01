"""
birthday.py
Author: Avery Wallis
Credit: None so far
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

temperature = float(input("What is the temperature outside? "))
weather = input("Is it raining or sunny outside? ")
weather = weather.lower() # change to lower case
if temperature < 55 and weather == "raining":
    print("You should bring a warm raincoat.")
elif temperature < 55 and weather == "sunny":
    print("You should bring a fleece.")
elif temperature >= 55 and weather == "raining":
    print("You should bring an umbrella.")
else: # the only combination left is sunny and temperature >= 55
    print("You should bring sunglasses.")