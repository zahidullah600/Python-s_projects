

import tkinter as tk

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x300")
root.minsize(350, 280)

label1 = tk.Label(root, text="Student ID:")
label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)


label2 = tk.Label(root, text="Name:")
label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)


label3 = tk.Label(root, text="Department:")
label3.grid(row=2, column=0, padx=10, pady=10, sticky="w")

entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=10)

# Semester
label4 = tk.Label(root, text="Semester:")
label4.grid(row=3, column=0, padx=10, pady=10, sticky="w")

entry4 = tk.Entry(root)
entry4.grid(row=3, column=1, padx=10, pady=10)



def save_data():
    student_id = entry1.get()
    name = entry2.get()
    department = entry3.get()
    semester = entry4.get()

    print("Student ID:", student_id)
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("----------------------")



def clear_data():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)



save_button = tk.Button(root, text="Save", command=save_data)
save_button.grid(row=4, column=0, padx=10, pady=15)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_data)
clear_button.grid(row=4, column=1, padx=10, pady=15)

# Run the application
root.mainloop()