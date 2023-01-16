from collections import Counter
from datetime import date, timedelta
from pprint import pprint

date_start: date = date(2023, 1, 1)
date_end: date = date(2023, 12, 31)
total_days: int = (date_end - date_start).days + 1
sunday: int = 6

holidays = [
    date(2023, 1, 1),
    date(2023, 1, 2),
    date(2023, 1, 3),
    date(2023, 1, 4),
    date(2023, 1, 5),
    date(2023, 1, 6),
    date(2023, 1, 7),
    date(2023, 1, 8),
    date(2023, 2, 23),
    date(2023, 2, 24),
    date(2023, 2, 25),
    date(2023, 2, 26),
    date(2023, 4, 29),
    date(2023, 4, 30),
    date(2023, 5, 1),
    date(2023, 5, 8),
    date(2023, 5, 9),
    date(2023, 5, 9),
    date(2023, 5, 9),
    date(2023, 5, 9),
    date(2023, 5, 9),
    date(2023, 6, 12),
    date(2023, 11, 6),
]

days_of_weekend = []
for day in range(total_days):
    cur_day = date_start + timedelta(days=day)
    if cur_day.weekday() not in [5, 6] and cur_day not in holidays:
        days_of_weekend.append(cur_day.day)

counter = dict(Counter(days_of_weekend)).items()
for c in sorted(counter, key=lambda x: (x[1], x[0])):
    print(c)
