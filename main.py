import calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2021, 3))
print()

print(calendar.monthcalendar(2021, 3))
print()

print(calendar.calendar(2021))
print()

day_of_the_week = calendar.weekday(2021, 3, 4)
print(day_of_the_week)

is_leap = calendar.isleap(2021)

print(is_leap)