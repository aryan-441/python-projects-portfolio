import math
from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
CHECKMARK = '✔'
reps = 0
timer = None

def reset_timer():
    global reps
    window.after_cancel()
    canvas.itemconfig(timer_text,text='00:00')
    title_label.config(text='Timer')
    checkmarks.config(text='')
    reps = 0
def start_timer():
    global reps
    reps += 1
    
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text='Break',fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text='Break',fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text='Work',fg=GREEN)

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    count_sec = str(count_sec).zfill(2)
    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000,countdown,count - 1)
    else:
        start_timer()
        for _ in range(math.floor(reps/2)):
            mark += '✔'
        checkmarks.config(text=mark)


window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)



title_label = Label(text='Timer',fg=GREEN, font=(FONT_NAME,50),bg=YELLOW)
title_label.grid(column=1,row=0)

start_button = Button(text='Start',highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset',highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1,row=3)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=image)
timer_text = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)






window.mainloop()