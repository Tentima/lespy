# Задача: "Учёт с соханением данных"
# 1. Добавление ученика
# Запрашивает имя, возраст, балл и любимый предмет.
# Проверяет:
# длину имени (не более 16 и не менее 3 символов);
# что возраст введён числом
# После добавления сразу сохраняет обновленный словарь в students.txt.
# 2. Удаление ученика
# Запрашивает имя и удаляет его, если найден.
# После удааления записывает изменения в students.txt.
# 3. Просмотр всех учеников
# Выводит всех учеников построчно:
# Имя: Aman / Возраст: 16 лет
    # Балл: 4.8 / Любимый предмет: Математика
# Загружает данные из файла перед показом (если файл существует).
# 4. Изменение данных ученика
# Запрашивает имя.
# Позволяет изменить:
# 1- возраст
# 2- балл
# 3- любимый предмет
# После изменения данные сохраняются в students.txt
# 5. Выход из программы

import json
import os

FILE_NAME = "students.txt"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

def add_student(students):
    name = input("Введите имя ученика: ").strip()
    if not (3 <= len(name) <= 16):
        print("Ошибка: длина имени должна быть от 3 до 16 символов.")
        return
    if name in students:
        print("Ученик с таким именем уже существует.")
        return
    age = input("Введите возраст ученика: ").strip()
    if not age.isdigit():
        print("Ошибка: возраст должен быть числом.")
        return
