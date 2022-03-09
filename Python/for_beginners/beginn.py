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

# 6.3.9 Вводятся 3 строки в случайном порядке. 
# Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
words_len = sorted([len(input()) for _ in range(3)])
print('YES' if words_len[1] - words_len[0] == words_len[2] - words_len[1] else 'NO')

# 6.3.12 Напишите программу, которая считывает одну строку, 
# после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.
print('YES' if "синий" in input() else 'NO')

# 6.3.13 Напишите программу, которая считывает одну строку, 
# после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.
text = input()
print('YES' if ("суббота" in text) or ("воскресенье" in text) else 'NO')

# 6.3.14 Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. 
# Напишите программу проверяющую корректность email адреса.
text = input()
print('YES' if '@' in text and '.' in text else 'NO')

# 7.1.2 Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.
for _ in range(10):
    print('Python is awesome!')

# 7.1.3 Дано предложение и количество раз которое его надо повторить. 
# Напишите программу, которая повторяет данное предложение нужное количество раз.
text, count = input(), int(input())
for _ in range(count):
    print(text)

# 7.1.4 Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов.
for _ in range(6):
    print('AAA')
for _ in range(5):
    print('BBBB')
print('E')
for _ in range(9):
    print('TTTTT')
print('G')

# 7.1.5 На вход программе подается натуральное число n. Напишите программу, которая печатает звездный прямоугольник размерами n * 19
for _ in range(int(input())):
    print('*' * 19)

# 7.1.7 Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9, 
# каждая с указанной строкой текста.
text = input()
for i in range(10):
    print(i, text)

# 7.1.8 На вход программе подается натуральное число n. Напишите программу, которая для каждого из чисел от 0 до n (включительно)
# выводит фразу: «Квадрат числа [число] равен [число]».
n = int(input())
for i in range(n + 1):
    sq_num = pow(i, 2)
    print(f'Квадрат числа {i} равен {sq_num}')

# 7.1.9 На вход программе подается натуральное число n. 
# Напишите программу, которая выводит звездный треугольник в соответствии с примером.
n = int(input())
for i in range(n, 0, -1):
    print('*' * i)

# 7.1.10 Напишите программу, которая предсказывает размер популяции организмов.
m, p, n = [int(input()) for _ in range(3)]
for i in range(n):
    print(i + 1, m)
    m += (m / 100 * p)

# 7.2.7 Даны два целых числа m, n. m <= n. Напишите программу, которая выводит все числа [m, n].
m, n = [int(input()) for _ in range(2)]
for i in range(m, n + 1):
    print(i)

# 7.2.8 Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно 
# в порядке возрастания, если m < n, или в порядке убывания в противном случае.
m, n = [int(input()) for _ in range(2)]
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)

# 7.2.9 Даны два целых числа m и nn(m > n). Напишите программу, которая выводит все нечетные числа от m до n включительно 
# в порядке убывания.
m, n = [int(input()) for _ in range(2)]
if m % 2 == 0:
    m -= 1
for i in range(m, n - 1, -2):
    print(i)

# 7.2.10 Даны два натуральных числа m и n (m ≤ n). Напишите программу, которая выводит все числа от m до n включительно 
# удовлетворяющие хотя бы одному из условий: число кратно 17; число оканчивается на 9; число кратно 3 и 5 одновременно.
m, n = [int(input()) for _ in range(2)]
for i in range(m, n + 1):
    if (i % 17 == 0) or (i % 10 == 9) or (i % 15 == 0):
        print(i)

# 7.2.11 Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n.
n = int(input())
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')

# 7.3.5 На вход программе подаются два целых числа a и b (a≤b). 
# Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно, 
# куб которых оканчивается на 44 или 99.
counter = 0
a, b = [int(input()) for _ in range(2)]
for i in range(a, b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        counter += 1
print(counter)

# 7.3.6 На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке. 
# Напишите программу, которая подсчитывает сумму введенных чисел. 
total = 0
for _ in range(int(input())):
    total += int(input())
print(total)

# 7.3.7. На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения
# Асимптотическое приближение
from math import log
n = int(input())
total = 0
for i in range(1, n + 1):
    total += 1 / i
print(total - log(n))

# 7.3.8 На вход программе подается натуральное число n. Напишите программу, 
# которая подсчитывает сумму тех чисел от 11 до n (включительно) квадрат которых оканчивается на 2, 5 или 8.
n = int(input())
total = 0
for i in range(1, n + 1):
    if i * i % 10 == 5:
        total += i
print(total)

# 7.3.9 На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.
n = int(input())
total = 1
for i in range(1, n + 1):
    total *= i
print(total)

# 7.3.10 Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
total = 1
for _ in range(10): 
    num = int(input())
    if num: 
        total *= num
print(total)

# 7.3.11 На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.
n = int(input())
print(sum([i for i in range(1, n + 1) if n % i == 0]))

# 7.3.12 На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы.
n = int(input())
print(sum([- i if i % 2 == 0 else i for i in range(1, n + 1)]))

# 7.3.13 На вход программе подается натуральное число n, а затем nn различных натуральных чисел, каждое на отдельной строке. 
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
largest1, largest2 = 0, 0
for i in range(int(input())):
    num = int(input())
    if num > largest1:
        largest2 = largest1
        largest1 = num
    if num > largest2 and num < largest1:
        largest2 = num
print(largest1, largest2, sep='\n')
# or
large = sorted([int(input()) for _ in range(int(input()))])
print(large[-1], large[-2], sep='\n')

# 7.3.14 Напишите программу, которая считывает последовательность из 10 целых чисел и определяет 
# является ли каждое из них четным или нет.
flag = True
numbers = [int(input()) for _ in range(10)]
for i in numbers:
    if i % 2 != 0:
        flag = False
print('YES' if flag else 'NO')

# 7.3.15 Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.
x1, x2 = 1, 1
for _ in range(int(input())):
    print(x1, end=' ')
    x1, x2 = x2, x1 + x2

# 7.4.8 На вход программе подается последовательность слов, каждое слово на отдельной строке. 
# Концом последовательности является слово «КОНЕЦ» (без кавычек). Напишите программу, 
# которая выводит члены данной последовательности.
text = input()
while text != 'КОНЕЦ':
    print(text)
    text = input()

# 7.4.9. На вход программе подается последовательность слов, каждое слово на отдельной строке. 
# Концом последовательности является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек). 
# Напишите программу, которая выводит члены данной последовательности.
text = input()
while text not in ('КОНЕЦ', 'конец'):
    print(text)
    text = input()

# 7.4.10 На вход программе подается последовательность слов, каждое слово на отдельной строке. 
# Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). 
# Напишите программу, которая выводит общее количество членов данной последовательности.
counter = 0
while input() not in ('стоп', 'хватит', 'достаточно'):
    counter += 1
print(counter)

# 7.4.11 На вход программе подается последовательность целых чисел делящихся на 77, каждое число на отдельной строке. 
# Концом последовательности является любое число не делящееся на 77. Напишите программу, 
# которая выводит члены данной последовательности.
n = int(input())
while n % 7 == 0:
    print(n)
    n = int(input())