"""У нас есть бюджет: 1572 рубля. На вход нам подается стоимость некоторого товара. Нужно вычислить, сколько единиц этого товара мы можем купить, используя полностью наш бюджет.

Покупать дробные единицы товара мы не можем.

Вполне возможно, что мы не сможем купить ни одной единицы товара. То есть ответом будет 0."""

#import math
#print(math.floor(1572/float(input())))

print(int(1572 // float(input())))