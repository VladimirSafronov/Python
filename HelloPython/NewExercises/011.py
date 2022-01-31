# 11 Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.

n = 10

def mult3(n):
    arr = [1]
    for i in range (2, n + 1):
        arr.append(-3 * arr[-1])
    return arr

list = mult3(n)
print(list)