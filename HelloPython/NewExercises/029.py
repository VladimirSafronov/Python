# 29 Найти НОК двух чисел

a = 285
b = 331

def simple_multiplier(arg):
    li = []
    count = 2
    while arg > 1:
        if arg % count == 0:
            li.append(count)
            arg /= count
        else :
            count += 1
    return li

li_a = simple_multiplier(a)
li_b = simple_multiplier(b)

print(li_a)
print(li_b)

def get_greatest_common_mult(list_a, list_b):
    for i in range(0, len(list_a)):
        for j in range(0, len(list_b)):
            if list_a[i] == list_b[j]:
                list_b[j] = 1
    return list_a + list_b


li = get_greatest_common_mult(li_a, li_b)
print(li)

def func(li):
    ans = 1
    for i in li:
        ans *= i
    return ans

result = func(li)
print(result)