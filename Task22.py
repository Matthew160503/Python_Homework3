# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

our_list = [2, 34, 45, 23, 12, 2, 1, 54]

def func(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum

print('Сумма элементов на нечетных позициях равна ',func(our_list))