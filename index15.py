# Задача: Транспортная компания ведёт учёт грузов, которые нужно доставить.
# Каждый груз имеет: название груза, вес (в кг), город назначения, стоимость доставки (в сомах), статус - "в пути" или "доставлен"
# 1)Показывает все грузы. 
# 2)Добавляет новый груз.
# 3)Находит все грузы, направленные в указанный город.
# 4)Находит самый тяжёлый груз.
# 5)Показывает все грузы дешевле заданной стоимости.
# 6)Меняет статус груза на "доставлен".
# 7)Увеличивает стоимость всех доставок на 10%.
# 0)Завершает работу программы.
cargo_list = [
    {"название": "Телевизор", "вес": 15, "город": "Ош", "стоимость":1200, "статус": "в пути"},
    {"название": "Холодильник", "вес": 45, "город": "Бишкек", "стоимость": 3000, "статус": "в пути"},
    {"название": "Книги", "вес": 5, "город": "Талас", "стоимость": 500, "статус": "доставлен"},]


def see_cargo():
    if not cargo_list:
        print("Список грузов пуст.")
    else:
        for cargo in cargo_list:
            print(cargo)


def add_cargo():
    name = input("Введите название груза: ")
    weight = float(input("Введите вес (в кг): "))
    city = input("Введите город назначения: ")
    cost = float(input("Введите стоимость доставки (в сомах): "))
    status = "в пути"
    cargo_list.append({"название": name, "вес": weight, "город": city, "стоимость": cost, "статус": status})
    print("Груз успешно добавлен!")


def city():
    city = input("Введите город для поиска: ")
    found = [cargo for cargo in cargo_list if cargo["город"].lower() == city.lower()]
    if found:
        for cargo in found:
            print(cargo)
    else:
        print("Грузы для этого города не найдены.")


def gruz():
    if cargo_list:
        heaviest = max(cargo_list, key=lambda c: c["вес"])
        print("Самый тяжёлый груз:", heaviest)
    else:
        print("Список грузов пуст.")


def find_gruz():
    limit = float(input("Введите максимальную стоимость: "))
    found = [cargo for cargo in cargo_list if cargo["стоимость"] < limit]
    if found:
        for cargo in found:
            print(cargo)
    else:
        print("Нет грузов дешевле указанной стоимости.")


def menyat_status():
    name = input("Введите название груза для изменения статуса: ")
    for cargo in cargo_list:
        if cargo["название"].lower() == name.lower():
            cargo["статус"] = "доставлен"
            print(f"Статус груза '{cargo['название']}' изменён на 'доставлен'.")
            return
    print("Груз не найден.")


def prosent():
    for cargo in cargo_list:
        cargo["стоимость"] *= 1.1
    print("Стоимость всех доставок увеличена на 10%.")


def menu():
    while True:
        print("""
         Показать все грузы
         Добавить новый груз
         Найти грузы по городу
         Найти самый тяжёлый груз
         Показать грузы дешевле заданной стоимости
         Изменить статус груза на 'доставлен'
         Увеличить стоимость всех доставок на 10%
         Выйти
        """)
        choice = input("Выберите действие: ")

        if choice == "1":
            see_cargo()
        elif choice == "2":
            add_cargo()
        elif choice == "3":
            city()
        elif choice == "4":
            gruz()
        elif choice == "5":
            find_gruz()
        elif choice == "6":
            menyat_status()
        elif choice == "7":
            prosent()
        elif choice == "0":
            print("Завершение")
            break
        else:
            print("Неверный выбор. Повторите попытку.")

            
menu()
