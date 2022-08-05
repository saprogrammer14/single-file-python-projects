import calendar

year = int(input("Enter the year: "))
if year < 1500:
    print("Enter 1500 or more.")
else:
    print(calendar.calendar(year, 2, 1, 6, 3))
