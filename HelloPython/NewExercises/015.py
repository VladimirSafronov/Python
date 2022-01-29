# 15 Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

n = 10

def miltiplicate_next_index (n):
    list = [1]
    for i in range (2, n + 1):
        list.append(i * list[-1])
    return list

list = miltiplicate_next_index (n)
print(list)
