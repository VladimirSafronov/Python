# 20 Определить, присутствует ли в заданном списке строк, некоторое число 
import string


list = ['a', 'b', 'c', '3']
number = 3

def find_number_in_list(list, number):
    num_in_str = str(number)
    count = 0
    for i in list:
        if num_in_str == list[count]:
            return True
        else:
            count += 1
    return False

print(find_number_in_list(list, number))