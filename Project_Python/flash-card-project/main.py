from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# ---------------------------- GET DATA ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Russian_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(title_text, text="Russian", fill="black")
    canvas.itemconfig(word_text, text=current_card["Russian"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(title_text, text="Indonesia", fill="white")
    canvas.itemconfig(word_text, text=current_card["Indonesia"], fill="white")

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    learn_data = pandas.DataFrame(to_learn)
    learn_data.to_csv("data/words_to_learn.csv", index=False)
    next_word()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Create Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", font=("ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Create img for button
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Create Button
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)

next_word()


window.mainloop()