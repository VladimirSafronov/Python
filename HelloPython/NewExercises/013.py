# 13 Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.

text = 'qwerqwerqwertjd'
str = str(input('введите текст:'))

def counter (str1, str2):
    t = str1
    count = 0
    index = 0
    while len(t) != 0:
        index = str1.find(str2, index)
        if index != -1:
            count += 1
            index += len(str2)
        else:
            break
    return count

print(counter(text, str))