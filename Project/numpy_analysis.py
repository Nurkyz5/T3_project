import numpy as np


def numpy_analysis(students):
    if not students:
        print("Список студентов пуст.")
        return

    all_grades = []

    for student in students:
        all_grades.extend(student.grades)

    grades_array = np.array(all_grades)

    print("\nАнализ с NumPy")
    print("Средний балл всех студентов:", np.mean(grades_array))
    print("Наивысшая оценка:", np.max(grades_array))