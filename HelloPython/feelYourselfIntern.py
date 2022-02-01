# 00 Вывести квадрат числа

# def sqrt(x):
#     return x * x

# 01 По двум заданным числам проверять является ли первое квадратом второго

# def isFirstNumberSqrt (x, y):
#     return x == y * y

# 02 Даны два числа. Показать большее и меньшее число

# def maxNumber (a, b):
#     if a > b:
#         return a
#     else:
#         return b
# def minNumber (a, b):
#     if a < b:
#         return a
#     else:
#         return b
# a = 100
# b = 20
# highNumber = maxNumber (a, b)
# lowNumber = minNumber (a, b)
# print (f'Большее число {highNumber}')
# print(f'Меньшее число {lowNumber}')

# 03 По заданному номеру дня недели вывести его название

# def dayOfWeek (x):
#     week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     return week[x-1]
# print(dayOfWeek(5))

# 04 Найти максимальное из трех чисел

# def maxNumber (a, b, c):
#     maxNum = a
#     if maxNum < b:
#         maxNum = b
#     if maxNum < c:
#         maxNum = c
#     return maxNum

# 05 Написать программу вычисления значения функции y = f(a)

# import math

# def sin (a):
#     return math.sin(a)

# 06 Выяснить является ли число чётным

# def isNumberEven (a):
#     return (a % 2 == 0)

# 07 Показать числа от -N до N

# def showFromNegativeToPositive (n):
#     listNumbers = [0] * (n * 2 + 1)
#     index = 0
#     for i in range(-n, n + 1):
#         listNumbers[index] = i
#         index += 1
#     return listNumbers

# 08 Показать четные числа от 1 до N

# def showFromOneToN (n):
#     listNumbers = [0] * n
#     index = 0
#     for i in range(1, n + 1):
#         listNumbers[index] = i
#         index += 1
#     return listNumbers

# 09 Показать последнюю цифру трёхзначного числа

# def getLastNumber (n):
#     n = abs(n)
#     return (n % 10)

# 10 Показать вторую цифру трёхзначного числа

# def getSecondNumber (n):
#     n = abs(n)
#     return n // 10 % 10

# 11 Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

# import random
# a = random.randint(10, 99)
# print (a)
# firstNumber = a % 10
# secondNumber = a // 10
# if firstNumber > secondNumber:
#     print (firstNumber)
# else:
#     print (secondNumber)

# 12 Удалить вторую цифру трёхзначного числа

# def cutSecondNumber (n):
#     n = abs(n)
#     lastNumber = n % 10
#     firstNumber = n // 100
#     return firstNumber * 10 + lastNumber

# 13 Выяснить, кратно ли число заданному, если нет, вывести остаток

# firstNumber = int(input())
# secondNumber = int(input())

# def isMultiple (firstNumber, secondNumber):
#     if firstNumber % secondNumber == 0:
#         return 0 #означает кратность
#     else:
#         return firstNumber % secondNumber

# 14 Найти третью цифру числа или сообщить, что её нет

# def getThirdNumber (n):
#     n = abs(n)
#     if n // 100 > 0:
#         while n // 100 > 9:
#             n = n // 10
#         return n % 10
#     else:
#         return -1
#