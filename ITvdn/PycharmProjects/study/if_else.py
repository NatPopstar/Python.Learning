# animal = "bird"
# if animal == "cat":
#    print("Meow")
# elif animal =="dog":
#    print("woof")
# elif animal == "bird":
#    print("tweet")
# else:
#    print("I don't know this animal!")

'''value = 10
result_value_greater_than_zero = True if value > 0 else False
print(result_value_greater_than_zero) '''

'''Рассчитать стоимость товара с учетом скидки. 
Если стоимость больше 100р - скидка 3%, 
если больше 500 р - скидка 5%, 
если больше 1000р - скилка 10%К'''

cost = int(input())
if cost > 100:
    print("Your discount is 3%")
elif cost > 500:
    print("Your discount is 5%")
elif cost > 1000:
    print("Your discount is 10%")
else:
    print("You didn`t have any discount")