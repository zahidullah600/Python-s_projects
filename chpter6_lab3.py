import tkinter as tk

root = tk.Tk()
root.title("Image Profile Card")
root.geometry("400x450")
root.minsize(350, 400)


profile_frame = tk.Frame(root, bg="lightgray", padx=20, pady=20)
profile_frame.pack(padx=20, pady=20, fill="both", expand=True)


profile_image = tk.PhotoImage(file="profile.png")

image_label = tk.Label(profile_frame, image=profile_image, bg="lightgray")
image_label.pack(pady=10)


name_label = tk.Label(
    profile_frame,
    text="Ahmad Khan",
    font=("Arial", 16, "bold"),
    bg="lightgray"
)
name_label.pack(pady=5)


department_label = tk.Label(
    profile_frame,
    text="Department: Computer Science",
    font=("Arial", 11),
    bg="lightgray"
)
department_label.pack(pady=5)


email_label = tk.Label(
    profile_frame,
    text="Email: ahmad@example.com",
    font=("Arial", 10),
    bg="lightgray"
)
email_label.pack(pady=5)



def edit_profile():
    name_label.config(text="Name: Edit Mode")
    department_label.config(text="Department: Edit Mode")
    email_label.config(text="Email: Edit Mode")


edit_button = tk.Button(
    profile_frame,
    text="Edit",
    command=edit_profile
)
edit_button.pack(pady=10)


close_button = tk.Button(
    profile_frame,
    text="Close",
    command=root.destroy
)
close_button.pack(pady=5)

root.mainloop()