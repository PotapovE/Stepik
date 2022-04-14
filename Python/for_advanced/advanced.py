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

# 2.1.4 Стоимость строки
price = len(input()) * 60
print(f'{price // 100} р. {price % 100} коп.')

# 2.1.5 Количество слов
print(len(input().split()))

# 2.1.6 Зодиак
animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
print(animals[int(input()) % 12])