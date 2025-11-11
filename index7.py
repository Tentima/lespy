# Новая тема: Работа с файлами
# mode - режим:
# r - read - чтение
# w - write - писать - создание нового файла, старый очищает
# a - append - добавлять 
# x - создание нового файла, но если есть такая то вызов ошибка
# b - binary - используется вместо с rb и wb
# t - текстовой режим по умолчанию
# open() функция во круг которого все крутится
# file = open("имя_файла", "режим")


# with open('data.txt', 'w', encoding='utf-8') as file:
#     file.write('Сегодня ПКС 2-24 сидят на уроке\n')
#     file.write('Марсель сегодня тихий\n')

# with open('sab.txt', 'w', encoding='utf-8') as file:
#     file.write('а я Миленина отец')
    

while True:
    print("""
    1. Добавляет заметку в файл
    2. Показывает все заметки
    3. Ищет заметку по слову
    4. Заканчивает работу по выбору пользователя""")
    choice = input("Выберите действие: ")
    if choice == '1':
        textUser = input("Что хотите добавить? ")
        with open('CopyBook', 'w', encoding='utf-8' ) as file:
            file.write(f"{textUser}\n")
    elif choice == '2':
        with open('CopyBook', 'r', encoding='utf-8' ) as file:
            print(file.read())
    elif choice == '3':
        textUser = input("Что ищете? ")
        with open('CopyBook', 'r', encoding='utf-8') as file:
            for line in file:
                if textUser.lower() in line.lower():
                    print("Найдено,", line.strip())
                else:
                    print("нет такой заметки")
    elif choice == '4':
        break
    else:
        print("Выбирайте от 1го до 4х")
        continue

