from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
current_card = {}
to_learn = []

# ------------------------------ Load Data -------------------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ------------------------------ Random Word Generate ---------------------------------- #


def next_card():
    global to_learn, current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=f"{current_card['German']}", fill="black")
    flip_timer = window.after(3000, flip_card)


# ------------------------------Flip Card ------------------------------------------ #
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ------------------------------Remove Known Words------------------------------------- #
def is_known():
    to_learn.remove(current_card)
    data2 = pandas.DataFrame(to_learn)
    data2.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ----------------------------- User Interface ----------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="English", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))

right_image = PhotoImage(file="./images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()
