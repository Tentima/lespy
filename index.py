print('Hello, World!')
print(2025)

# Операторы сравнения 
# > больше 
# < меньше 
# >= больше или равно
# <= меньше или равно
# == равно
# != не равно

# Типы данных в Python 
# int- целые числа (1,2,3,-5,-10)
#float- числа с плавающей точкой (1.5, 2.75, -3.14)
#str- строки (текст) ('Hello', "World")
#Boolean - True=1 и False=0 - булевые значения (логические)

# Переменные это именованные ячейки памяти, которые хранят в себе данные определенного типа 
a = 10 #int
b  =2.5 #float
c = 'Hello'# str
d = True # boolean(истина и ложь)
name= 'Zahid'
age= 19

#type () - функция, которая возвращает тип данных
print(type(45-3.5))
print(type(45-35))
print(type(True))
print(type('Hello'))
print(int(5.5))
print(float(6))
print(int('5'))
print(int(True))
print(45+True)
print(5*'Hello\n')

# Типы данных 
# float - числа с плавающей точкой 3.14, -0.5, 2.0
# str - строки "Hello", 'World', "123"
# bool - булевые значения (True, False)
# list - списки [1, 2, 3], ['a', 'b', 'c']
# tuple - кортежи (1, 2, 3,), ('x', 'y', 'z')
# dict - словари {'key': 'value'}, {'name': 'Zahid', 'age': 19}
# set - множества {1, 2, 3}, {'a', 'b'}
# None- специальный тип данных, обозначающий отсутствие значения

# Ввод и вывод данных
name = input("Введите ваше имя")
age = input("Введите ваше возраст:")
learning = input("Что вы изучаете ? ")
Like = input("ping pong")
print("Привет," + name + "!Тебе "+ age + " лет.")
print("Ты изучаешь " + learning + "и тебе нравится " + like )

# Правила объявления пременных 
# Нельзя начинать название переменной с цифры 
# 5=5 - неправильно
# number_5=5 - правильно 

# В названиях переменных разрешаются только буквы латинского алфавита, цифры и нижний пробел_
# first_name = "Mark" - правильно
# first.name = "Mark" - неправильно 
# _=5 - переменная также может состоять из одного пробела 

#Названия переменных должны четко указывать, что в них хранится или же иметь смысловую связь.
# n="Mark" - непонятно , что хранится в переменной 
# name = "Mark" -правильное название 
# n = 5 - неправильно 
# num = 5 - правильно 
# number = 5 -правилно 
# Используем для отделения слов snake case
# Название пременных не должно совпадать с названием ключевых слов языка Python:
# False awwait else import pass
# None break except in raise 
# True class finally is return 
# and continue for lambda try 
# as def from nonlocal while
# assert del global not with 
# async elif if or yield

# Множественное присвоение 
# Можно также объеденить присваивание нескольких пременных в одну строку
# Например: 
# num1, num2, num3, = 1, 2, 3
# print(num1)
# результат выполнения: 1
# print(num2)
# результат выполнения: 2
# print(num3)
# результат выполнения :3

#name, surname, age ="John", "Doe" 20
#print(name)
# результат выполнения: "John"
#print(surname)
# результат выполнения: "Doe"
#print(age)
# резльтат выполнения: 20

# ASCII table
print('A'>'!')
print('A'<'a')
print('#'>'$')

# множество присваивание 
num1, num2, num3 = 5, 10, 15
# свайп переменных
num1, num2, = num2, num1
print(num1)
print(num2)
print(num3)