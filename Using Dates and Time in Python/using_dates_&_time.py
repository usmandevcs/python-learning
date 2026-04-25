# Using Dates and Time in Python:
'''
Today we learn how to use dates and time in Python. We will be 
using the `datetime` module, which provides classes for 
manipulating dates and times.
'''
# import datetime
# INTRODUCTION TO THE datetime MODULE: 
'''
The `datetime` module provides several classes for working with
dates and times. The most commonly used classes are:
- `datetime`: This class represents a single point in time, 
including the date and time.
- `date`: This class represents a date (year, month, and day).
- `time`: This class represents a time (hour, minute, second, and microsecond).
- `timedelta`: This class represents a duration, the difference
between two dates or times.
- `tzinfo`: This class provides time zone information.
To use the `datetime` module, you need to import it first:
'''
import datetime
# GETTING THE CURRENT DATE AND TIME:
now = datetime.datetime.now() # for time we use now() method of datetime class
print(f"Current date and time: {now}")

# GETTING THE CURRENT DATE:
today = datetime.date.today()
print(f"Today's date: {today}")

# GETTING THE CURRENT TIME:
current_time = datetime.datetime.now().time()
print(f"Current time: {current_time}")

# CREATING A SPECIFIC DATE AND TIME:
specific_datetime = datetime.datetime(2022, 1, 1, 12, 0, 0)
print(f"Specific date and time: {specific_datetime}")

# USEFUL METHODS:

# 1. `strftime()`: This method formats a date or time object into a string
formatted_date = now.strftime("%d-%m-%Y %H:%M:%S") # this is date and time specified format. for this we use strftime() method of datetime class. this method takes a format string as an argument and returns a formatted string representation of the date or time object.
print(f"Formatted date and time: {formatted_date}")

# 2. `strptime()`: This method parses a string into a date or time object
date_string = "01-01-2022 12:00:00"
parsed_datetime = datetime.datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S") # this method takes a date string and a format string as arguments and returns a datetime object.
print(f"Parsed date and time: {parsed_datetime}")

# 3. `timedelta()`: This class represents a duration, the difference between two dates or times
delta = datetime.timedelta(days=7)
future_date = today + delta
print(f"Date after 7 days: {future_date}")

# 4. `replace()`: This method allows you to replace specific components of a date or time object
replaced_datetime = now.replace(year=2023)
print(f"Replaced date and time: {replaced_datetime}")

# 5. `weekday()`: This method returns the day of the week as an integer (0 for Monday, 6 for Sunday)
weekday = today.weekday()
print(f"Today's weekday (0=Monday, 6=Sunday): {weekday}")

# 6. `isoformat()`: This method returns the date or time in ISO 8601 format
iso_date = today.isoformat()
print(f"Today's date in ISO format: {iso_date}")

# 7. `timestamp()`: This method returns the number of seconds since the epoch (January 1, 1970)
timestamp = now.timestamp()
print(f"Current timestamp: {timestamp}")

# 8. `fromtimestamp()`: This method creates a datetime object from a timestamp
datetime_from_timestamp = datetime.datetime.fromtimestamp(timestamp)
print(f"Datetime from timestamp: {datetime_from_timestamp}")

# 9. `utcnow()`: This method returns the current UTC date and time
utc_now = datetime.datetime.utcnow()
print(f"Current UTC date and time: {utc_now}")

# 10. `astimezone()`: This method converts a datetime object to a different
# time zone
local_time = now.astimezone()
print(f"Local date and time: {local_time}") 

# CONCLUSION:
'''
In this tutorial, we have learned how to use the `datetime` module
in Python to work with dates and times. We have covered how to get
the current date and time, create specific date and time objects, and
use various methods to manipulate and format dates and times. The
`datetime` module is a powerful tool for handling date and time data in
Python, and it provides a wide range of functionality for working with
dates and times in various formats and time zones.
'''