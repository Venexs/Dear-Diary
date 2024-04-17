
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import json
import datetime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("633x257")
window.configure(bg = "#FF9090")
window.title('Dear Diary - Q5')
window.iconbitmap("Files/icon.ico")

today=datetime.datetime.today()
today_str=today.strftime("%Y-%m-%d")
subprocess.Popen(['python', 'sfx.py'])

with open('Files/records.json', 'r') as fin:
    data=json.load(fin)

def opens():
    notes=entry_1.get()
    if today_str not in data:
        data[today_str] = {}
    data[today_str]['notes']=notes
    
    with open('Files/records.json', 'w') as fin:
        json.dump(data, fin, indent=4)

    subprocess.Popen(['python', 'GUI/Ques_6/build/gui.py'])
    window.quit()

canvas = Canvas(
    window,
    bg = "#FF9090",
    height = 257,
    width = 633,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_0 = PhotoImage(
    file=relative_to_assets("image.png"))
image_0 = canvas.create_image(
    538.0,
    385.0,
    image=image_image_0
)
canvas.create_rectangle(
    9.0,
    7.0,
    624.0,
    250.0,
    fill="#FFF5D3",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    316.0,
    133.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=40.0,
    y=73.0,
    width=552.0,
    height=119.0
)

canvas.create_text(
    286.0,
    25.0,
    anchor="nw",
    text="Notes",
    fill="#000000",
    font=("Just Another Hand", 48 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=opens,
    relief="flat"
)
button_1.place(
    x=571.0,
    y=197.0,
    width=50.0,
    height=50.0
)
def back_return():
    subprocess.Popen(['python', 'GUI/Ques_4/build/gui.py'])
    window.quit()

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: back_return(),
    relief="flat"
)
button_2.place(
    x=15.0,
    y=128.0,
    width=24.0,
    height=24.0
)
window.resizable(False, False)
window.mainloop()
