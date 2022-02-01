# 25 Написать программу преобразования десятичного числа в двоичное

def to_binary(arg):
    binary_num = ''
    if arg == 0:
        return '0'
    while arg != 0:
        binary_num = str(arg % 2) + binary_num
        arg //= 2
    return binary_num

print(to_binary(16))