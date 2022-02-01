import time
import math

def find_max(arg):  # определяем максимальное число для нахождения делителя (кол-ва нулей)
    a = abs(arg[0])
    b = abs(arg[1])
    if a > b:
        return a
    else:
        return b

def find_denominator(arg):
    count = 0
    if arg >= 0 and arg < 10:
        count = 1
    while arg // 10 > 0:
        count += 1
        arg /= 10
    return count

def is_number_negative(): # метод определяющий полярность числа
    num = int(round(time.time() * 10000))
    num = num % 10000
    arg = []
    while num > 0:
        arg.append(num % 10)
        num //= 10
    if arg[-1] < 5: # если четвертая цифра с конца меньше 5, то минус
        return True
    else:
        return False

def get_random_number(intrval, denominator):
    number = int(round(time.time() * 10000))
    number = number % denominator
    if is_number_negative():
        number *= -1
    if number >= interval[0] and number <= interval[1]:
        return number
    else:
        get_random_number(interval, denominator)

interval = (-5, 11) # ищем число в заданном интервале
max_number = find_max(interval)
denominator = 10 ** find_denominator(max_number)
print(denominator)
randon_num = get_random_number(interval, denominator)
print(randon_num)