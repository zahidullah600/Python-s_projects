import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Student Preferences Form")
root.geometry("550x700")

name_frame = tk.LabelFrame(root, text="Student Information")
name_frame.pack(fill="x", padx=15, pady=10)

name_label = tk.Label(name_frame, text="Student Name")
name_label.pack(anchor="w", padx=10, pady=5)

name_entry = tk.Entry(name_frame)
name_entry.pack(fill="x", padx=10, pady=5)

department_label = tk.Label(name_frame, text="Department")
department_label.pack(anchor="w", padx=10, pady=5)

department_combo = ttk.Combobox(
    name_frame,
    values=["Computer Science", "Software Engineering",
            "Information Technology", "Information Systems"],
    state="readonly"
)
department_combo.pack(fill="x", padx=10, pady=5)

study_frame = tk.LabelFrame(root, text="Study Mode")
study_frame.pack(fill="x", padx=15, pady=10)

study_var = tk.StringVar(value="Online")

tk.Radiobutton(study_frame, text="Online", variable=study_var, value="Online").pack(anchor="w", padx=10)

tk.Radiobutton(study_frame, text="On Campus", variable=study_var, value="On Campus").pack(anchor="w", padx=10)

tk.Radiobutton(study_frame, text="Hybrid", variable=study_var, value="Hybrid").pack(anchor="w", padx=10)

communication_frame = tk.LabelFrame(root, text="Communication Preferences")
communication_frame.pack(fill="x", padx=15, pady=10)

email_var = tk.BooleanVar()
phone_var = tk.BooleanVar()
sms_var = tk.BooleanVar()

tk.Checkbutton(communication_frame, text="Email", variable=email_var).pack(anchor="w", padx=10)

tk.Checkbutton(communication_frame, text="Phone", variable=phone_var).pack(anchor="w", padx=10)

tk.Checkbutton(communication_frame, text="SMS", variable=sms_var).pack(anchor="w", padx=10)

experience_frame = tk.LabelFrame(root, text="Programming Experience")
experience_frame.pack(fill="x", padx=15, pady=10)

experience_scale = tk.Scale(
    experience_frame,
    from_=0,
    to=10,
    orient="horizontal",
    label="Experience Level"
)
experience_scale.set(5)
experience_scale.pack(fill="x", padx=10)

skills_frame = tk.LabelFrame(root, text="Programming Skills")
skills_frame.pack(fill="x", padx=15, pady=10)

skills_list = tk.Listbox(skills_frame, selectmode="multiple", height=6)

skills = ["Python", "Java", "C++", "JavaScript",
          "HTML/CSS", "SQL", "C#", "PHP"]

for skill in skills:
    skills_list.insert(tk.END, skill)

skills_list.pack(fill="x", padx=10, pady=5)

summary_frame = tk.LabelFrame(root, text="Student Summary")
summary_frame.pack(fill="both", expand=True, padx=15, pady=10)

summary_text = tk.Text(summary_frame, height=7, state="disabled")
summary_text.pack(fill="both", expand=True, padx=10, pady=5)

status_label = tk.Label(root, text="Status: Ready")
status_label.pack(pady=5)

def show_summary():
    name = name_entry.get().strip()
    department = department_combo.get()

    selected_skills = skills_list.curselection()
    skill_names = [skills_list.get(i) for i in selected_skills]

    communication = []

    if email_var.get():
        communication.append("Email")

    if phone_var.get():
        communication.append("Phone")

    if sms_var.get():
        communication.append("SMS")

    if name == "":
        status_label.config(text="Please enter student name")
        return

    if department == "":
        status_label.config(text="Please select department")
        return

    if len(skill_names) == 0:
        status_label.config(text="Please select at least one skill")
        return

    if len(communication) == 0:
        communication.append("None")

    summary = (
        "Student Name: " + name +
        "\nDepartment: " + department +
        "\nStudy Mode: " + study_var.get() +
        "\nCommunication: " + ", ".join(communication) +
        "\nExperience Level: " + str(experience_scale.get()) +
        "\nSkills: " + ", ".join(skill_names)
    )

    summary_text.config(state="normal")
    summary_text.delete("1.0", tk.END)
    summary_text.insert("1.0", summary)
    summary_text.config(state="disabled")

    status_label.config(text="Status: Form Submitted Successfully")

def clear_form():
    name_entry.delete(0, tk.END)
    department_combo.set("")
    study_var.set("Online")
    email_var.set(False)
    phone_var.set(False)
    sms_var.set(False)
    experience_scale.set(5)
    skills_list.selection_clear(0, tk.END)

    summary_text.config(state="normal")
    summary_text.delete("1.0", tk.END)
    summary_text.config(state="disabled")

    status_label.config(text="Status: Form Cleared")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Submit", command=show_summary).pack(side="left", padx=10)

tk.Button(button_frame, text="Clear", command=clear_form).pack(side="left", padx=10)

root.mainloop()