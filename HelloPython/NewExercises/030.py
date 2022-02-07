# 30 Вычислить число пи c заданной точностью d
# Пример: при d = 0.001, пи = 3.141

import math


d = 0.00001

def accuracy(d):
    count = 0
    while d != 1:
        d *= 10
        count += 1
    return count

n = accuracy(d)

def func(n):
    return int(math.pi * (10 ** n)) / 10 ** n

print(func(n))