def car_reental(cars, services):
    total = 0 # общая сумма 
    orders = [] # список заказов
    chosen_services = [] # список доп.услуг
    name = input("Имя: ")
    try:
        passajirs = input("количество пассажиров: ")
    except ValueError:
        print("Пишите только числа!")
        return
    while True:
        for name in cars:
            print(name, end=", ")
        choice = input("Какой тип машины хотите (стоп): ").title()
        if choice == 'стоп':
            break
        if choice not in cars:
            print("Нет такого типа машины")
            continue
        if passajirs > cars[choice]["макс_пассажиров"]:
            print("Слишком много пассажиров для этой машины")
            continue
        if cars[choice]['машины'] == 0:
            print("Не осталось машин этой категории. Выберите другие")
            continue
        try:
            days = int(input("количество дней: "))
        except ValueError:
            print("Пишите только числа!")
            continue
        if days <= 0:
            print("Количество дней аренды должно быть положительным")
            continue
        print(services)
        service_input = input("Выберите доп.услуги: ").title().strip()
        if service_input == 'нет':
            print("ОК")
        elif service_input in services:
            chosen_services.append((service_input, services[service_input]))
            print(chosen_services)
        else:
            print("нет такой доп.услуги")
            # начнем подсчет
            bc = cars[choice]['цена'] * days
            total += bc
            cars[choice]['машины'] -= 1
            orders.append(f"{choice} ({days} дней) {total}")
            print(f"Вы арендовали {choice} на {days}дней за {total}сом")
            # Ваша задача сделать скидку если сумма будет от 20тысяч сомов на 15% 
            # и также считать доп.услуги и добавлять их к общей сумме если они есть



cars = {
    "Эконом": {"цена": 2000,  "машина": 5, "макс_пассажиров": 4},
    "Комфорт": {"цена": 3500,  "машина": 3, "макс_пассажиров": 5},
    "Бизнес": {"цена": 6000,  "машина": 5, "макс_пассажиров": 5},   
}
services = {

}
car_reental(cars, services)