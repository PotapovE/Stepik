# 2.1.2 На вход программе подаются два целых числа a и b.
a, b = int(input()), int(input())
print(a + b, a - b, a * b, a / b, a // b, a % b, (a ** 10 + b ** 10) ** 0.5, sep='\n')