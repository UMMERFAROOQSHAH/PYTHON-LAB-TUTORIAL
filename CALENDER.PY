import calendar
year=int(input("Enter year: "))
month=int(input("Enter month: "))
print(calendar.calendar(year))               #WHOLE YEAR
print(calendar.month(year,month))            #MONTH WISE
