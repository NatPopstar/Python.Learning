# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
# put your python code here
a = int(input())
b = int(input())
c = int(input())
d = 0

if a > 0:
	d = d + a
if b > 0:
   d = d + b
if c > 0:
	d = d + c
print(d)
