import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    department TEXT NOT NULL,
    semester TEXT NOT NULL
)
""")

conn.commit()

root = tk.Tk()
root.title("Student CRUD System")
root.geometry("850x600")

selected_id = None
record_ids = []

form_frame = tk.LabelFrame(root, text="Student Information")
form_frame.pack(fill="x", padx=10, pady=10)

tk.Label(form_frame, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Email").grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Department").grid(row=2, column=0, padx=10, pady=5)

department_combo = ttk.Combobox(
    form_frame,
    values=["Computer Science", "Software Engineering",
            "Information Technology", "Information Systems"],
    state="readonly",
    width=27
)
department_combo.grid(row=2, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Semester").grid(row=3, column=0, padx=10, pady=5)

semester_combo = ttk.Combobox(
    form_frame,
    values=["1", "2", "3", "4", "5", "6", "7", "8"],
    state="readonly",
    width=27
)
semester_combo.grid(row=3, column=1, padx=10, pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

search_frame = tk.LabelFrame(root, text="Search Students")
search_frame.pack(fill="x", padx=10, pady=5)

search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side="left", padx=10, pady=5)

list_frame = tk.LabelFrame(root, text="Student Records")
list_frame.pack(fill="both", expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

student_list = tk.Listbox(
    list_frame,
    yscrollcommand=scrollbar.set,
    height=12
)
student_list.pack(fill="both", expand=True, padx=5, pady=5)

scrollbar.config(command=student_list.yview)

def refresh_list(search=""):
    global record_ids

    student_list.delete(0, tk.END)
    record_ids = []

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ? ORDER BY id",
        ("%" + search + "%",)
    )

    records = cursor.fetchall()

    for record in records:
        record_ids.append(record[0])

        display_text = (
            f"ID: {record[0]} | Name: {record[1]} | "
            f"Email: {record[2]} | Department: {record[3]} | "
            f"Semester: {record[4]}"
        )

        student_list.insert(tk.END, display_text)

def clear_form():
    global selected_id

    selected_id = None
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    department_combo.set("")
    semester_combo.set("")
    student_list.selection_clear(0, tk.END)

def save_student():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    department = department_combo.get()
    semester = semester_combo.get()

    if not name or not email or not department or not semester:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        cursor.execute(
            "INSERT INTO students (name, email, department, semester) "
            "VALUES (?, ?, ?, ?)",
            (name, email, department, semester)
        )

        conn.commit()
        refresh_list()
        clear_form()

        messagebox.showinfo("Success", "Student saved successfully!")

    except sqlite3.IntegrityError:
        conn.rollback()
        messagebox.showerror("Error", "Email already exists!")

def select_student(event):
    global selected_id

    selection = student_list.curselection()

    if not selection:
        return

    index = selection[0]
    selected_id = record_ids[index]

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (selected_id,)
    )

    record = cursor.fetchone()

    if record:
        clear_form()
        selected_id = record[0]

        name_entry.insert(0, record[1])
        email_entry.insert(0, record[2])
        department_combo.set(record[3])
        semester_combo.set(record[4])

def update_student():
    if selected_id is None:
        messagebox.showerror("Error", "Select a student first!")
        return

    name = name_entry.get().strip()
    email = email_entry.get().strip()
    department = department_combo.get()
    semester = semester_combo.get()

    if not name or not email or not department or not semester:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        cursor.execute(
            "UPDATE students SET name=?, email=?, department=?, semester=? "
            "WHERE id=?",
            (name, email, department, semester, selected_id)
        )

        conn.commit()
        refresh_list()
        clear_form()

        messagebox.showinfo("Success", "Student updated successfully!")

    except sqlite3.IntegrityError:
        conn.rollback()
        messagebox.showerror("Error", "Email already exists!")

def delete_student():
    if selected_id is None:
        messagebox.showerror("Error", "Select a student first!")
        return

    answer = messagebox.askyesno(
        "Confirmation",
        "Are you sure you want to delete this student?"
    )

    if answer:
        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (selected_id,)
        )

        conn.commit()
        refresh_list()
        clear_form()

        messagebox.showinfo("Success", "Student deleted successfully!")

def search_student():
    refresh_list(search_entry.get().strip())

def show_all():
    search_entry.delete(0, tk.END)
    refresh_list()

tk.Button(button_frame, text="Save", command=save_student).pack(side="left", padx=5)

tk.Button(button_frame, text="Update", command=update_student).pack(side="left", padx=5)

tk.Button(button_frame, text="Delete", command=delete_student).pack(side="left", padx=5)

tk.Button(button_frame, text="Clear", command=clear_form).pack(side="left", padx=5)

tk.Button(search_frame, text="Search", command=search_student).pack(side="left", padx=5)

tk.Button(search_frame, text="Show All", command=show_all).pack(side="left", padx=5)

student_list.bind("<<ListboxSelect>>", select_student)

refresh_list()

root.mainloop()

conn.close()