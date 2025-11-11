# исключение - try except
# continue - отправляет в начало, а break завершает цикл
while True:
    try:
        a = int(input("Первое: "))
    except ValueError:
        print("Вводите только числа")
        continue
    simbol = input("символ: ")
    try:
        b = int(input("Второе: "))
    except ValueError:
        print("Вводите только числа")
        continue
    if simbol == '/':
        try:
            print(a/b)
        except ZeroDivisionError:
            print("Делить на ноль нельзя")
    elif simbol == '+':
        print(a+b)
    else:
        print("Надо писать + - * /")
        