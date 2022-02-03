# 35 В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

with open('35.txt') as file:
    A = [int(x) for x in file.read().split()]

print(A)
def finder(A):
    for i in range(1, len(A)):
        if not A[i] - 1 == A[i-1]:
            return A[i] - 1

print(finder(A))