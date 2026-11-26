



import tkinter as tk


root = tk.Tk()


root.title("Advanced Programming Lab")


root.geometry("500x350")

root.minsize(400, 300)

# Create a heading label
heading = tk.Label(
    root,
    text="Welcome to Advanced Programming",
    font=("Arial", 16, "bold")
)

heading.pack(pady=20)

button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")

button1.pack(pady=5)
button2.pack(pady=5)
button3.pack(pady=5)


label = tk.Label(root, text="Tkinter GUI Programming", bg="lightblue")

label.pack(fill="x", padx=10, pady=10)

# Run the application
root.mainloop()
