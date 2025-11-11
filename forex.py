def analyze_journal(journal):
    name = input("Введите имя ученика: ")
    if name not in journal:
        print("Ученика нет в журнале")
        return
    
    student_grades = journal[name]
    total_sum = 0
    total_count = 0

    print(f"Оценки ученика {name}:")
    for subject, grades in student_grades.items():
        avg = sum(grades) / len(grades)
        total_sum += sum(grades)
        total_count += len(grades)
        print(f"{subject}: средняя оценка {avg:.2f}")

    overall_avg = total_sum / total_count
    print(f"Общая средняя оценка: {overall_avg:.2f}")

    if overall_avg >= 4.5:
        print("Отличник")
    elif overall_avg >= 3:
        print("Хорошист")
    else:
        print("Нужно подтянуть учёбу")

journal = {
    "Алиса": {"математика": [5, 4, 5], "русский": [4, 4, 3]},
    "Бек": {"математика": [3, 2, 4], "русский": [5, 5, 5]},
    "Дана": {"математика": [5, 5, 5], "русский": [4, 5, 4]}
}

analyze_journal(journal)

