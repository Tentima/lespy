menu_food = {
    "Плов": 250,
    "Манты": 300,
    "Лагман": 280,
    "Шашлык": 400,
    "Бшбармак": 500
}
menu_drinks = {
    "Чай": 50,
    "Кофе": 120,
    "Кумыс": 150,
    "Айран": 80,
    "Сок": 100
}
cart = [] #Ваша корзина куда кладется стоимость заказов
while True:
    req = int(input('1. Показать меню блюд\n2. Показать меню напитков\n3. Заказать блюдо\n4. Заказать напиток\n5. Показать корзину и итоговую сумму\n6. Выйти\nВыберите действие:'))
    if req == 1:
        for k,v in menu_food.items():
            print(f"{k}: {v}com")
    elif req == 2:
        for k,v in menu_drinks.items():
            print(f"{k}: {v}com")
    elif req == 3:
        print(menu_food)
        name_food = input("какое блюдо хотите?").title()
        if name_food in menu_food:
            cart.append(menu_food[name_food])
            print(cart)
    elif req == 4:
        print(menu_drinks)
        name_drink = input("какой напиток хотите?").title()
        if name_drink in menu_drinks:
            cart.append(menu_drinks[name_drink])
            print(cart)
    elif req == 5:
        if not cart:
            print("В корзине", len(cart))
            total = sum(cart)
            print("Общая сумма:", total)
        else:
            print("Вы ничего не заказали")
    elif req == 6:
        print("Спасибо что посетили")
        break
    