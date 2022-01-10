a_1 = int(input())
b_1 = int(input())
a_2 = int(input())
b_2 = int(input())
if (a_2 < b_1) and (b_1 < b_2):
    print(a_2, b_1)
elif (b_1 == a_2):
    print(b_1)
elif (a_1 == a_2) and (b_1 < b_2):
    print(a_1, b_1)
else:
    print("пустое множество")