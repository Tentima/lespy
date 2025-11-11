library = {
    "Роман": {"Война и мир": "Толстой"},
    "Фантастика": {"Мастер и Маргарита": "Булгаков"},
    "Поэзия": {"Евгений Онегин": "Пушкин"}
}
rep = input("1-показать библ, 2-добавить книги, 3-удалить книгу\n4-найти книгу, 5-автор книг, 6-количество, 7-выйти: ")
if rep == '1':
    for k,v in menu_food.items():
        print(key, value)
elif rep == "2":
    category = input("Введите жанр: ")
    title = input("Введите название книги: ")
    author = input("Введите автора:")
    if category in library:
        library[category][title] = author
        print("Успешно добавлен")
elif rep == "3":
    category = input("Введите жанр: ")
    title = input("Введите название книги: ")
    if category in library and title in library:
        del library[category][title]
        print("Успешно удален")
    else:
        print("нет такого")
elif rep == '4':
    title = input("Введите название книги:")
    found = False
    for category, books in library. items():
        if title in books:
            print(f"Найдена: {title} - {books}")
            found = True 
    if not found:
        print("нет такой книги")
elif rep == '5':
    author = input("Введите автора:")
    found = False
    for category, books in library.items():
        for title, auth in books.items():
            if auth == author:
                print(f"{title} категория: {category}")
                found = True 
    if not found:
        print("У автора книг нет в библиотеке")
elif rep == '6':
    total = 0 
    for books in library.values():
        total+=len(books)
    print('Всего в библиотеке: ', total, 'книг')
else:
    print("неверный ввод! Вы должны выбрать от 1го до 6ти")
    