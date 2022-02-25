# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
a, b, c = int(input()), int(input()), int(input())
sum_value = 0
if a > 0:
    sum_value += a
if b > 0:
    sum_value += b
if c > 0:
    sum_value += c
print(sum_value)