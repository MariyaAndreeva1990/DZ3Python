"""
Задача 16: Требуется вычислить, сколько раз 
встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. 
Последняя строка содержит число X
n = 5
1 2 3 4 5
x = 3
-> 1
"""

n = int(input("Введите количество элементов массива: "))
from random import randint
A = [randint(1,6)for i in range(n)]
print(A)
count = 0
x = int(input("Введите искомое число от 1 до 5: "))
for i in A:
        count += 1
print (f'В массиве {A} искомый элемент {x} встречается {count} раз(а)')