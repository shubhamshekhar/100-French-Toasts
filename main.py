from tkinter import *
from ReadWrite import *


BACKGROUND_COLOR = "#B1DDC6"

current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = readWrite.get_random_french_word()
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(primary_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_foreground_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(primary_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_background_img)


def on_cancel_button_click():
    pass


def is_known():
    global current_card
    readWrite.remove_word_from_dict(current_card)
    next_card()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

readWrite = ReadWrite()

canvas = Canvas(width=800, height=526)
card_foreground_img = PhotoImage(file="images/card_front.png")
card_background_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_foreground_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
primary_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_image = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_image.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_image = Button(image=check_image, highlightthickness=0, command=is_known)
known_image.grid(row=1, column=1)

next_card()

window.mainloop()
