# 27 Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

str_numbers = '10 3 5 8 -99 43'

def min_max(str):
    data = list(map(int, str.split()))
    return (min(data), max(data))
print(min_max(str_numbers))

