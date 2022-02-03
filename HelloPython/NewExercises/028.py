# 28 Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*

# a != 0
# D = b^2 - 4ac
# D > 0   2 корня, x1,2 = (-b +и- sqrt(D)) / 2a
# D = 0   1 корень, x = -b / 2a
# D < 0   корней нет

from math import sqrt


a = 1
b = -3
c = 5

discriminant = lambda a, b, c: pow(b, 2) - 4 * a * c
disc = discriminant(a, b, c)

def find_rad(arg, a, b):
    if arg > 0:
        return (((-b + sqrt(arg)) / (2 * a), (-b - sqrt(arg)) / (2 * a)))
    if arg == 0:
        return -b / (2 * a)
    if arg < 0:
        return 'корней нет'

print(disc)
print(find_rad(disc, a, b))