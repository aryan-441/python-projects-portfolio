'''Flash Cards App Capstone Project'''
from tkinter import *
import pandas
import random

BG_COLOUR = '#B1DDC6'
FONT_LANG = ("Arial", 40, 'italic')
FONT_WORD = ("Arial", 60, 'bold')
try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('vocab_csv.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')
current_card = {}

def next_card():
    global current_card
    if len(to_learn) == 0:
        canvas.itemconfig(card_title, text='¡Muy Bien!', fill='black')
        canvas.itemconfig(card_word, text='You cleared the list!', fill='black')
        cross_button.config(state="disabled")
        tick_button.config(state="disabled")
        return
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_background, image=card_img)
    canvas.itemconfig(card_title, text='Spanish', fill='black')
    canvas.itemconfig(card_word, text=current_card['Spanish'], fill='black')

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def known_card():
    flip_card()
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv('words_to_learn.csv', index=False)
    window.after(2000, next_card)

def unknown_card():
    flip_card()
    window.after(3500,next_card)
#Interface

window = Tk()
window.title('Flashy')
window.config(padx=50,pady=50,bg=BG_COLOUR)
window.state('zoomed')

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

main_frame = Frame(window, bg=BG_COLOUR, padx=50, pady=50)
main_frame.grid(row=0, column=0)

canvas = Canvas(main_frame,width=800, height=526, bg=BG_COLOUR, highlightthickness=0)

card_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_img)
card_title = canvas.create_text(400, 150, text='', font=FONT_LANG)
card_word = canvas.create_text(400, 263, text='', font=FONT_WORD)
canvas.grid(row=0, column=0, columnspan=2)


canvas.bind("<Button-1>", flip_card)

cross_button_image = PhotoImage(file='images/wrong.png')
cross_button = Button(main_frame,image=cross_button_image, highlightthickness=0, command=unknown_card)
cross_button.grid(row=1,column=0)

tick_button_image = PhotoImage(file='images/right.png')
tick_button = Button(main_frame,image=tick_button_image, highlightthickness=0, command=known_card)
tick_button.grid(row=1,column=1)

next_card()

window.mainloop()