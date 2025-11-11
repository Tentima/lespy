# Напиши программу "Список дел"
# Пользователь может:
# 1. Посмотреть список дел.
# 2. Добавить новое дело.
# 3. Удалить дело по названию.
# 4. Отметить дело как выполненное.
# 5. Выйти.
tasks = {
    'Сделать домашку': "не сделано",
    'Почистить зубы': "сделано",
}

usl = """
    1. Посмотреть список дел.
    2. Добавить новое дело.
    3. Удалить дело по названию.
    4. Отметить дело как выполненное.
    5. Выйти."""
while True:
    print(usl)
    req = input("Выберите действие: ")
    if req == '1':
        for key, value in tasks.items():
            print(f"{key} - {value}")
    elif req == '2':
        print(tasks)
        new_task = input("Добавить дело: ").capitalize()
        status = "не сделано"
        tasks[new_task] = status 
        print(tasks)
    elif req == '3':
        print(tasks)
        del_tasks = input("Удалить дело: ").capitalize()
        if del_tasks in tasks:
            del tasks[del_tasks]
            print(tasks)
        else:
            print("нет такого дела")
    elif req == '4':
        print(tasks)
        reStatus = input("Название дела: ").capitalize()
        status ="сделано"
        if reStatus in tasks:
            tasks[reStatus] = status