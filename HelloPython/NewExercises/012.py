# 12 Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.

n = 10

def dict (n):
    dictionary = {}
    for k in range (1, n + 1):
        dictionary[k] = 3 * k + 1
    return dictionary

diction = dict(n)
print(diction)