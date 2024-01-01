# Write your code here :-)
import re, sys

# Regular expression matching for date
dateRegex = re.compile(r'''(
(0[1-9]|[1-2]\d|3[0-1])/  # day and forward slash
(0[1-9)|1[0-2])/  # month and forwardslash
([1-2]\d{3})  # year
)''', re.VERBOSE)

# User input
myDate = input('Enter the date in DD/MM/YYYY format:')

# Assign date variables
mo = dateRegex.search(myDate)
day = mo.group(2)
month = mo.group(3)
year = mo.group(4)

# Convert date string variables to integers
my_day = int(day)
my_month = int(month)
my_year = int(year)

# Error message function

# Check for 30 day months
def thirty_day_month():
    global my_day
    if my_day > 30:
        print("Error: invalid date")
        sys.exit()
    else:
        return

# Check for leap year
def leap_year():
    global my_year
    if my_year % 4 != 0:
        print("Error: invalid date")
        sys.exit()
    elif my_year % 100 == 0:
        if my_year % 400 != 0:
            print("Error: invalid date")
            sys.exit()
        else:
            return
    else:
        return

if my_month == 2:
    if my_day > 28:
        if my_day == 29:
            leap_year()
        else:
            print("Error: invalid date")
            sys.exit()
elif my_month == 4:
    thirty_day_month()
elif my_month == 6:
    thirty_day_month()
elif my_month == 9:
    thirty_day_month()
elif my_month == 11:
    thirty_day_month()


# Testing
# print(type(month))
# print(mo.group(1))
print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
