hotel = {
    "Стандарт": {"цена": 3000, "места": 5, "макс_гостей": 2},
    "Комфорт": {"цена": 5000, "места": 3, "макс_гостей": 3},
    "Люкс": {"цена": 10000, "места": 2, "макс_гостей": 4}
}
def hotel_booking(hotel):
    booking = []
    total = 0
    while True:
        name = input("Имя:")
        guests = int(input("Количество гостей: "))
        room = input("Какой номер хотите \n(Стандарт, Комфорт, Люкс) ?")
        if room == 'стоп':
            print("Спасибо что посетили нас")
            break
        if room not in hotel:
            print("Такого номера нет")
            continue
        if hotel[room]['места'] == 0:
            print("Номеров больше нет")
            continue
        if guests > hotel[room]["макс_гостей"]:
            print("Слишком много гостей для этого номера")
            continue
        nights = int(input("количество ночей: "))
        if nights <= 0:
            print("Число должно быть положительным!")
            continue

        sums = hotel[room]["цена"] * nights
        total += sums
        hotel[room]['места']-=1
        booking.append(f"{room} {nights} = {total} сом")
        print(f"Вы {name} забронили {room} на {nights} за {total} сом")
        