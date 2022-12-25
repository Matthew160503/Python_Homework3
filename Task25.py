# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
num = int(input('Введите число: ')) 
res = '' 
temp = 0
while num > 0:
    temp = num % 2
    res = str(temp) + res
    num = num // 2
 
print('Число в двоичной системе: ', res)