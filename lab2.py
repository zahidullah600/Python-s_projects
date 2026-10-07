# Collection Operations

# 1. Create a list of at least 10 student scores
scores = [85, 72, 55, 90, 60, 45, 78, 88, 60, 95]

print("Student Scores:")
print(scores)


# 2. Calculate minimum, maximum and average

minimum = min(scores)
maximum = max(scores)
average = sum(scores) / len(scores)

print("\nMinimum Score:", minimum)
print("Maximum Score:", maximum)
print("Average Score:", average)


# 3. Create a new list containing scores >= 60
# Using List Comprehension

passed_scores = [score for score in scores if score >= 60]

print("\nScores >= 60:")
print(passed_scores)


# 4. Convert the list to a set

score_set = set(scores)

print("\nSet of Scores:")
print(score_set)

print("Original number of scores:", len(scores))
print("Number of unique scores:", len(score_set))

# 60 appears twice, so the set keeps only one 60.


# 5. Create a dictionary mapping student IDs to names

students = {
    101: "Ahmad",
    102: "Zahid",
    103: "Karim",
    104: "Bilal",
    105: "Hamid"
}

print("\nStudent Dictionary:")
print(students)


# 6. Search for one student by ID

search_id = 103

if search_id in students:
    print("\nStudent found:")
    print("ID:", search_id)
    print("Name:", students[search_id])
else:
    print("\nStudent not found.")


# 7. Sort student records by score

student_records = [
    ("Ahmad", 85),
    ("Zahid", 72),
    ("Karim", 55),
    ("Bilal", 90),
    ("Hamid", 60)
]

sorted_records = sorted(student_records, key=lambda student: student[1])

print("\nStudents sorted by score:")
for name, score in sorted_records:
    print(name, score)


# 8. Use enumerate()

print("\nScores with index:")

for index, score in enumerate(scores, start=1):
    print(index, score)


# 9. Use zip()

names = ["Ahmad", "Zahid", "Karim", "Bilal", "Hamid"]
scores2 = [85, 72, 55, 90, 60]

print("\nNames and Scores:")

for name, score in zip(names, scores2):
    print(name, "->", score)