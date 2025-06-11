import datetime

def sol(a, b):
    current_date = datetime.date(2022, 11, a)
    weeks = datetime.timedelta(weeks=b)
    that_day = current_date + weeks
    if that_day.year == 2022 and that_day.month == 11:
        return 1
    else:
        return 0

if __name__ == '__main__':
    a = int(input())
    b = int(input())
 
    print(sol(a, b))
