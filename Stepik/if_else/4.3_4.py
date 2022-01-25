# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.
a = int(input())
b = int(input())
c = int(input())
max_ = max(a, b, c)
min_ = min(a, b, c)
if a != max_ and a != min_:
	print(a)
# for q in (a, b, c):
# 	min_ < a < max_
elif b != max_ and b != min_:
	print(b)
elif c != max_ and c != min_:
	print(c)

# a, b, c = int(input()), int(input()), int(input())
# abc = a,b,c
# a1 = 0
# b1 = 0
# a1 = min(abc)
# b1 = max(abc)
# abc1 = a + b + c
# print(abc1 - a1 - b1)

# a, b, c = int(input()), int(input()), int(input())
# if c < a:
#     a, c = c, a
# if b < a:
#     a, b = b, a
# if c < b:
#     b, c = c, b
# print(b)
