# 23 Показать таблицу квадратов чисел от 1 до N

# def func (n):
#     list = []
#     for i in range(1, n + 1):
#         list.append(i ** 2)
#     return list

# 24 Найти кубы чисел от 1 до N

# def get_cube_to_n (n):
#     list = []
#     for i in range(1, n + 1):
#         list.append(i ** 3)
#     return list

# 25 Найти сумму чисел от 1 до А

# def sum_numbers (a):
#     total = 1
#     for i in range(2, a + 1):
#         total = total + i
#     return total

# 26 Возведите число А в натуральную степень B используя цикл

# def degree (a, b):
#     answer = a
#     for i in range(1, b):
#         answer *= a
#     return answer
# print(degree(5, 3))

# 27 Определить количество цифр в числе

# import math
# def func (a):
#     a = abs(a)
#     count = 1
#     while a // 10 != 0:
#         a //= 10
#         count += 1
#     return count

# 28 Подсчитать сумму цифр в числе

# import math
# def func (a):
#     a = abs(a)
#     total = 0
#     while a > 0:
#         total = total + a % 10
#         a //= 10
#     return total

# 29 Написать программу вычисления произведения чисел от 1 до N

# def multiplication_num (n):
#     answer = 1
#     for i in range (1, n + 1):
#         answer *= i
#     return answer

# 30 Показать кубы чисел, заканчивающихся на четную цифру

# def cube (n, m):
#     list = []
#     if n % 2 == 1:
#         n +=1
#     for i in range(n, m + 1, 2):
#         list.append(i ** 3)
#     return list
