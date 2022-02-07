# 38 Напишите программу, удаляющую из текста все слова содержащие "абв"

text = 'аптека абв улица преабвгд фонарь'
list_text = text.split()
symb = 'абв'

def cut_symb(li, symb):
    res = []
    for i in range(len(li)):
        if not symb in li[i]:
            res.append(li[i])
    return res

list_new_text = cut_symb(list_text, symb)
print(list_new_text)

new_text = ' '.join(list_new_text)
print(new_text)