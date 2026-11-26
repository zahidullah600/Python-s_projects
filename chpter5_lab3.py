import tkinter as tk

root = tk.Tk()
root.title("Responsive Layout")
root.geometry("500x350")
root.minsize(350, 250)

# Header Frame
header = tk.Frame(root, bg="lightblue")
header.pack(fill="x")

header_label = tk.Label(
    header,
    text="Student Information",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
header_label.pack(pady=15)

# Content Frame
content = tk.Frame(root)
content.pack(fill="both", expand=True, padx=20, pady=20)

# Grid configuration
content.columnconfigure(1, weight=1)

# Name Label
name_label = tk.Label(content, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Name Entry
name_entry = tk.Entry(content)
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Department Label
department_label = tk.Label(content, text="Department:")
department_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Department Entry
department_entry = tk.Entry(content)
department_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Footer Frame
footer = tk.Frame(root, bg="lightgray")
footer.pack(fill="x")

footer_label = tk.Label(
    footer,
    text="Advanced Programming Lab",
    bg="lightgray"
)
footer_label.pack(pady=10)

root.mainloop()