"""
Задача 18: Требуется найти в массиве A[1..N] 
самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – 
количество элементов в массиве. В последующих строках записаны 
N целых чисел Ai. Последняя строка содержит число X
n = 5
1 2 3 4 5
x = 6
-> 5
"""
n = int(input("Введите количество элементов массива: "))
from random import randint
A = [randint(1,6)for i in range(n)]
print(A)
x = int(input("Введите число, к которому будем искать близкий по значению элемент в массиве: "))
B = list()
for i in A:
    B.append(i-x)
for i in range(len(B)):
    if B[i] < 0:
        B[i] = B[i]*(-1)
print(f'При числе элементов n = {n}, последовательность представляет собой {A}. Близким по значению к числу {x} в последовательности является число {A[B.index(min(B))]}.')