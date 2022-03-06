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

# 4.2.12 Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник
a, b, c = int(input()), int(input()), int(input())
if a < (b + c) and b < (a + c) and c < (a + b):
    print('YES')
else:
    print('NO')

# 4.2.13 Напишите программу, которая определяет, является ли год с данным номером високосным
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('YES')
else:
    print('NO')

# 4.2.14 Даны две различные клетки шахматной доски. Напишите программу, которая определяет, 
# может ли ладья попасть с первой клетки на вторую одним ходом
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a == c) or (b == d):
    print('YES')
else:
    print('NO')

# 4.2.15 Напишите программу,  которая определяет, может ли король попасть с первой клетки на вторую одним ходом
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if ((a - 1) <= c <= (a + 1)) and ((b - 1) <= d <= (b + 1)):
    print('YES')
else:
    print('NO')

# 4.3.3 Если Зум быстрее Флэша нужно вывести «NO», если Флэш быстрее Зума нужно вывести «YES», 
# если их скорости равны нужно вывести "Don't know"
a, b = int(input()), int(input())
if a > b:
    print('NO')
elif a == b:
    print("Don't know")
else:
    print('YES')

# 4.3.4 Напишите программу, которая принимает три положительных числа и определяет вид треугольника
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif (a == b != c) or (a == c != b) or (c == b != a):
    print('Равнобедренный')
else:
    print('Разносторонний')

# 4.3.5 Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.
a, b, c = int(input()), int(input()), int(input())
if a > b:
    if a < c:
        print(a)
    else:
        if c > b:
            print(c)
        else:
            print(b)
else:
    if a > c:
        print(a)
    else:
        if c > b:
            print(b)
        else:
            print(c)

# 4.3.6 Напишите программу, которая выводит на экран количество дней в этом месяце
month = int(input())
if month == 2:
    print(28)
elif month in (4, 6, 9, 11):
    print(30)
else:
    print(31)

# 4.3.7 Напишите программу, определяющую, в какой категории будет выступать данный боксер.
weight = int(input())
if weight < 60:
    print('Легкий вес')
elif 59 < weight < 64:
    print('Первый полусредний вес')
elif 63 < weight < 69:
    print('Полусредний вес')

# 4.3.8 Напишите программу, которая считывает с клавиатуры два целых числа и строку. 
# Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /), 
# то выведите результат применения этой операции к введённым ранее числам, в противном случае выведите «Неверная операция». 
# Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».
a, b = int(input()), int(input())
sign = input()
try:
    if sign in ('+', '-', '*', '/'):
        if sign == '+':
            print(a + b)
        elif sign == '-':
            print(a - b)
        elif sign == '*':
            print(a * b)
        else:
            print(a / b)
    else:
        print('Неверная операция')
except ZeroDivisionError:
    print("На ноль делить нельзя!")    

# 4.3.9 Напишите программу, которая считывает названия двух основных цветов для смешивания. 
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», 
# то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести название вторичного цвета, 
# который получится в результате.
first_color, second_color = input(), input()
if first_color in ('красный', 'синий', 'желтый') and second_color in ('красный', 'синий', 'желтый'):
    if first_color == second_color:
        print(first_color)
    elif first_color in ('красный', 'синий') and second_color in ('красный', 'синий'):
        print('фиолетовый')
    elif first_color in ('красный', 'желтый') and second_color in ('красный', 'желтый'):
        print('оранжевый')
    else:
        print('зеленый')
else:
    print('ошибка цвета')

# 4.3.10 Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным. 
# Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.
a = int(input())
if 0 <= a <= 36:
    if a == 0:
        print('зеленый')
    elif (1 <= a <= 10) or (19 <= a <= 28):
        if a % 2 == 0:
            print('черный')
        else:
            print('красный')
    elif (11 <= a <= 18) or (29 <= a <= 36):
        if a % 2 == 0:
            print('красный')
        else:
            print('черный')
else:
    print('ошибка ввода')

# 4.3.11 На числовой прямой даны два отрезка. Напишите программу, которая находит их пересечение.
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a2 > b1 or b2 < a1:
    print('пустое множество')
elif a2 == b1:
    print(a2)
elif a1 >= a2:
    if b1 > b2:
        if a1 == b2:
            print(a1)
        else:
            print(a1, b2)
    else:
        if a1 == b1:
            print(a1)
        else:
            print(a1, b1)
elif a1 < a2:
    if b1 > b2:
        if a2 == b2:
            print(a2)
        else:
            print(a2, b2)
    else:
        if a2 == b1:
            print(a2)
        else:
            print(a2, b1)

# 6.1.3 Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
a, b = float(input()), float(input())
area = (1 / 2) * a * b
print(area)

# 6.1.4 Две старушки идут навстречу друг другу с постоянными скоростями. Определите, через какое время старушки встретятся.
s, v1, v2 = float(input()), float(input()), float(input())
time = s / (v1 + v2)
print(time)

# 6.1.5 Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
x = float(input())
if x:
    print(1 / x)
else:
    print('Обратного числа не существует')

# 6.1.6 Напишите программу, которая определяет, какой температуре по шкале Цельсия 
# соответствует указанное значение по шкале Фаренгейта.
print(5 / 9 * (float(input()) - 32))

# 6.1.7 Напишите программу, которая вычисляет возраст собаки в человеческих годах.
age_dog = int(input())
if age_dog > 2:
    print(21 + (age_dog - 2) * 4)
else:
    print(age_dog * 10.5)

# 6.1.8 Дано положительное действительное число. Выведите его первую цифру после десятичной точки.
print(int((float(input()) * 10) % 10))

# 6.1.9 Дано положительное действительное число. Выведите его дробную часть.
x = float(input())
print(x - int(x))

# 6.1.12 Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.
a = [int(input()) for _ in range(5)]
print('Наименьшее число =', min(a))
print('Наибольшее число =', max(a))

# 6.1.13 Напишите программу, которая упорядочивает три числа от большего к меньшему.
a = [int(input()) for _ in range(3)]
rev_a = sorted(a, reverse=True)
for i in rev_a:
    print(i)

# 6.1.14 Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре.
x = int(input())
a = x % 10
b = x // 10 % 10
c = x // 100
if a + b + c == 2 * max(a, b, c):
    print('Число интересное')
else:
    print('Число неинтересное')

# 6.1.15 Даны пять чисел. Напишите программу, которая вычисляет сумму их модулей.
print(sum([abs(float(input())) for _ in range(5)]))

# 6.1.16 Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.
coordinates = [int(input()) for _ in range(4)]
print(abs(coordinates[0] - coordinates[2]) + abs(coordinates[1] - coordinates[3]))

# 6.2.2 Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
from math import sqrt
x1, y1, x2, y2 = [float(input()) for _ in range(4)]
print(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

# 6.2.3 Напишите программу определяющую площадь круга и длину окружности по заданному радиусу
from math import pi
rad = float(input())
print(pi * rad ** 2)
print(2 * pi * rad)

# 6.2.4 Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.
from math import sqrt
a, b = [float(input()) for _ in range(2)]
print((a + b) / 2)
print(sqrt(a * b))
print((2 * a * b) / (a + b))
print(sqrt((a ** 2 + b ** 2) / 2))

# 6.2.5 Напишите программу, вычисляющую значение тригонометрического выражения sin(x) + cos(x) + tan^2(x)
# по заданному числу градусов x.
from math import sin, cos, tan, radians
x = radians(float(input()))
print(sin(x) + cos(x) + pow(tan(x), 2))

# 6.2.6 Программа должна вывести одно число – значение указанного выражения. |_x_| + -|x|-
from math import floor, ceil
x = float(input())
print(floor(x) + ceil(x))

# 6.2.7 Напишите программу, которая находит вещественные корни квадратного уравнения.
from math import sqrt
a, b, c = [float(input()) for _ in range(3)]
dis = b ** 2 - 4 * a * c
x1, x2 = 0, 0
if dis > 0:
    x1 = (- b + sqrt(dis)) / (2 * a)
    x2 = (- b - sqrt(dis)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif dis == 0:
    print((-b) / (2 * a))
else:
    print('Нет корней')

# 6.2.8 Напишите программу, которая находит площадь указанного правильного многоугольника.
from math import pi, tan
n, a = int(input()), float(input())
print((n * pow(a, 2)) / (4 * tan(pi / n)))

# 6.3.5 Напишите программу, которая выводит текст.
print('"Python is a great language!", said Fred. "I don\'t ever remember having this much fun before."')

# 6.3.6 Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу.
print(f'Hello {input()} {input()}! You just delved into Python')

# 6.3.7 Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу.
print(f'Футбольная команда {(team := input())} имеет длину {len(team)} символов')

# 6.3.8 Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
print(*sorted([input() for _ in range(3)], key=len)[::2], sep='\n')