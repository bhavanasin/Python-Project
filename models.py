# models.py

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}  # Dictionary to map subject names to grades

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average(self):
        if not self.grades:
            return 0.0
        total = sum(self.grades.values())
        return total / len(self.grades)