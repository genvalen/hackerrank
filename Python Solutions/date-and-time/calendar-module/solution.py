# Original problem: https://www.hackerrank.com/challenges/calendar-module/problem
if __name__ == '__main__':
    import calendar

    month, date, year = map(int, input().split())

    day = calendar.day_name[calendar.weekday(year, month, date)].upper()

    print(day)
