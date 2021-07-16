"""Вычислите сумму всех целых чисел от 16 до 24 включительно."""

#print(sum(range(16, 25)))

result = 0
for i in range(16, 25):
    result = result + i
print(result)