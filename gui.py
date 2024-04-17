
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import datetime
import json
import subprocess
import threading

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1106x766")
window.configure(bg = "#FF9090")
window.title('Dear Diary - Main Page')
window.iconbitmap("Files/icon.ico")

subprocess.Popen(['python', 'sfx_1.py'])
subprocess.Popen(['python', 'sfx.py'])
today=datetime.datetime.today()
yesterday=today-datetime.timedelta(days=1)

today_str=today.strftime("%Y-%m-%d")
yestr=yesterday.strftime("%Y-%m-%d")
with open('Files/records.json', 'r') as fin:
    data=json.load(fin)
    # ! Date of Yesterday
    comp=False
    for k in data:
        if k==yestr:
            date_1=k
            comp=True
    if comp==False:
        date_1='----'
        day_1='-'
        resp_a1='-'
        resp_b1='-'
        resp_c1='-'
        resp_d1='-'

        notes_1='-'
        hap_score_1='-'
    else:
            for j in data:
                if date_1==k:
                    day_1=data[date_1]['day']
                    resp_a1=data[date_1]['resp_a']
                    resp_b1=data[date_1]['resp_b']
                    resp_c1=data[date_1]['resp_c']
                    resp_d1=data[date_1]['resp_d']

                    notes_1=data[date_1]['notes']
                    hap_score_1=data[date_1]['score']

    # ! Date of Today
    comp=False
    for k in data:
        if k==today_str:
            date_2=k
            comp=True
    if comp==False:
        date_2='----'
        day_2='-'
        resp_a2='-'
        resp_b2='-'
        resp_c2='-'
        resp_d2='-'

        notes_2='-'
        hap_score_2='-'
    else:
        for j in data:
            if date_2==k:
                day_2=data[date_2]['day']
                resp_a2=data[date_2]['resp_a']
                resp_b2=data[date_2]['resp_b']
                resp_c2=data[date_2]['resp_c']
                resp_d2=data[date_2]['resp_d']

                notes_2=data[date_2]['notes']
                hap_score_2=data[date_2]['score']

tim='21:00'
action='(insert)'
time_obj = datetime.datetime.strptime(tim, "%H:%M")

with open('Files/personal_info.json', 'r') as fins:
    rexs=json.load(fins)
    if 'info' not in rexs:
        subprocess.Popen(['python', 'GUI/Adv_test/build/gui.py'])
        window.destroy()
    else:
        action=rexs['info']['action']
        tim=rexs['info']['time']
        time_obj = datetime.datetime.strptime(tim, "%H:%M")

def run_at_specific_time(target_time):
    while True:
        now = datetime.datetime.now()
        if now.hour == target_time.hour and now.minute == target_time.minute:
            subprocess.Popen(['python', 'GUI/Reminder/build/gui.py'])
            break

def open_q1():
    subprocess.Popen(['python', 'sfx_1.py'])
    subprocess.Popen(['python', 'GUI/Ques_1/build/gui.py'])
    window.quit()

def open_q2():
    subprocess.Popen(['python', 'GUI/Date/build/gui.py'])
    window.quit()

def open_q3():
    subprocess.Popen(['python', 'sfx_1.py'])
    subprocess.Popen(['python', 'GUI/Adv_test/build/gui.py'])
    window.quit()

canvas = Canvas(
    window,
    bg = "#FF9090",
    height = 766,
    width = 1106,
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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    247.0,
    382.0,
    image=image_image_1
)

# ? ======================================================
# ? DATE 1
# ? ======================================================

canvas.create_text(
    39.0,
    46.0,
    anchor="nw",
    text=date_1,
    fill="#000000",
    font=("Kite One Hand", 32 * -1)
)

# ? ======================================================
# ? DAY 1
# ? ======================================================

canvas.create_text(
    39.0,
    85.0,
    anchor="nw",
    text=day_1,
    fill="#000000",
    font=("Kite One Hand", 32 * -1)
)

# ? ==========================================================
# ? ==========================================================
# ! Q: HOW WAS YOUR DAY?

canvas.create_text(
    69.0,
    179.0,
    anchor="nw",
    text="How was your day?",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Answer

canvas.create_text(
    69.0,
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
    66.0,
    250.0,
    anchor="nw",
    text="Why is that?",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Answer

canvas.create_text(
    66.0,
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
    66.0,
    321.0,
    anchor="nw",
    text=f"Did you do {action}",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Answer

canvas.create_text(
    66.0,
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
    66.0,
    392.0,
    anchor="nw",
    text="How much water did you have today? approx",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Answer

canvas.create_text(
    66.0,
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
    66.0,
    461.0,
    anchor="nw",
    text="Notes:",
    fill="#000000",
    font=("Just Another Hand", 24 * -1)
)

# ? Notes Line - 1

canvas.create_text(
    66.0,
    485.0,
    anchor="nw",
    text=la1,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Notes Line - 2

canvas.create_text(
    66.0,
    510.0,
    anchor="nw",
    text=la2,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Notes Line - 3

canvas.create_text(
    66.0,
    534.0,
    anchor="nw",
    text=la3,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Notes Line - 4

canvas.create_text(
    66.0,
    558.0,
    anchor="nw",
    text=la4,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Notes Line - 5

canvas.create_text(
    66.0,
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
    64.0,
    626.0,
    anchor="nw",
    text="Overall Happiness score:",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Score

canvas.create_text(
    69.0,
    651.0,
    anchor="nw",
    text=f"{hap_score_1}/10 ",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? ======================================================
# ? PAGE 2
# ? ======================================================

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    737.0,
    382.0,
    image=image_image_2
)

# ? ======================================================
# ? DATE 2
# ? ======================================================

canvas.create_text(
    550.0,
    46.0,
    anchor="nw",
    text=date_2,
    fill="#000000",
    font=("Kite One Hand", 32 * -1)
)

# ? ======================================================
# ? DAY 2
# ? ======================================================

canvas.create_text(
    550.0,
    85.0,
    anchor="nw",
    text=day_2,
    fill="#000000",
    font=("Kite One Hand", 32 * -1)
)

# ? ======================================================
# ? ======================================================
# ! Q: How was your day?

canvas.create_text(
    580.0,
    176.0,
    anchor="nw",
    text="How was your day?",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Answer

canvas.create_text(
    580.0,
    202.0,
    anchor="nw",
    text=resp_a2,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? ======================================================
# ? ======================================================
# ! Q: Why is that?

canvas.create_text(
    577.0,
    247.0,
    anchor="nw",
    text="Why is that?",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Answer

canvas.create_text(
    577.0,
    273.0,
    anchor="nw",
    text=resp_b2,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? ======================================================
# ? ======================================================
# ! Q: Did you do (insert action that makes you happy)

canvas.create_text(
    577.0,
    318.0,
    anchor="nw",
    text="Did you do (insert action that makes you happy)",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Answer

canvas.create_text(
    577.0,
    344.0,
    anchor="nw",
    text=resp_c2,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? ======================================================
# ? ======================================================
# ! Q: How much water did you have today? approx

canvas.create_text(
    577.0,
    389.0,
    anchor="nw",
    text="How much water did you have today? approx",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Answer

canvas.create_text(
    577.0,
    415.0,
    anchor="nw",
    text=resp_d2,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? ======================================================
# ? ======================================================
# ! Q: Notes
# Initialize variables
lb1 = lb2 = lb3 = lb4 = lb5 = ''  # default value for each variable
segments = []
segment_length = 88

# Split the string into segments of length 88 characters
for i in range(0, len(notes_2), segment_length):
    segments.append(notes_2[i:i+segment_length])

# Assign segments to variables lb1, lb2, lb3, lb4, lb5
if len(segments) >= 1:
    lb1 = segments[0]
if len(segments) >= 2:
    lb2 = '-'+segments[1]
if len(segments) >= 3:
    lb3 = '-'+segments[2]
if len(segments) >= 4:
    lb4 = '-'+segments[3]
if len(segments) >= 5:
    lb5 = '-'+segments[4]

canvas.create_text(
    577.0,
    458.0,
    anchor="nw",
    text="Notes:",
    fill="#000000",
    font=("Just Another Hand", 24 * -1)
)

# ? Notes line - 1

canvas.create_text(
    577.0,
    482.0,
    anchor="nw",
    text=lb1,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Notes line - 2

canvas.create_text(
    577.0,
    507.0,
    anchor="nw",
    text=lb2,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Notes line - 3

canvas.create_text(
    577.0,
    531.0,
    anchor="nw",
    text=lb3,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Notes line - 4

canvas.create_text(
    577.0,
    555.0,
    anchor="nw",
    text=lb4,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? Notes line - 5

canvas.create_text(
    577.0,
    577.0,
    anchor="nw",
    text=lb5,
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? ======================================================
# ? ======================================================
# ! Q: Overall Happiness score

canvas.create_text(
    576.0,
    623.0,
    anchor="nw",
    text="Overall Happiness score:",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

canvas.create_text(
    580.0,
    648.0,
    anchor="nw",
    text=f"{hap_score_2}/10",
    fill="#000000",
    font=("Just Another Hand", 20 * -1)
)

# ? ======================================================
# ? ======================================================
# ! Holes

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    491.0,
    383.0,
    image=image_image_3
)

# ? ======================================================
# ? ======================================================
# ! Writing Button

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_q1(),
    relief="flat"
)
button_1.place(
    x=981.0,
    y=71.0,
    width=118.0,
    height=511.0596008300781
)

# ? ======================================================
# ? ======================================================
# ! Reading Button

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_q2(),
    relief="flat"
)
button_2.place(
    x=1001.0,
    y=588.0,
    width=48.0,
    height=48.0
)
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_q3(),
    relief="flat"
)
button_3.place(
    x=1001.0,
    y=646.0,
    width=48.0,
    height=48.0
)
thread = threading.Thread(target=run_at_specific_time, args=(time_obj,))
thread.start()
window.resizable(False, False)
window.mainloop()
