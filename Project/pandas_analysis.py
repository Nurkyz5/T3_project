import pandas as pd


def pandas_analysis(students):
    if not students:
        print("Список студентов пуст.")
        return

    data = []

    for student in students:
        data.append({
            "Имя": student.name,
            "Возраст": student.age,
            "Оценки": student.grades,
            "Средний балл": student.get_average()
        })

    df = pd.DataFrame(data)

    print("\nТаблица студентов:")
    print(df)

    print("\nСортировка по среднему баллу:")
    print(df.sort_values(by="Средний балл", ascending=False))