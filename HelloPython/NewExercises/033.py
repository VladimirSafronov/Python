# 33 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = 1
coefficients = k + 1
li = [random.randint(0, 100) for x in range (coefficients)]
print(li)


def get_string(li, k, coef):
    result = ''
    for m in range (coef):
        if k == 1: 
            result += f'{li[m]}x + '
        elif k == 0: 
            result += f'{li[m]} = 0'
        else:
            result += f'{li[m]}x^{k} + '
        k -= 1
    return result

result = get_string(li, k, coefficients)

print(result)

with open ("33.txt", 'a') as file:
    file.write(f'{result}\n')