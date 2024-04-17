from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import datetime
import json
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("484x757")
window.configure(bg = "#FF9090")
window.title('Dear Diary - Single Page')
window.iconbitmap("Files/icon.ico")

subprocess.Popen(['python', 'sfx.py'])
with open('Files/open_temp_records.json', 'r') as fin:
    data=json.load(fin)
    
    rol=list(data.keys())
    date_1=rol[0]
    comp=False
    action_1=data[rol[0]]['action']
    day_1=data[rol[0]]['day']
    resp_a1=data[rol[0]]['resp_a']
    resp_b1=data[rol[0]]['resp_b']
    resp_c1=data[rol[0]]['resp_c']
    resp_d1=data[rol[0]]['resp_d']

    notes_1=data[rol[0]]['notes']
    hap_score_1=data[rol[0]]['score']

def close_prog():
    subprocess.Popen(['python', 'gui.py'])
    window.quit()

canvas = Canvas(
    window,
    bg = "#FF9090",
    height = 757,
    width = 484,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# ? ======================================================
# ? PAGE 1
# ? ======================================================

canvas.place(x = 0, y = 0)
image_image_0 = PhotoImage(
    file=relative_to_assets("image.png"))
image_0 = canvas.create_image(
    538.0,
    385.0,
    image=image_image_0
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
    7.0,
    9.0,
    451.0,
    757.0,
    fill="#FFF5D3",
    outline="")

canvas.create_rectangle(
    19.0,
    29.0,
    302.0,
    141.0,
    fill="#FFE5C0",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    226.9000244140625,
    443.99322509765625,
    image=image_image_1
)

# ? ======================================================
# ? DATE 1
# ? ======================================================

canvas.create_text(
    31.0,
    46.0,
    anchor="nw",
    text=date_1,
    fill="#000000",
    font=("Kite One", 32 * -1)
)

# ? ======================================================
# ? DAY 1
# ? ======================================================

canvas.create_text(
    31.0,
    85.0,
    anchor="nw",
    text=day_1,
    fill="#000000",
    font=("Kite One", 32 * -1)
)

# ? ==========================================================
# ? ==========================================================
# ! Q: HOW WAS YOUR DAY?

canvas.create_text(
    61.0,
    179.0,
    anchor="nw",
    text="How was your day?",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Answer

canvas.create_text(
    61.0,
    205.0,
    anchor="nw",
    text=resp_a1,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? ==========================================================
# ? ==========================================================
# ! Q: WHY IS THAT?

canvas.create_text(
    58.0,
    250.0,
    anchor="nw",
    text="Why is that?",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Answer

canvas.create_text(
    58.0,
    276.0,
    anchor="nw",
    text=resp_b1,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? ==========================================================
# ? ==========================================================
# ! Q: Did you do (insert action that makes you happy)?

canvas.create_text(
    58.0,
    321.0,
    anchor="nw",
    text=f"Did you do {action_1}",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Answer

canvas.create_text(
    58.0,
    347.0,
    anchor="nw",
    text=resp_c1,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? ==========================================================
# ? ==========================================================
# ! Q: How much water did you have today? approx

canvas.create_text(
    58.0,
    392.0,
    anchor="nw",
    text="How much water did you have today? approx",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Answer

canvas.create_text(
    58.0,
    418.0,
    anchor="nw",
    text=resp_d1,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? ==========================================================
# ? ==========================================================
# ! Q: Notes
la1 = la2 = la3 = la4 = la5 = ''  # default value for each variable
segments = []
segment_length = 88

# Split the string into segments of length 88 characters
for i in range(0, len(notes_1), segment_length):
    segments.append(notes_1[i:i+segment_length])

# Assign segments to variables lb1, lb2, lb3, lb4, lb5
if len(segments) >= 1:
    la1 = segments[0]
if len(segments) >= 2:
    la2 = '-'+segments[1]
if len(segments) >= 3:
    la3 = '-'+segments[2]
if len(segments) >= 4:
    la4 = '-'+segments[3]
if len(segments) >= 5:
    la5 = '-'+segments[4]

canvas.create_text(
    58.0,
    461.0,
    anchor="nw",
    text="Notes:",
    fill="#000000",
    font=("Just Another Hand", 24 * -1)
)

# ? Notes Line - 1

canvas.create_text(
    58.0,
    485.0,
    anchor="nw",
    text=la1,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Notes Line - 2

canvas.create_text(
    58.0,
    510.0,
    anchor="nw",
    text=la2,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Notes Line - 3

canvas.create_text(
    58.0,
    534.0,
    anchor="nw",
    text=la3,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Notes Line - 4

canvas.create_text(
    58.0,
    558.0,
    anchor="nw",
    text=la4,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Notes Line - 5

canvas.create_text(
    58.0,
    580.0,
    anchor="nw",
    text=la5,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? ==========================================================
# ? ==========================================================
# ! Q: Overall Happiness Scores

canvas.create_text(
    56.0,
    626.0,
    anchor="nw",
    text="Overall Happiness score:",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Score

canvas.create_text(
    61.0,
    651.0,
    anchor="nw",
    text=f"{hap_score_1}/10",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? ==========================================================
# ? ==========================================================
# ! Q: HOLES 1

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    465.26666259765625,
    221.0440673828125,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    465.26666259765625,
    360.501708984375,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    465.26666259765625,
    499.9593200683594,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("return.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: close_prog,
    relief="flat"
)
button_1.place(
    x=318.0,
    y=39,
    width=79.24000549316406,
    height=22.22315788269043
)

window.resizable(False, False)
window.mainloop()