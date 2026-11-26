import tkinter as tk

root = tk.Tk()
root.title("Mouse Event Tracker")
root.geometry("600x450")
root.minsize(450, 350)


status_label = tk.Label(root, text="Status: Move your mouse")
status_label.pack(pady=10)

#
coordinates_label = tk.Label(root, text="X: 0, Y: 0")
coordinates_label.pack(pady=5)


click_label = tk.Label(root, text="Mouse Event: None")
click_label.pack(pady=5)


double_clicks = 0

double_label = tk.Label(root, text="Double Clicks: 0")
double_label.pack(pady=5)


mouse_frame = tk.Frame(root, bg="lightblue")
mouse_frame.pack(fill="both", expand=True, padx=20, pady=20)


# Mouse Motion Event
def mouse_motion(event):
    coordinates_label.config(
        text=f"X: {event.x}, Y: {event.y}"
    )


# Left Click Event
def left_click(event):
    click_label.config(text="Mouse Event: Left Click")


# Double Click Event
def double_click(event):
    global double_clicks

    double_clicks += 1

    double_label.config(
        text=f"Double Clicks: {double_clicks}"
    )


# Mouse Enter Event
def mouse_enter(event):
    status_label.config(text="Status: Mouse entered the Frame")


# Mouse Leave Event
def mouse_leave(event):
    status_label.config(text="Status: Mouse left the Frame")


# Bind Events
mouse_frame.bind("<Motion>", mouse_motion)
mouse_frame.bind("<Button-1>", left_click)
mouse_frame.bind("<Double-Button-1>", double_click)
mouse_frame.bind("<Enter>", mouse_enter)
mouse_frame.bind("<Leave>", mouse_leave)

root.mainloop()