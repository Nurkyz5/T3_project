from students import Student
from json_manager import save_students, load_students
from numpy_analysis import numpy_analysis
from pandas_analysis import pandas_analysis


students = []


def add_student():
    name = input("Введите имя студента: ")
    age = int(input("Введите возраст студента: "))

    grades_input = input("Введите оценки через запятую: ")
    grades = [int(grade.strip()) for grade in grades_input.split(",")]

    new_student = Student(name, age, grades)
    students.append(new_student)

    print(f"{name} добавлен(а) в журнал.")


def show_students():
    if not students:
        print("Список студентов пуст.")
        return

    print("\nСписок студентов:")
    for student in students:
        print(
            f"Имя: {student.name}, "
            f"Возраст: {student.age}, "
            f"Оценки: {student.grades}, "
            f"Средний балл: {student.get_average():.2f}"
        )


def delete_student():
    name = input("Введите имя студента для удаления: ")

    for student in students:
        if student.name.lower() == name.lower():
            students.remove(student)
            print("Студент удален.")
            return

    print("Студент не найден.")


def search_student():
    name = input("Введите имя студента для поиска: ")

    for student in students:
        if student.name.lower() == name.lower():
            print(
                f"Найден студент: {student.name}, "
                f"Возраст: {student.age}, "
                f"Оценки: {student.grades}, "
                f"Средний балл: {student.get_average():.2f}"
            )
            return

    print("Студент не найден.")


def menu():
    global students

    while True:
        print("\n===== МЕНЮ =====")
        print("1. Добавить студента")
        print("2. Показать всех студентов")
        print("3. Удалить студента")
        print("4. Сохранить в JSON")
        print("5. Загрузить из JSON")
        print("6. Анализ NumPy")
        print("7. Анализ pandas")
        print("8. Поиск студента")
        print("0. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            save_students(students)
        elif choice == "5":
            students = load_students()
        elif choice == "6":
            numpy_analysis(students)
        elif choice == "7":
            pandas_analysis(students)
        elif choice == "8":
            search_student()
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


menu()