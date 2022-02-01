# 23 Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

list = [1, 3, 6, 4, 8, 2, 9]

def mult_pairs(list):
    mult_list = []
    front = 0
    behind = len(list) - 1
    while front <= len(list) // 2:
        mult_list.append(list[front] * list[behind])
        front += 1
        behind -= 1
    return mult_list

print(mult_pairs(list))