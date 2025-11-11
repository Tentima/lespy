# name = input("Вводите имя:")
# print(f"Привет, {name}!")



# age = int(input("Введите ваш возраст: "))
# age_next_year = age + 1
# print(f"Через год вам будет {age_next_year} лет.")



# width=float(input("Вводите ширину:  "))
# lenth=float(input("Вводите длину: "))
# print(width*lenth)



# a = 'Hello'
# b = 4314
# c = False

# print(type(a))
# print(type(b))
# print(type(c))




# sentence = input()
# print(len(sentence.replace(" ", "")))



# user_input = input()

# if "python" in user_input.lower():
#     print("Да это про python")
# else:
#     print("Нет не про Python")



# name = input("Вводите имя: ").title()
# print(name)



# text = ("а, е, ё, и, о, у, ы, э, ю, я")
# count = 0
# vowels ="аеёиоуыэюяАЕЁИОУЫЭЮЯ"
# for char in text:
#     if char in vowels:
#         count += 1
#         print("Количество гласных", count)
        

def fitnes_center(plans, services, clients):
    total = 0
    orders = []
    name = input("Ваше имя: ").title().strip()
    if name in clients:
        print(f"С возвращением, {name}")
        level = clients[name]['уровень']
        points = clients[name]['баллы']
    else:
        print("Добро пожаловать в фитнес зал")
        level = input("Ваш уровень для тренировок: ")
        clients[name] = {'уровень': level, "баллы": 0, "история": []}
        points = 0 # баллы
    level_rank = {'начальный':1, 'средний':2, 'продвинутый':3}
    if level not in level_rank:
        print("Ошибка: неверный уровень")
        return
    
    while True:
        print("Доступные абонементы: ")
        for plan, info in plans.items():
            print(plan, info)
        choice = input("Выберите абонемент (или 'стоп')").title().strip()
        if choice == "Стоп":
            break
        if choice not in plans:
            print("Такого абонемента нет.")
            continue
        if plans[choice]["места"] == 0:
            print("Мест не осталось")
            continue
        if level_rank[level] < level_rank[plans[choice] ['уровень']]:
            print("Ваш уровень недостаточен для этого абонемента")
            continue
        try:
            count = int(input("Количество абонементов хотите? "))
        except ValueError:
            print("Пишите только числа")
            continue
        if count <= 0:
            print("Числа должны быть выше нуля")
            continue
        if count > plans[choice]["места"]:
            print("Недостаточно мест, у нас на этот тариф: ", plans[choice]["места"])
            continue
        #доп услуги
        choice_service = input(
            f"Доп. услуги : {', '.join(services.keys())} или 'нет':"
        ).split(',')
        

plans = {
    "Месячный": {"цена": 10000, "места": 10, "уровень": "начальный", "тренировок": 12},
    "Полугодовой": {"цена": 45000, "места": 5, "уровень": "средний", "тренировок": 72},
    "Годовой": {"цена": 80000, "места": 3, "уровень": "продвинутый", "тренировок": 150}
}

        