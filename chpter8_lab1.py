

import tkinter as tk

root = tk.Tk()
root.title("Mouse Drawing Pad")
root.geometry("600x500")

brush_size = 5

coordinates_label = tk.Label(root, text="X: 0, Y: 0")
coordinates_label.pack(pady=5)

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True, padx=10, pady=10)

def draw(event):
    x = event.x
    y = event.y

    coordinates_label.config(text=f"X: {x}, Y: {y}")

    canvas.create_oval(
        x - brush_size,
        y - brush_size,
        x + brush_size,
        y + brush_size,
        fill="black",
        outline="black"
    )

def erase(event):
    x = event.x
    y = event.y

    items = canvas.find_overlapping(
        x - 10, y - 10,
        x + 10, y + 10
    )

    for item in items:
        canvas.delete(item)

def clear_canvas():
    canvas.delete("all")
    coordinates_label.config(text="X: 0, Y: 0")

clear_button = tk.Button(root, text="Clear", command=clear_canvas)
clear_button.pack(pady=5)

canvas.bind("<B1-Motion>", draw)
canvas.bind("<Button-3>", erase)

root.mainloop()