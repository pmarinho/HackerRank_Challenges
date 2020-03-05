# Calendar Module


import calendar

MM, DD, YYYY = map(int, input().split())

week_day = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]


idx = calendar.weekday(YYYY, MM, DD)

print(week_day[idx])
