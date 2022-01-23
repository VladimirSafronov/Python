# 15 Дано число. Проверить кратно ли оно 7 и 23
# def isMultiple (x, a, b):
#     if (x % a == 0 and x % b == 0):
#         return True
#     else:
#         return False
# print(isMultiple(161, 7, 23))

# 16 Дано число обозначающее день недели. Выяснить является номер дня недели выходным

# def isWeekend (a):
#     if a == 6 or a == 7:
#         return True
#     else:
#         return False

# 17 По двум заданным числам проверять является ли одно квадратом другого

# def isNumberSqrt (a, b):
#     if a == b ** 2 or b == a ** 2:
#         return True
#     else:
#         return False

# 18 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

# def isItTrue (x, y, z):
#     return not(x or y or z) == (not x and not y and not z)
# for x in range (0, 2):
#     for y in range (0, 2):
#         for z in range (0, 2):
#             print(isItTrue(x, y, z))

# 19 Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

# def getQuarter (x, y):
#     if x == 0 or y == 0:
#         return -1
#     if x > 0 and y > 0:
#         return 1
#     if x < 0 and y > 0:
#         return 2
#     if x < 0 and y < 0:
#         return 3
#     else:
#         return 4
# print(getQuarter(1, -1))

# 20 Задать номер четверти, показать диапазоны для возможных координат

# def showDiapasones (n):
#     if n == 1:
#         return 'x > 0, y > 0'
#     if n == 2:
#         return 'x < 0, y > 0'
#     if n == 3:
#         return 'x < 0, y < 0'
#     if n == 4:
#         return 'x > 0, y < 0'
#     else:
#         return 'Укажите номер четверти от 1 до 4'

# 21 Программа проверяет пятизначное число на палиндромом

# def checkPalindrome (n):
#     if n // 10000 % 10 == n % 10 and n // 1000 % 10 == n / 10 % 10:
#         return True
#     else:
#         return False

# 22 Найти расстояние между точками в пространстве 2D/3D

# import math
# def searchDistancePoints3D(x1, y1, z1, x2, y2, z2):
#     return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2) + math.pow((z2 - z1), 2))

