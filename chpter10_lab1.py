import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    semester INTEGER
)
""")

students = [
    (1, "Ahmad", "Computer Science", 1),
    (2, "Mahmood", "Software Engineering", 2),
    (3, "Ali", "Information Technology", 3),
    (4, "Khan", "Computer Science", 4),
    (5, "Hamid", "Software Engineering", 2)
]

cursor.executemany(
    "INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?)",
    students
)

conn.commit()

print("All Students:")
cursor.execute("SELECT * FROM students")
for record in cursor.fetchall():
    print(record)

print("\nStudents of Semester 2:")
cursor.execute("SELECT * FROM students WHERE semester = ?", (2,))
for record in cursor.fetchall():
    print(record)

cursor.execute(
    "UPDATE students SET department = ? WHERE id = ?",
    ("Computer Science", 2)
)

conn.commit()

cursor.execute("DELETE FROM students WHERE id = ?", (5,))
conn.commit()

print("\nFinal Table Contents:")
cursor.execute("SELECT * FROM students")
for record in cursor.fetchall():
    print(record)

conn.close()