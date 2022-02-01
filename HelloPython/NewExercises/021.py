# 21 Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.
list = ['q', 'w', 'e', 'r', 'w']
str = 'z'

def find_second_input(list, str):
    count = 0
    i = 0
    while i < len(list):
        if str == list[i]:
            count += 1
        if count == 2:
            return i
        i += 1
    return -1

print(find_second_input(list, str))