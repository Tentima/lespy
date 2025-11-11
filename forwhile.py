print("hello"*100)
print("hello")
print("hello")
print("hello")

# циклы: for-для and while-пока

# цикл for  нужен чтобы повторять действия несколько раз, (список, строка, диапазон чисел, кортежи и т.д. )
# for переменная in последовательность:
#   действия

# range(start,stop, step) - генератор чисел, он создает последовательность чисел по которой проходит цикл
for name in range(1,11):
    print(name,'hello')

names =['jiraf', 'Aibek', 'begemot', 'Gena', 'begemot', 'Gena','Mars',]
for name in names:
    print('Привет',name)
    # Циклы
    # for | while

    # цикл - это когда программа повторяет одно и то же действие много раз 

    # цикл for перебирает элементы какого-то набора (списка, строки, диапазона чисел и т.д)

    # range() "генератор чисел". он создает последовательность чисел которые удобно перебирать в цикле
    # range(start, stop, step)

    # for переменная in последовательность:
#         действие

for num in range(0, 101, 2):
    print(num,'hello')
    
numbers = []
for num in range(1,101,2):
    numbers.append(num)
print(numbers)

name ='Abdul345boid35'
nums = []
for n in name:
    if n.isdigit():
        nums.append(n)
print(nums)

lista = 'Abdul345bosid35'
nums = []
for n in name:
    if n.isdigit():
        nums.append(n)
print(nums)

lista = ['Gena', 'Aibek', 'Mili']
lst = []
for l in lista:
    lst.append(l.upper())
print(lst)


# float неизменяемый тип
# str
# int неизменяемый тип 
# bool неизменяемый
# list [] изменяемый тип данных
# tuple () неизменяемый тип данных
# set - множества - {34,46,557} изменяемый тип 
# dict - dictionary - словари {key:value} изменяемый тип
names = {
    'Elnura':17,
    'Davlet':24,
    'Gena': 34,
}
for n, v in names.items():
    print(n, v+1)

    # у нас есть список телефонных номеров, нам надо создать программу которая будет спрашивать действие:
    # 1-добавить новый номер телефона
    # 2-удалить номер телефона
    # 3-поиск по имени и вывод имени и телефона 
    # 4-изменение имени и телефона также должна быть проверка на длину имени, имя должен быть выше двух символов 
    # номер телефона должен быть ровно из 9 символов, не больше и не меньше, программа должна проверять это и если не соответствует длине, то говорить пользователю о том что надо исправить
    contact_names = {
        'Davlet': 770700700,
        'Aliya': 202456456,
        'Adilet': 550343434,
    }
    num_request = input("1-добавить новый номер телефона\n2-удалить номер телефона\n3-поиск по имени и вывод имени и телефона\n4-изменение имени и телефона\nВыберите действие:")
if num_request == '1':
    new_name = input("Введите имя: ").title()
    if len(new_name) > 2 and len(new_name)< 20:
        new_numbers = input("Введите номер телефона: ")
        if len(new_numbers) == 9:
            contact_names[new_name] = new_numbers
            print(contact_names)
        else:
            print("номер должен быть 9 символов")
    else:
        print("имя должно быть от 3х и выше символов")
elif num_request == '2':
    del_name = input("Введите имя для удаления: ").title()
    if del_name in contact_names.keys():
        print(contact_names[del_name], 'успешно удален')
        del contact_names[del_name]
        print(contact_names)
    else:
        print(del_name, 'не найден')
elif num_request =='3':
    search_name = input("Введите имя для поиска").title()
    if search_name in contact_names.keys():
        print(search_name, contact_names[search_name])
    else:
        print("нет такого контакта")
elif num_request == '4':
    choice = input("1-изменить имя\n2-изменить номер\nДействие:")
    if choice == '1':
        print(contact_names)
        old_name = input("Введите прошлое имя: ")
        if old_name in contact_names.keys():
            new_name = input("Введите новое имя:")
            contact_names[new_name]=contact_names.pop(old_name)
            print("Контакт успешно изменен")
            print(contact_names)
    elif choice == '2':
        name = input('Введите имя контакта:').title()
        if name in contact_names.keys():
            new_phone = input('Введите номер:')
            if len(new_phone) == 9:
                contact_names[name]= new_phone
                print("Успешно изменено")
                print(contact_names)
            else:
                print("длина номера от 9 символов")
        else:
            print("Нет такого контакта")
            
