import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Settings Panel")
root.geometry("500x550")

notification_frame = tk.LabelFrame(root, text="Notifications")
notification_frame.pack(fill="x", padx=15, pady=10)

email_var = tk.BooleanVar()
sms_var = tk.BooleanVar()
desktop_var = tk.BooleanVar()

email_check = tk.Checkbutton(notification_frame, text="Email Notifications", variable=email_var)
email_check.pack(anchor="w", padx=10, pady=5)

sms_check = tk.Checkbutton(notification_frame, text="SMS Notifications", variable=sms_var)
sms_check.pack(anchor="w", padx=10, pady=5)

desktop_check = tk.Checkbutton(notification_frame, text="Desktop Notifications", variable=desktop_var)
desktop_check.pack(anchor="w", padx=10, pady=5)

theme_frame = tk.LabelFrame(root, text="Theme")
theme_frame.pack(fill="x", padx=15, pady=10)

theme_var = tk.StringVar(value="System")

tk.Radiobutton(theme_frame, text="Light", variable=theme_var, value="Light").pack(anchor="w", padx=10)

tk.Radiobutton(theme_frame, text="Dark", variable=theme_var, value="Dark").pack(anchor="w", padx=10)

tk.Radiobutton(theme_frame, text="System", variable=theme_var, value="System").pack(anchor="w", padx=10)

volume_frame = tk.LabelFrame(root, text="Notification Volume")
volume_frame.pack(fill="x", padx=15, pady=10)

volume_scale = tk.Scale(volume_frame, from_=0, to=100, orient="horizontal")
volume_scale.set(50)
volume_scale.pack(fill="x", padx=10)

language_frame = tk.LabelFrame(root, text="Language")
language_frame.pack(fill="x", padx=15, pady=10)

language_combo = ttk.Combobox(
    language_frame,
    values=["English", "Pashto", "Persian", "Arabic"],
    state="readonly"
)

language_combo.set("English")
language_combo.pack(padx=10, pady=10)

summary_label = tk.Label(root, text="Settings Summary", justify="left", anchor="w")
summary_label.pack(fill="x", padx=15, pady=10)

def save_settings():
    notifications = []

    if email_var.get():
        notifications.append("Email")

    if sms_var.get():
        notifications.append("SMS")

    if desktop_var.get():
        notifications.append("Desktop")

    if not notifications:
        notifications.append("None")

    summary = (
        "Notifications: " + ", ".join(notifications) +
        "\nTheme: " + theme_var.get() +
        "\nVolume: " + str(volume_scale.get()) +
        "\nLanguage: " + language_combo.get()
    )

    summary_label.config(text=summary)

def reset_settings():
    email_var.set(False)
    sms_var.set(False)
    desktop_var.set(False)
    theme_var.set("System")
    volume_scale.set(50)
    language_combo.set("English")
    summary_label.config(text="Settings Summary")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Save", command=save_settings).pack(side="left", padx=10)

tk.Button(button_frame, text="Reset", command=reset_settings).pack(side="left", padx=10)

root.mainloop()