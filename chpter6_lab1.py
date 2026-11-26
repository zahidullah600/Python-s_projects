
import tkinter as tk

root = tk.Tk()
root.title("Student Profile Form")
root.geometry("500x450")
root.minsize(400, 350)

# Header Frame
header = tk.Frame(root, bg="lightblue")
header.pack(fill="x")

title = tk.Label(
    header,
    text="Student Profile",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
title.pack(pady=15)

# Form Frame
form = tk.Frame(root)
form.pack(fill="both", expand=True, padx=20, pady=10)

# Full Name
label1 = tk.Label(form, text="Full Name:")
label1.grid(row=0, column=0, padx=10, pady=8, sticky="w")

entry1 = tk.Entry(form)
entry1.grid(row=0, column=1, padx=10, pady=8, sticky="ew")

# Student ID
label2 = tk.Label(form, text="Student ID:")
label2.grid(row=1, column=0, padx=10, pady=8, sticky="w")

entry2 = tk.Entry(form)
entry2.grid(row=1, column=1, padx=10, pady=8, sticky="ew")

# Email
label3 = tk.Label(form, text="Email:")
label3.grid(row=2, column=0, padx=10, pady=8, sticky="w")

entry3 = tk.Entry(form)
entry3.grid(row=2, column=1, padx=10, pady=8, sticky="ew")

# Phone
label4 = tk.Label(form, text="Phone:")
label4.grid(row=3, column=0, padx=10, pady=8, sticky="w")

entry4 = tk.Entry(form)
entry4.grid(row=3, column=1, padx=10, pady=8, sticky="ew")

# Address
label5 = tk.Label(form, text="Address:")
label5.grid(row=4, column=0, padx=10, pady=8, sticky="nw")

address = tk.Text(form, width=25, height=4)
address.grid(row=4, column=1, padx=10, pady=8, sticky="ew")

form.columnconfigure(1, weight=1)


# Save Function
def save_data():
    full_name = entry1.get()
    student_id = entry2.get()
    email = entry3.get()
    phone = entry4.get()
    student_address = address.get("1.0", tk.END).strip()

    print("Full Name:", full_name)
    print("Student ID:", student_id)
    print("Email:", email)
    print("Phone:", phone)
    print("Address:", student_address)
    print("----------------------")

    status_label.config(text="Profile saved successfully!")


# Clear Function
def clear_data():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    address.delete("1.0", tk.END)

    status_label.config(text="Form cleared!")


# Actions Frame
actions = tk.Frame(root)
actions.pack(pady=10)

save_button = tk.Button(
    actions,
    text="Save",
    command=save_data
)
save_button.pack(side="left", padx=10)

clear_button = tk.Button(
    actions,
    text="Clear",
    command=clear_data
)
clear_button.pack(side="left", padx=10)

# Status Message
status_label = tk.Label(root, text="Ready", fg="green")
status_label.pack(pady=10)

root.mainloop()