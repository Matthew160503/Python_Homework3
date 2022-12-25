# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
N = int(input('введите желаемую длину списка: '))
our_script = []
for i in range(0,N):
    our_script.append(float(input("введите числа для записи в список: ")))

def difference_list(list):
    temp = []
    for i in our_script:
        temp.append(round((i % 1), 5))
    print('Список из дробных частей равен ', temp)
    min = temp[0]
    max = temp[0]
    for j in temp:
        if min > j:
            min = j
        elif max < j:
            max = j
    difference = max - min
    return difference

print('Разность между максимумом и минимумом = ',difference_list(our_script))

