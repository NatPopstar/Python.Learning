# Дано трехзначное число abc, в котором все цифры различны.
# Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.
num = int(input())
d3 = (num%10**1)//10**0
d2 = (num%10**2)//10**1
d1 = (num%10**3)//10**2
print(d1, d2, d3, sep="")
print(d1, d3, d2, sep="")
print(d2, d1, d3, sep="")
print(d2, d3, d1, sep="")
print(d3, d1, d2, sep="")
print(d3, d2, d1, sep="")
