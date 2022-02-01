# print ('Hello world!')
# value = None
# print (type(value))
# a = 123
# b = 1.23
# print (type(a))
# print (type(b))
# value = 13345
# s = "War \"And Peace"
# print (s) # output string
# print (a,'-',b,'-',s)
# print ('{1} - {2} - {0}'.format(a,b,s))
# print (f'{a} - {b} - {s}')
# f = True
# print (f)
# list = ['1', '2', '3', 'hello']
# col = [1, 2, 4.5, 'world'] # тоже работает, но так делать не надо
# print (list)
# print (col)
# print ('введите а')
# a = float(input())
# print ('введите b')
# b = float(input())
# print (a, '+' , b, '=' ,a + b)
# a = 12
# b = 8
# c = a // b # деление без остатка (/ выдаст дробное число)
# print (c)
# a = 12
# b = 8
# c = a ** b # возведение в степень
# print (c)
# a = 1.34564
# b = 3
# c = round(a * b, 5) # округление числа последняя цифра означает кол-во символов после точки
# print (c)

# логические операции
# not, and, or не путать с ^, &, |
# a = 1 < 2 < 5
# print (a) 
# from turtle import color


# f = [1, 2, 3, 4]
# print (2 in f) # получим истину
# is_odd = not f[0] % 2
# print (is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if (a > b):
#     print(a)
# else:
#     print(b)

# username = input('введите имя: ')
# if (username == 'Маша'):
#     print('Ура, это же Маша!')
# elif (username == 'Марина'):
#     print('Давно не заходила Марина')
# else:
#     print('Привет', username)

# original = 235
# inverted = 0
# while (original != 0):
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Хватит \nна сегодня')
# print(inverted)

# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i ** 2)

# r = range(1, 10, 2)
# for i in r:
#     print(i)

# r = 'qwerty'
# for i in r:
#     print(i)

# text = 'съешь еще этих мягких французских булок'
# help(int)
# print(len(text)) # длинна строки
# print('еще' in text) 
# print(text.isdigit())
# print(text.islower())
# print(text.replace('еще','ЕщЕ'))
# print(text[0])
# print(text[1])
# print(text[-5])
# print(text[:6])
# print(text[0])

# numbers = [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers)
# print(f'{len(numbers)} len')

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e * 2)
# colors.append('grey')
# print(colors)
# del colors[0]
# print(colors)

# def f(x):
#     if x == 1:
#         return 'целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# arg = 2.3
# print(f(arg))
# print(type(f(arg)))

#