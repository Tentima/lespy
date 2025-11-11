def add_students(students):
    name = input("Введите имя: ").title().strip()
    group = input("Введите название группы").strip()
    try:
        age = int(input("Введите возраст:"))
    except ValueError:
        print("Введите только цифры")
    if name in students:
        print("Такой уже существует")
        return
    students[name] = {"группа":group, "возраст":age, 'оценки':0}
    print(f"Студент {name} добавлен")

def add_subject(students):
    name = input("Введите название предмета: ").title().strip()
    teacher = input("Введите имя и Фамилие учителя: ").title().strip()
    if name in subjects:
        print("Такой предмет уже есть")
        return
    subjects[name] = teacher
    print(subjects)
    print(f"Предмет {name} добавлен. Препод {teacher} добавлен")

def add_mark(students, subjects):
    name = input("Введите Имя и Фамилию учителя: ").title().strip()
    if name not in students:
        print("Такого студента нет!")
        return
    subject = input("Введите предмет: ").title().strip()
    if subject not in subjects:
        print("Такого предмета нет!")
        return
    try:
        mark = int(input("Введите оценку (от 0-100) "))
    except ValueError:
        print("Пишите только числа")
        return
    if mark < 0 or mark > 100:
        print("Оценка должна быть от 0 до 100")
        return
    students[name]["оценки"][subject] = mark
    print(f"{name} получил {mark} по предмету {subject}")
def show_student_info(students):
    name = input("Введите имя студента: ").title().strip()
    if name not in students:
        print("Такого студента нет!")
        return
    data = students[name]
    print(f"Инфо о студенте {name}:")
    print(f"Группа: {data['группа']}")
    print(f"Возраст: {data['возраст']}")
    print(f"Оценки:")
    if not data['оценки']:
        print("Нет оценок")
    else:
        for subj, mark in data['оценки'].items():
            print(f"{subj}: {mark}")
    avg = calculate_average(data['оценки'])
    print(f"Средний балл: {avg}\n")

def calculate_average(marks):
    if not marks:
        return 0 
    total = 0
    count = 0
    for mark in marks.values():
        total += mark
        count += 1
    return round(total / count, 2)
       
def show_top_students(students):
    group = input("Введите навание группы: ")
    group_students = {}
    for name, data in students.items():
        if data['группа']==group:
            avg = calculate_average()
            group_students[name] = avg
    if len(group_students) == 0:
        print("В этой группе нет студентво")
        return
    sorted_names = sorted(group_students.keys())
    print(f"Топ студентов группы {group}")
    for name in sorted_names:
        print(f"{name} - средний балл {group_students[name]}")
        

def expel_students(students):
    expelled = []
    for name, data in list(students.items()):
        avg = calculate_average(data['оценки'])
        if avg < 50:
            expelled.append(name)
            del students[name]
    if expelled:
        print("Отчислены студенты: ")
        for name in expelled:
            print(name, end=', ')
    else:
        print("Никто не отчислен - все молодцы")

students = {}
subjects = {}
while True:
    print("""
        1.Регистрировать студентов (имя, группа, возраст).
        2. Добавлять предметы (название, преподователь).
        3. Назначать оценки студентам по предметам.
        4. Вычислять средний балл каждого студента.
        5. Показывать топ-студентов группы.
        6. Проверять, кто подлежит отчислению (если средний балл < 50).""")
    choice = int(input("Выберите действие: "))
    if choice == 1:
        add_students(students)
    elif choice == 2:
        add_subject(subjects)
    elif choice == 3:
        add_mark(students,subjects)
    elif choice == 4:
        show_student_info(students)
    elif choice == 5:
         show_top_students(students)
    elif choice == 6:
        expel_students(students)
    elif choice == 0:
        print("Выход  из системы")
        break
    else:
        print("Вводите от 1 до 6ти")
