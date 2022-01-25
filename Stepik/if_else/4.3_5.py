# Дан порядковый номер месяца (1, \, 2, \ldots, 12)(1,2,…, 12).
# Напишите программу, которая выводит на экран количество дней в этом месяце.
# Принять, что год является невисокосным.

month = int(input())
if month in (4, 6, 9, 11):
	print(30)
elif month == 2:
	print(28)
else:
	print(31)


# from datetime import datetime, timedelta
# last_day_of_month = datetime(2022, (month % 12) + 1, 1) - timedelta(days=1)
# print(last_day_of_month.day)
