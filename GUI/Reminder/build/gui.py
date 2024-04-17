
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Projects\Dear Diary\GUI\Reminder\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("633x222")
window.configure(bg = "#FF9090")


canvas = Canvas(
    window,
    bg = "#FF9090",
    height = 222,
    width = 633,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    9.0,
    7.0,
    624.0,
    215.0,
    fill="#FFF5D3",
    outline="")

canvas.create_text(
    59.0,
    77.0,
    anchor="nw",
    text="Remember to input your diary today!",
    fill="#000000",
    font=("Just Another Hand", 64 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=478.0,
    y=176.0,
    width=138.0,
    height=35.0
)
window.resizable(False, False)
window.mainloop()