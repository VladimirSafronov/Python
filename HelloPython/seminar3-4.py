# 13 Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.

# text = 'qwerqwerqwertjd'
# str = str(input('введите текст:'))

# def counter (str1, str2):
#     t = str1
#     count = 0
#     index = 0
#     while len(t) != 0:
#         index = str1.find(str2, index)
#         if index != -1:
#             count += 1
#             index += len(str2)
#         else:
#             break
#     return count

# print(counter(text, str))

# 14 Подсчитать сумму цифр в вещественном числе

# number = 13.4860451

# def sum_numbers(arg): 
#     string_num = str(arg)
#     total = 0
#     for i in string_num:
#         if i == '.':
#             total += 0
#         else:
#             total = total + int(i)
# print(sum_numbers(number))

# 18 Реализовать алгоритм перемешивания списка

# import random

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# def mix (arr):
#     for i in arr:
#         random_index = random.randint(i, len(arr) - 1)
#         temporary = arr[i]
#         arr[i] = arr[random_index]
#         arr[random_index] = temporary
#     return arr
# print (mix(list))

