# Из почтового адреса нужно извлечь логин (то, что идет до @).
s = input()
print(s[:s.index('@')])
# print(input().split("@")[0])
