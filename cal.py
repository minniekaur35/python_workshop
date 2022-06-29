# program for creating a calendar

#import calendar (built-in function in python)
# Get current date
# Extract current month from the date
# check if month is 12 or less
# If less than 12 do a loop otherwise do it for current month

import calendar
from datetime import date

todaydate = date.today()

print (type(todaydate))
print(todaydate.month)

if todaydate.month == 12 :
    print(calendar.month(todaydate.year, todaydate.month, 4, 2))
else :
    # creating an array of months without typing actual number just iterate 
    # then doing a for loop to represent the calendar 

    # months = list()

    # counter = todaydate.month # starting number
    # while counter <= 12:
    #     months.append(counter)
    #     # print(calendar.month(todaydate.year, counter))
    #     counter = counter + 1
    # print(months)
    
    # for i in months:
    #     print(calendar.month(todaydate.year, i))
    
    for i in range(todaydate.month, 12 + 1):
        print(calendar.month(todaydate.year, i))
