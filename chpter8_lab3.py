import tkinter as tk

root = tk.Tk()
root.title("Bouncing Ball")
root.geometry("600x450")

canvas_width = 500
canvas_height = 350

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack(pady=10)

ball = canvas.create_oval(50, 50, 90, 90, fill="red")

dx = 4
dy = 4
running = False
delay = 30

def move_ball():
    global dx, dy

    if running:
        x1, y1, x2, y2 = canvas.coords(ball)

        if x1 <= 0 or x2 >= canvas_width:
            dx = -dx

        if y1 <= 0 or y2 >= canvas_height:
            dy = -dy

        canvas.move(ball, dx, dy)
        root.after(delay, move_ball)

def start_ball():
    global running

    if not running:
        running = True
        move_ball()

def pause_ball():
    global running
    running = False

def reset_ball():
    global running, dx, dy, delay

    running = False
    dx = 4
    dy = 4
    delay = 30

    canvas.coords(ball, 50, 50, 90, 90)

def faster():
    global dx, dy

    if dx > 0:
        dx += 1
    else:
        dx -= 1

    if dy > 0:
        dy += 1
    else:
        dy -= 1

def slower():
    global dx, dy

    if abs(dx) > 1:
        dx = dx - 1 if dx > 0 else dx + 1

    if abs(dy) > 1:
        dy = dy - 1 if dy > 0 else dy + 1

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start", command=start_ball)
start_button.pack(side="left", padx=5)

pause_button = tk.Button(button_frame, text="Pause", command=pause_ball)
pause_button.pack(side="left", padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset_ball)
reset_button.pack(side="left", padx=5)

faster_button = tk.Button(button_frame, text="Faster", command=faster)
faster_button.pack(side="left", padx=5)

slower_button = tk.Button(button_frame, text="Slower", command=slower)
slower_button.pack(side="left", padx=5)

root.mainloop()