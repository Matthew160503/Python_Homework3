# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

def fib(num):
    if num in [1,2]:
        return 1
    else:
        return fib(num-1) + fib(num-2)

N = int(input("Введите размерность списка: "))
list = [0,]
for e in range(1,N+1):
    list.append(fib(e))

reversed_list = []
reversed_list.extend(list)
reversed_list.reverse()

if len(reversed_list) % 2 == 0:
    for i in range(N, -1, -1):
        if i % 2 == 1:
            reversed_list[i] = - reversed_list[i]
else:
    for i in range(N, -1, -1):
        if i % 2 == 0:
            reversed_list[i] = - reversed_list[i]

for i in range (1, N+1):
    reversed_list.append(list[i])
print(reversed_list)
