import tkinter as tk

root = tk.Tk()
root.title("Keyboard Event Viewer")
root.geometry("500x350")

key_label = tk.Label(root, text="Last Key: None", font=("Arial", 14))
key_label.pack(pady=15)

status_label = tk.Label(root, text="Status: Ready", font=("Arial", 11))
status_label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=15)

def key_pressed(event):
    key_label.config(text=f"Key: {event.keysym} | Character: {event.char}")

def clear_display(event):
    key_label.config(text="Last Key: None")
    status_label.config(text="Status: Cleared")

def save_status(event):
    status_label.config(text="Status: Saved")

root.bind("<KeyPress>", key_pressed)
root.bind("<Escape>", clear_display)
root.bind("<Control-s>", save_status)

root.mainloop()