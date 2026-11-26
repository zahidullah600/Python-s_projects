import tkinter as tk

root = tk.Tk()
root.title("Notes Editor")
root.geometry("600x450")
root.minsize(400, 300)

# Header Frame
header = tk.Frame(root, bg="lightblue")
header.pack(fill="x")

title = tk.Label(
    header,
    text="My Notes Editor",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
title.pack(pady=10)

# Main Text Editor
text_area = tk.Text(root, wrap="word")
text_area.pack(fill="both", expand=True, padx=10, pady=10)

# Action Frame
action_frame = tk.Frame(root)
action_frame.pack(fill="x", padx=10, pady=5)

# Status Label
status = tk.Label(root, text="Status: Ready", anchor="w")
status.pack(fill="x", padx=10, pady=5)


# Clear Function
def clear_text():
    text_area.delete("1.0", tk.END)
    status.config(text="Status: Notes cleared")


# Insert Sample Text Function
def insert_sample():
    text_area.delete("1.0", tk.END)

    sample = "Welcome to Notes Editor!\nThis is sample text."
    text_area.insert("1.0", sample)

    status.config(text="Status: Sample text inserted")


# Disable / Enable Function
def toggle_text():
    if text_area.cget("state") == "normal":
        text_area.config(state="disabled")
        toggle_button.config(text="Enable")
        status.config(text="Status: Editing disabled")
    else:
        text_area.config(state="normal")
        toggle_button.config(text="Disable")
        status.config(text="Status: Editing enabled")


# Clear Button
clear_button = tk.Button(
    action_frame,
    text="Clear",
    command=clear_text
)
clear_button.pack(side="left", padx=5)

# Insert Sample Text Button
sample_button = tk.Button(
    action_frame,
    text="Insert Sample Text",
    command=insert_sample
)
sample_button.pack(side="left", padx=5)

# Disable / Enable Button
toggle_button = tk.Button(
    action_frame,
    text="Disable",
    command=toggle_text
)
toggle_button.pack(side="left", padx=5)

root.mainloop()