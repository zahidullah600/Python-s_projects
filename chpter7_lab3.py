import tkinter as tk

root = tk.Tk()
root.title("Event-Driven Login Form")
root.geometry("400x300")

username_label = tk.Label(root, text="Username")
username_label.pack(pady=5)

username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

status_label = tk.Label(root, text="Status: Ready")
status_label.pack(pady=10)

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        status_label.config(text="Please fill all fields")
        return False

    return True

def login(event=None):
    if validate_login():
        status_label.config(text="Login Successful")

def clear_form(event=None):
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    status_label.config(text="Form Cleared")
    username_entry.focus_set()

def focus_in(event):
    status_label.config(text="Active: " + event.widget.winfo_name())

def focus_out(event):
    status_label.config(text="Field Focus Lost")

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=5)

username_entry.bind("<Return>", login)
password_entry.bind("<Return>", login)

username_entry.bind("<FocusIn>", focus_in)
username_entry.bind("<FocusOut>", focus_out)

password_entry.bind("<FocusIn>", focus_in)
password_entry.bind("<FocusOut>", focus_out)

root.bind("<Escape>", clear_form)

root.mainloop()