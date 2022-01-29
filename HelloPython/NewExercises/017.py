# 17 Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

from fileinput import close
import random
n = 10
def fill_list (n):
    list = []
    for i in range (0, n):
        list.append(random.randint(-n, n))
    return list
list = fill_list(n)
print(list)

def get_index ():
    data = open('file.txt', 'r')
    numbers = []
    for i in data:
        numbers.append(int(i))
    data.close()
    return numbers

mult_index = get_index()
print(mult_index)

