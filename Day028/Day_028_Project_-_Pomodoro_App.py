import math
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    window.after_cancel(timer)

    # reset items in the GUI
    canvas.itemconfig(timer_text, text="00:00")
    header_label.config(text="Timer")
    check_marks.config(text="")
    
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # manage when breaks happen
    if reps % 8 == 0:
        countdown(long_break_sec)
        header_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        header_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        header_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    # Expressing the time properly
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}" # dynamic typing

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # countdown loop
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            marks=""
            for _ in range(math.floor(reps/2)):
                marks += "✔"
            
            check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# display header
header_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
header_label.grid(row=0, column=1)

# display the tomato picture
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# display the timer
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)


# display start button
start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# display reset button
reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# display check marks
check_marks = tkinter.Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_marks.grid(row=2, column=1)

window.mainloop()