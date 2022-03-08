def DayOfWeek(day, n):
    for i in range(n):
        if day == 7:
            day = 0
        day += 1
    return day
print(DayOfWeek(7, 31))