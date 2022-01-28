# 14 Подсчитать сумму цифр в вещественном числе

number = 13.4860451

def sum_numbers(arg): 
    string_num = str(arg)
    total = 0
    for i in string_num:
        if i == '.':
            total += 0
        else:
            total = total + int(i)
print(sum_numbers(number))