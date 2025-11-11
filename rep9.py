# Напишите функцию order(menu), которая:
# 1. Спрашивает у пользователя, что он хочет заказать(несколько раз, пока не введёт стоп).
# 2. Если блюда нет в меню - выводит сообщение "Такого блюда нет". 
# 3. Если есть - добавляет его цену к итоговой сумме.
# 4. В конце выводит:
#     список заказанных блюд,
#     итоговую сумму.
def order(menu):
    total = 0 #итог сумма
    ordered = [] # список заказанных блюд
    while True:
        item = input("Что закажете? ")
        if item == 'стоп':
            break
        if item in menu:
            # total = total + menu[item]
            total += menu[item]
            ordered.append(item)
            print(ordered)
        else:
            print('Такого блюда нет')
    print(f"Ваш заказ: {ordered}")
    print(f"Сумма: {total}")

menuList = {
    "бургер": 150,
    "пицца": 500,
    "салат": 200,
    "суп": 120,
    "чай": 50
}
# order(menuList)

library = {
    "Гарри Потер": 3,
    "Влесталин колец": 2,
    "Три мушкетёра": 2
}
def library_system(library):
    books_taken = []
    while True:
        book = input("Какую книгу вы хотите? ")
        if book == 'стоп':
            break
        if book in library:
            library[book] -= 1
            books_taken.append(book)
            print("Взяли", book)
        elif library[book] == 0:
            print('Эта книга закончилось')
        else:
            print("Такой книги нет")
    print("Ваши книги", books_taken)

library = {
    "Гарри Потер": 3,
    "Влесталин колец": 2,
    "Три мушкетёра": 2
}   
