from typing import Dict, Set, TypedDict


# Student record structure
class StudentRecord(TypedDict):
    name: str
    courses: Set[str]


# Dictionary: Student ID -> Student Record
students: Dict[int, StudentRecord] = {
    101: {
        "name": "Ahmad",
        "courses": {"CS101", "MATH101"}
    },
    102: {
        "name": "Zahid",
        "courses": {"CS101", "ENG101"}
    },
    103: {
        "name": "Karim",
        "courses": {"DB101", "CS101"}
    }
}


# Add a course
def add_course(student_id: int, course_code: str) -> None:
    students[student_id]["courses"].add(course_code)


# Drop a course
def drop_course(student_id: int, course_code: str) -> None:
    students[student_id]["courses"].discard(course_code)


# Find common courses between two students
def common_courses(student_id1: int, student_id2: int) -> Set[str]:
    courses1 = students[student_id1]["courses"]
    courses2 = students[student_id2]["courses"]

    return courses1.intersection(courses2)


# Find all unique courses
def all_unique_courses() -> Set[str]:
    all_courses: Set[str] = set()

    for student in students.values():
        all_courses = all_courses.union(student["courses"])

    return all_courses


# -------------------------------
# Testing the program
# -------------------------------

print("Initial Student Data:")
print(students)


# Add course
add_course(101, "DB101")
print("\nAfter adding DB101 to Ahmad:")
print(students[101])


# Duplicate course
add_course(101, "CS101")
print("\nAfter adding CS101 again to Ahmad:")
print(students[101])


# Drop course
drop_course(101, "MATH101")
print("\nAfter dropping MATH101 from Ahmad:")
print(students[101])


# Common courses
common = common_courses(101, 102)
print("\nCommon courses between Ahmad and Zahid:")
print(common)


# All unique courses
unique = all_unique_courses()
print("\nAll unique courses:")
print(unique)