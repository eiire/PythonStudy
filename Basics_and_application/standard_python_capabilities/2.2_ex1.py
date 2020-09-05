# task 1
import datetime
year, month, day = input().split(' ')
date = datetime.date(year=int(year),
                     month=int(month),
                     day=int(day),
                     )
days_pass = int(input())

delta = datetime.timedelta(
    days=days_pass,
)

new_date = date + delta
# print(delta)
# print(date)
print(new_date.year, new_date.month, new_date.day)