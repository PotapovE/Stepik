# 2.1.2 На вход программе подаются два целых числа a и b.
a, b = int(input()), int(input())
print(a + b, a - b, a * b, a / b, a // b, a % b, (a ** 10 + b ** 10) ** 0.5, sep='\n')

# 2.1.3 Индекс массы тела
weight, growth = float(input()), float(input())
bmi = weight / (growth ** 2)
if bmi < 18.5:
    print('Недостаточная масса')
elif bmi > 25:
    print('Избыточная масса')
else:
    print('Оптимальная масса')