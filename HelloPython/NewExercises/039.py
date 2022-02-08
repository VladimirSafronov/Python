# 39 Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

import random
import time


sweets = random.randint(100, 200)

# def game(total):
#     max_steps = total
#     for i in range(1, max_steps):
#         if i % 2 != 0:
#             print('Игрок 1 возьми конфеты')
#         else:
#             print('Игрок 2 возьми конфеты')    
#         step = int(input())
#         if step > 30:
#             print('Не жадничай!')
#             total = total - (random.randint(1, 2))
#             i += 1
#         else:
#             total -= step
#             print(f'Осталось {total} конфет')
#             if total <= 0:
#                 print('Ты победил')
#                 break

# game(sweets)

# def game_with_bot(total):
#     max_steps = total
#     for i in range(1, max_steps):
#         if i % 2 != 0:
#             print('Человек возьми конфеты')
#             step = int(input())
#         else:
#             print('Железная голова возьми конфеты')
#             time.sleep(3)    
#             step = random.randint(1, 30)
#         if step > 30:
#             print('Не жадничай!')
#             total = total - (random.randint(1, 2))
#             i += 1
#         else:
#             total -= step
#             print(f'Осталось {total} конфет')
#             if total <= 0:
#                 print('Ты победил')
#                 break

# game_with_bot(sweets)

def game_with_god(total):
    max_steps = total
    for i in range(1, max_steps):
        if i % 2 != 0:
            print('Человек возьми конфеты')
            step = int(input())
        else:
            print('Железная голова возьми конфеты')
            time.sleep(3)    
            step = total % 31
        if step > 30:
            print('Не жадничай!')
            total = total - (random.randint(1, 2))
            i += 1
        else:
            total -= step
            print(f'Осталось {total} конфет')
            if total <= 0:
                print('Ты победил')
                break

game_with_god(sweets)