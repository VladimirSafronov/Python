# 24 В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]

def find_max_fraction(list):
    max = 0.01
    for i in list:
        if round(i % 1, 2) > max:
            max = round(i % 1, 2)
    return max

def find_min_fraction(list):
    min = 0.99
    for i in list:
        if round(i % 1, 2) != 0.00 and round(i % 1, 2) < min:
            min = round(i % 1, 2)
    return min

print(find_max_fraction(list) - find_min_fraction(list))