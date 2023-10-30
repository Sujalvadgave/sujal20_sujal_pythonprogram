
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        return f"Person: Name - {self.name}, Age - {self.age}"
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def get_info(self):
        person_info = super().get_info()
        return f"{person_info}, Student ID - {self.student_id}"
class Undergraduate(Student):
    def __init__(self, name, age, student_id, major):

        super().__init__(name, age, student_id)
        self.major = major

    def get_info(self):
        student_info = super().get_info()
        return f"{student_info}, Major - {self.major}"

undergrad_student = Undergraduate("sujal", 20, "EN21188455", "Computer Science")

print("Undergraduate Student Information:")
print(undergrad_student.get_info())
