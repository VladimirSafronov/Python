# 26 Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

k = 8

def fibonacci(n):
	if n in [1, 2]:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

fi = [fibonacci(i) for i in range(1, k+1)]

def negofib(n, li):
    res_list = []
    last_ind = -1
    while n != 0:
        if n % 2 == 0:
            res_list.append(li[last_ind] * -1)
        else:
            res_list.append(li[last_ind])
        last_ind -= 1
        n -= 1
    res_list.append(0)
    return res_list + li

result = negofib(k, fi)
print(result)