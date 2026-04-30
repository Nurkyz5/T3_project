import json
from students import Student

def save_students(students,filename='students.json'):
    data=[students.to_dict() for student in students]
    with open(filename,'w',encoding='utf-8') as file:
        json.dump(data,file,ensure_ascii=False,indent=4)

    print("Data is saved in JSON")

def load_students(filename="students.json"):
    try:
        with open(filename,'r',encoding='utf-8') as file:
            data=json.load(file)
        students=[]
        for item in data:
            student=Student(
                item['name'],
                item['age'],
                item['grades']
            )
            students.append(student)

        print("The data is loaded from JSON")
        return students
    except FileNotFoundError:
        print("Файл не найден. Сперва сохраните данные.")
        return []
    


