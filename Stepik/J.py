#Напишите программу для нахождения цифр четырёхзначного числа.
num = int(input())
d4 = (num%10**1)//10**0
d3 = (num%10**2)//10**1
d2 = (num%10**3)//10**2
d1 = (num%10**4)//10**3
print("Цифра в позиции тысяч равна", d1)
print("Цифра в позиции сотен равна", d2)
print("Цифра в позиции десятков равна", d3)
print("Цифра в позиции единиц равна", d4)
