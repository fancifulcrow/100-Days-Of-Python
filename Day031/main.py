import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
french_words_data = {}

# -------------------- CREATE NEW FLASH CARDS -------------------- #
try:
    data = pd.read_csv("data/words_to_learn")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    french_words_data = original_data.to_dict(orient="records")
else:
    french_words_data = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer

    # Stop the flip_timer if it is still running
    window.after_cancel(flip_timer)

    current_card = random.choice(french_words_data)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=flash_card_front)

    # Create a new flip_timer
    flip_timer = window.after(ms=3000, func=flip_the_card)


# -------------------- FLIP THE CARD -------------------- #
def flip_the_card():
    canvas.itemconfig(card_background, image=flash_card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# -------------------- SAVE YOUR PROGRESS -------------------- #
def is_known():
    french_words_data.remove(current_card)
    data = pd.DataFrame(french_words_data).to_csv("data/words_to_learn.csv", index=False)
    next_card()


# -------------------- CREATING THE UI -------------------- #
window = tkinter.Tk()
window.title = "Flash Card App"
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(ms=3000, func=flip_the_card)

# the right button
right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

# the wrong button
wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# flash card
canvas = tkinter.Canvas(width=800, height=526)
flash_card_front = tkinter.PhotoImage(file="images/card_front.png")
flash_card_back = tkinter.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=flash_card_front)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel,", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

next_card()

window.mainloop()