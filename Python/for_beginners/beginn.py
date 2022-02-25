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

# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанному промежутку (-1, 17).
x = int(input())
if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанным промежуткам до -3, от 7.
x = int(input())
if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанным промежуткам. (-30, 2] & (7, 25]
x = int(input())
if -30 < x <= 2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

# Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17
x = int(input())
if (999 < x < 10000) and (x % 7 == 0 or x % 17 == 0):
    print('YES')
else:
    print('NO')