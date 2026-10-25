
class Student:
    def __init__(self, student_id, name, age, email, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.course = course

    def display(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Course:", self.course)

