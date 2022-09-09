import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def sqrt(x):
    return math.sqrt(x)


print("")
print("|------------------|")
print("|  Сложить [+]     |")
print("|  Вычесть [-]     |")
print("|  Умножить [*]    |")
print("|  Разделить [/]   |")
print("|  Кв. корень [√]  |")
print("|------------------|")
print("")

while True:
    choice = input("Выберите действие [+], [-], [*], [/], [√] --> ")

    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

    if choice in ('√'):
        num3 = float(input("Введите корень: "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '√':
            print("√", num3, "=", sqrt(num3))

        print('')
        next_calculation = input("Сделать еще вычисления? (yes/no): ")
        print('')

        if next_calculation == ('yes'):
            continue

        if next_calculation == ('no'):
            break

    else:
        print('')
        print("Неверный ввод")