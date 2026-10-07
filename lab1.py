from abc import ABC, abstractmethod


# Abstract Base Class
class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email address")
        self._email = value

    @abstractmethod
    def role_info(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"


# Student class
class Student(Person):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id

    # Method Overriding
    def role_info(self):
        return f"Student ID: {self.student_id}"

    def __str__(self):
        return f"Student: {self.name}, Email: {self.email}, ID: {self.student_id}"


# Lecturer class
class Lecturer(Person):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    # Method Overriding
    def role_info(self):
        return f"Lecturer teaches: {self.subject}"

    def __str__(self):
        return f"Lecturer: {self.name}, Email: {self.email}, Subject: {self.subject}"


# Course class - Composition
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print(f"\nCourse: {self.course_name}")
        print("Students:")

        for student in self.students:
            print(student)

    def __str__(self):
        return f"Course: {self.course_name}"


# Create Student objects
student1 = Student("Ahmad", "ahmad@gmail.com", 101)
student2 = Student("Zahid", "zahid@gmail.com", 102)

# Create Lecturer object
lecturer1 = Lecturer("Dr. Ali", "ali@gmail.com", "Python Programming")


# Polymorphism
people = [student1, student2, lecturer1]

print("=== Person Information ===")

for person in people:
    print(person)
    print(person.role_info())
    print()


# Composition
course = Course("Python Programming")

course.add_student(student1)
course.add_student(student2)

course.show_students()


# Test email validation
# student1.email = "wrong-email"   # This will raise ValueError