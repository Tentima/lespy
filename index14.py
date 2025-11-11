# создайте программу для комп клуба, которая будет спрашивать играл ли этот человек наше игру, если "нет" не играл, тогда регистрируется, он создает себе логтн и пароль, и этот логин и пароль мы записываем к себе в список, а если он скажет, что у нас играл, мы проверим свой список клиентов, если он та есть, скажем"Добро Пожаловать в бойцовский клуб", а если нет в списке, отправляем его на регистрацию. Дальше после входа, он может пополнить свой баланс или проверить сколько у него на балансе денег. У нашего комп клуба есть тарифы, и может выбрать из этих тарифов, если хватает денег он выбирает, то с его баланса снимается это сумма 
tarif = {
    '3 часа': 150,
    '5 часов': 200,
    '7 часов': 330,
}
clients = {
    "Agent007": {'password':'qwerty', 'balance':300},

}
def register():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    password2 = input("Введите пароль: ")
    if len(password) == len(password2):
        clients[login]={'password': password, 'balance': 0}
        print(f"Добро пожаловать в бойцовский клуб")
    else:
        print("Разные пароли")

    def login():
        login = input("Введите логин: ")
        if login in clients:
            password = input("Введите пароль: ")
            if password == clients[login]['password']:
                print("Снова добро пожаловать в бойцовский клуб")
            else:
                print("пароль не совпадает")
        else:
            print("Нет такого юзера")

def show_balance(login):
    print("Ваш счёт:", clients[login]['balance'],"сом")

def choose_tarif(user):
    print("\nДоступные тарифы")
    for name, price in tarif.items():
        print(f"{name} {price} сом.")
    choice = input("Выберите тариф: ")
    if choice in tarif:
        cost = tarif[choice]
        if clients[user]['balance'] >= cost:
            clients[user]['balance'] -= cost
            print(f"Вы выбрали тариф '{choice}'. С вашего баланса списано {cost} сом.")
            print(f"Остаток: {clients[user]['balance']} сом.")
        else:
            print("Недостаточно средств! Пополните баланс.")
    else:
        print("Такого тарифа нет.")

while True:
        print("\nЧто вы хотите сделать?")
        print("1. Проверить баланс")
        print("2. Выбрать тариф")
        print("3. Выйти")
        choice = input("Ваш выбор: ")

        if choice == "1":
            show_balance(login)
        elif choice == "2":
            choose_tarif(login)
        elif choice == "3":
            print("До встречи в бойцовском клубе!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

