# Напиши программу "Барбершоп"
# В барбершопе можно:
usl = """
1. Показать список барберов и их услуги.
2. Записаться на услугу к выбранному барберу.
3. Отменить запись по имени клиента.
4. Показать все записи.
5. Найти самого популярного барбера (у кого больше всего клиентов).
6. Выйти."""
barbers = {
    "Алия": {
        "Стрижка": 500,
        "Бритьё": 300
    },
    "Давлет": {"Стрижка": 450, "Осветление": 800},
    "Ахмед": {"Модная стришка": 700, "Укладка": 400}
}
print(usl)
zapis = {}
while True:
    req = input("Введите действие: ")
    if req == '1':
        for name, services in barbers.items():
            print(name)
            for ser, price in services.items():
                print(f"   {ser}: {price}")
    elif req == '2':
        name = input("Введите имя клиента: ")
        barber = input("Введите барбера: ")
        if barber in barbers:
            for service, price in barbers[barber].items():
                print(f" {service}: {price}сом")
            service = input("Выберите услугу мастера: ")
            priceService = barbers[barber][service]
            time = input("Укажите время на которую хотите: ")
            zapis[name]= {
                'Барбер':barber,'Услуги':service,
                'Стоимость': priceService, 'время': time
            }
            print(zapis)
    elif req == '3':
        name = input("Введите имя клиента отмены: ")
        if name in zapis:
            del zapis[name]
            print(f"Отменена запись у {name}")
        else:
            print("Нет такого")
    elif req =='4':
        for zap in zapis:
            print(zap)
            