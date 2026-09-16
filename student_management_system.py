from typing import TypeVar
T = TypeVar("T")

# Generic helper function
def first_item(items: list[T]) -> T:
    if not items:
        raise ValueError("The collection is empty")
    return items[0]

# student course registration manager
students: dict[int, dict[str, object]] ={101:{"name":"Ahmad","courses":{"CS201","CS202"}},102:{"name":"ali","courses":{"CS202","CS203"}}}

# add new student

def add_student(student_id: int,name:str) -> None:
    if student_id in students:
        print("Student already exists.")
        return
    students[student_id] = {"name" : name, "courses":set()
                            }
    print("Student added successfully.")

    # Register a course
def register_course(student_id: int, course: str) -> None:
    if student_id not in students:
        print("Student not found.")
        return

    courses = students[student_id]["courses"]
    courses.add(course)
    print("course registered successfully.")


#drop a course

def drop_course(student_id: int, course:str) -> None:
    if student_id not in students:
        print("Student not found.")
        return
    courses = students[student_id]["courses"]
    if course in courses:
        courses.remove(course)
        print("Course dropped successfully")
    else:
        print("Course is not registered.")
# search for a student
def search_student(student_id:int) -> None:
    if student_id not in students:
        print("student not found")
        return
    student = students[student_id]

    print("Student ID:",student_id)
    print("Name:",student["name"])
    print("Courses:",student["courses"])
#Display all unique courses

def display_unique_courses() -> None:
    all_courses: set[str] = set()
    for student in students.values():
        courses = student["courses"]
        all_courses.update(courses)
    print("All Unique Courses:")
    print(sorted(all_courses))


#find students sharing a selected course

def find_students_by_course(course:str) -> None:
    result = [student["name"]
              for student in students.values()
              if course in student["courses"]
              ]
    print(f"Students registered in {course}:")
    print(result)
# Sort students by name for display
def display_student_sorted() -> None:
    sorted_students = sorted(
        students.items(), key = lambda item:item[1]["name"]
    )
    print("Students sorted by name:")

    for student_id, student in sorted_students:
        print(student_id,"-",student["name"])

# Testing the program
print("===STUDENTS COURSE REGISTRATION MANAGER===")
print("\n1.Add Student")
add_student(104,"Maryam")

print("\n2.Register Course")
register_course(104,"CS205")

print("\n3.Drop Course")
drop_course(104,"CS205")

print("\n4.Search Student")
search_student(101)

print("\n5.Display Unique Courses")
display_unique_courses()

print("\n6.Find Students Sharing CS202")
find_students_by_course("CS202")

print("\n7.Students Sorted by Name")
display_student_sorted()

print("\n8.Generic Function")
print("First item:",first_item([10,20,30]))
print("First item:",first_item(["Python","Java","C++"]))