class Student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return round(sum(self.grades) / len(self.grades), 2)
    def to_dict(self):
        return {
            'name':self.name,
            'age':self.age,
            'grades':self.grades
        }

