"""Давайте повторим функциональность калькулятора краски на сайте OBI, только без количества слоев.

Округляйте значения, если нужно, только при их печати. Все вычисления производите с полной точностью."""

a = float(input())
h = float(input())
rashod = float(input())
v = int(input())
procent = int(input())

s = a*h
print(round(s, 2))
l = s/rashod * (1 + procent/100)
print(round(l, 2))
import math
banki = math.ceil(l/v)
print(banki)
print(round(banki * v - l, 2))