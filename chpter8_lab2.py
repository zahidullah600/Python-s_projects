import tkinter as tk

root = tk.Tk()
root.title("Keyboard-Controlled Player")
root.geometry("600x450")

canvas_width = 500
canvas_height = 350
speed = 10

coordinates_label = tk.Label(root, text="X: 50, Y: 50")
coordinates_label.pack(pady=5)

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack(pady=10)

player = canvas.create_rectangle(50, 50, 90, 90, fill="blue")

def move_player(event):
    global speed

    if event.keysym == "Shift_L" or event.keysym == "Shift_R":
        speed = 20
        return

    x1, y1, x2, y2 = canvas.coords(player)

    dx = 0
    dy = 0

    if event.keysym == "Up":
        dy = -speed
    elif event.keysym == "Down":
        dy = speed
    elif event.keysym == "Left":
        dx = -speed
    elif event.keysym == "Right":
        dx = speed

    if x1 + dx >= 0 and x2 + dx <= canvas_width:
        if y1 + dy >= 0 and y2 + dy <= canvas_height:
            canvas.move(player, dx, dy)

    x1, y1, x2, y2 = canvas.coords(player)
    coordinates_label.config(text=f"X: {x1}, Y: {y1}")

def reset_player(event):
    canvas.coords(player, 50, 50, 90, 90)
    coordinates_label.config(text="X: 50, Y: 50")

def normal_speed(event):
    global speed
    speed = 10

root.bind("<KeyPress>", move_player)
root.bind("<KeyRelease-Shift_L>", normal_speed)
root.bind("<KeyRelease-Shift_R>", normal_speed)
root.bind("r", reset_player)
root.bind("R", reset_player)

root.mainloop()