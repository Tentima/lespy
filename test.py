movies = ["Люси", "Аватар", "Титаник", "Матрица", "Гладиатор"]
print("Ваши списки:", movies)
request = int(input("Нажмите на 1 если хотите добавить фильм \nНажмите на 2 если хотите найти фильм \nНажмите на 3 чтобы удалить фильм \nВаш выбор:"))
if request == 1:
    new_name = input('Введите название для добавления: ')
    movies.append(new_name)
    print(movies)
elif request == 2:
    name = input('Введите название для поиска: ')
    if name in movies:
        print(name)
    else:
        print("Нет такого фильма")
elif request == 3:
    name = input('Введите название для удаления: ')
    if name in movies:
        movies.remove(name)
        print(movies)
else:
    print("Нет такого фильма")