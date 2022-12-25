# Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
N = int(input('введите желаемую длину списка: '))
our_list = []
for i in range(0,N):
    our_list.append(int(input("введите числа для записи в список: ")))

def func(list):
    reverse_list = []
    res = []
    reverse_list.extend(list)
    reverse_list.reverse()
    if (len(list) % 2 == 0):
        for i in range(0,int(len(list)/2)):
            res.append(reverse_list[i]*list[i])
    else: 
        for i in range(0,int(len(list)/2)+1):
            res.append(reverse_list[i]*list[i])
    return res

print('Произведение пар числе списка: ', func(our_list))