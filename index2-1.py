name = 'Zahid'
prof = 'student'
age = 19
# конкатенация строк (сложение строк) с помощью +
bio = 'I am '+name+','+str(age)+' years, I am a '+prof
print(bio)
# форматирование строк с помощью f-строк
bio2 = f'I am {name}, {age} years, I am a {prof}'
print(bio2)
# форматирование строк с помощью метода format
bio3 = 'I am {0}, {1} years, I am a {2}'.format(name, age, prof)
print(bio3)

# индексы это порядкоый номер символа в строке
# индексы начинаются с 0
name = 'Zahid Haldarov'
print(name[7],name[8],name[9],name[10],name[11],name[12],name[13])

# срезы строк (substring) [start:stop:step]
print(name[0:6]) # с 0 индекса по 6 не включая
print(name[7:17]) # с 7 по 17 не включая 
print(name[0:14:2]) # шаг 2
print(name[:6]) # с начала по 6 не включая
print(name[::-1]) # реверс строки

age = input('Введите ваш возраст: ')
age = int(age)
if age >0 and age < 16:
    print('пока рано')
elif age >= 16 and age <= 18:
    print('готовься к службе')
elif age >= 18 and age <= 45:
    print('идем служить')
elif age > 45 and age <= 60:
    print('пора на пенсию')
elif age > 60 and age <= 100:
    print('отдыхай')
else:
    print('ошибка введите возраст корректно')
    

# Создать программу для вычисления четных и нечетных чисел
# человек будет вводить число и будем говорить четная она или нет 
number = int(input("введите число:"))
if number % 2 == 0: # проверяем на остаток 
    print("четное число", number)
elif number % 2 != 0:
    print('нечетное число', number)

name = 'Алиса, Бека, Гена, Арслан, Арген, Артем'
print(name[7], name[8], name[9], name[10])
print(name[7:11]) # срезы [start:stop:step]
print(type(name))
name = name.upper() # преобразует в верхний регистр
print(name)
print(name.find("ГЕНА"))
print(name.replace("A", "O"))


# LIST - списки -изменяемый тип данных, который может хранить разные типы данных в себе 
na = [354, 435.56,'Aibek', True, ['hello'], 45]
print(type(na))
print(na[2])
print(na[2][0:3])
na.append('Elnura') #добавляет объект в конец списка
na.insert(3, 'Gena') #добавляет объект в тот индекс который указан
na.remove(True) #удаляет по объекту 
na.pop(1) # удаляет по индексу
print(na)

# Задача: телефонная книжка, у нас список имен, мы должны заполнить его именами наших контактов, то есть у нас должна быть функция для добавление имени контакта и поиска контактов по имени 
contact_names = ['Zahid', 'Ali', 'Abdullatif', 'Asim']
print("Ваши контакты:", contact_names)
request = int(input("Нажмите на 1 -если хотите добавить новое имя \nНажмите на 2 - если хотите искать имя \nНажмите на 3 - если хотите удалить имя\nВаш выбор:"))
if request == 1:
    new_name = input('Введите имя для добавления: ').title()
    contact_names.append(new_name)
    print(contact_names)
elif request == 2:
    name = input('Введите имя для поиска: ').title()
    if name in contact_names:
        print(name)
    else:
        print("нет такого имени")
elif request == 3:
    name = input('Введите имя для удаления: ').title()
    if name in contact_names:
        contact_names.remove(name)
        print(contact_names)    
else:
        print("нет такого имени")
