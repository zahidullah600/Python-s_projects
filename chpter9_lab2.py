import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Course Selection")
root.geometry("500x500")

courses = [
    "Programming",
    "Advanced Programming",
    "Database",
    "Computer Networks",
    "Operating Systems",
    "Cyber Security",
    "Web Development",
    "Software Engineering",
    "Data Structures",
    "Artificial Intelligence",
    "Computer Architecture",
    "Discrete Mathematics"
]

course_frame = tk.LabelFrame(root, text="Select Courses")
course_frame.pack(fill="both", expand=True, padx=15, pady=10)

listbox = tk.Listbox(course_frame, selectmode="multiple", height=10)
listbox.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(course_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

for course in courses:
    listbox.insert(tk.END, course)

semester_label = tk.Label(root, text="Select Semester")
semester_label.pack(pady=5)

semester_combo = ttk.Combobox(
    root,
    values=["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8"],
    state="readonly"
)

semester_combo.set("Semester 1")
semester_combo.pack(pady=5)

count_label = tk.Label(root, text="Selected Courses: 0")
count_label.pack(pady=5)

result_label = tk.Label(root, text="Selected Courses and Semester", justify="left")
result_label.pack(pady=10)

def update_count(event):
    selected = listbox.curselection()
    count_label.config(text=f"Selected Courses: {len(selected)}")

def show_selection():
    selected = listbox.curselection()
    selected_courses = []

    for index in selected:
        selected_courses.append(listbox.get(index))

    semester = semester_combo.get()

    result = "Courses:\n" + "\n".join(selected_courses)
    result += "\nSemester: " + semester

    result_label.config(text=result)

def clear_selection():
    listbox.selection_clear(0, tk.END)
    count_label.config(text="Selected Courses: 0")
    result_label.config(text="Selected Courses and Semester")

show_button = tk.Button(root, text="Show Selection", command=show_selection)
show_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear Selection", command=clear_selection)
clear_button.pack(pady=5)

listbox.bind("<<ListboxSelect>>", update_count)

root.mainloop()