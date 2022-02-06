# 31 Составить список простых множителей натурального числа N

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

print(simple_multiplier(75))