# 36 Дан список чисел. Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

import random


list_numbers = [random.randint(1,10) for i in range(10)]
print(list_numbers)

def higher(li):
    max = li[0]
    new_list = [max]
    for i in li:
        if i > max:
            new_list.append(i)
            max = i
    return new_list

higher_list = higher(list_numbers)
print(higher_list)

