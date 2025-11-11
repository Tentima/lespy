# Функции - это кусочек кода который мы можем написать один раз, и использовать множество раз 
# она помогает:
# 1) не повторять один и тот же код
# 2) делает программу аккуратнее т понятнее
# 3) Удобно передавать данные внутрь и получать результат

# функция бывают двух видов:
    # 1) встроенные функции print(), input(), type(), len()
# list(), dict(), и т.п.
    #   2) пользовательские функции, те функции что мы пишем сами через def, они бывают с аргументами и без аргументов
# def -исп только тогда когда мы создаем функцию

# функция без аргументов
def HelloPrint():
    return 'Hello world'

print(HelloPrint())
# функция с аргументами
def HelloPrint(name):
    return f'Hello world {name}'

print(HelloPrint("Bilal"))

# Создайте калькулятор используя функцию, цикл, условие и ввод и вывод данных
def calc(num1, simbol, num2):
    while True:
        if simbol =='+':
            return num1+num2
        elif simbol == '-':
            return num1-num2
        elif simbol =='*':
            return num1*num2
        elif simbol =='/':
            return num1/num2
        elif simbol =='**':
            return num1**num2
        elif simbol =='//':
            return num1//num2
        elif simbol =='%':
            return num1%num2
        else:
            print("пишите только символы")
        
a = int(input("Первое:"))
c = input("Символ")
b = int(input("Второе:"))
print(calc(a,c,b))