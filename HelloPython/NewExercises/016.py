# 16 Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

a = 5

def fill_list (n):
    list = []
    for i in range (1, n + 1):
        list.append((1 + 1 / i) ** i)
    return list

list = fill_list(a)
print(list)

def sum_list (list):
    total = 0
    for i in list:
        total += i
    return total

print(sum_list(list))