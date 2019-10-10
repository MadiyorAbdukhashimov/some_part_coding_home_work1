import calendar
month, day, year = input().split(" ")
header = (calendar.weekday(int(year), int(month), int(day)))
header+=1
if header == 1:
    print("Monday".upper())
elif header == 2:
    print("Tuesday".upper())
elif header == 3:
    print("Wednesday".upper())
elif header == 4:
    print("Thursday".upper())
elif header == 5:
    print("Friday".upper())
elif header == 6:
    print("Saturday".upper())
else:
    print("Sunday".upper())

