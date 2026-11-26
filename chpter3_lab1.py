


file_name = "students.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write("101,Ahmad,Computer Science\n")
    file.write("102,Mahmood,Information Technology\n")
    file.write("103,Ali,Software Engineering\n")
    file.write("104,Fahim,Computer Science\n")
    file.write("105,Karim,Information Technology\n")

print("Five student records have been written successfully.")

print("\nAll Student Records:")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("The file does not exist.")

# 3. Search for a student by ID
search_id = input("\nEnter student ID to search: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        found = False

        for line in file:
            student = line.strip().split(",")

            if student[0] == search_id:
                print("Student Found:")
                print("ID:", student[0])
                print("Name:", student[1])
                print("Department:", student[2])
                found = True
                break

        if not found:
            print("Student not found.")

except FileNotFoundError:
    print("The file does not exist.")

# 4. Append a new student
with open(file_name, "a", encoding="utf-8") as file:
    file.write("106,Farid,Computer Science\n")

print("\nNew student record added successfully.")

# 5. Count total student records
try:
    with open(file_name, "r", encoding="utf-8") as file:
        total = 0

        for line in file:
            if line.strip():
                total += 1

    print("Total student records:", total)

except FileNotFoundError:
    print("The file does not exist.")
