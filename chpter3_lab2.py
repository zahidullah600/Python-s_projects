
import csv

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["student_id", "name", "midterm", "final"])

    writer.writerow([101, "Ahmad Khan", 70, 80])
    writer.writerow([102, "Ali Ahmad", 45, 55])
    writer.writerow([103, "Mohammad, Rahim", 85, 90])
    writer.writerow([104, "Farid Khan", 60, 65])
    writer.writerow([105, "Abdul Wahid", 30, 40])

print("Students data saved successfully.")

students = []

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        midterm = int(row["midterm"])
        final = int(row["final"])

        total = midterm + final
        average = total / 2

        student = {
            "student_id": row["student_id"],
            "name": row["name"],
            "midterm": midterm,
            "final": final,
            "total": total,
            "average": average
        }

        students.append(student)


print("\nStudent Results:")

for student in students:
    print(student["name"],
          "Total:", student["total"],
          "Average:", student["average"])

threshold = 50

print("\nPassed Students:")

for student in students:
    if student["average"] >= threshold:
        print(student["name"], "Average:", student["average"])

with open("results.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "student_id",
        "name",
        "midterm",
        "final",
        "total",
        "average"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

print("\nResults saved to results.csv")
