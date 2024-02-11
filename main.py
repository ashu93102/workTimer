import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✔"
reps = 0
timer = "00:00"
# ---------------------------- TIMER RESET ------------------------------- # 


def rest_timer():
    global timer
    window.after_cancel(timer)
    tim.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    check_box.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """This function is used to Start the timer"""
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        tim.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        countdown(long_break)
    elif reps % 2 == 0:
        tim.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        countdown(short_break)
    else:
        tim.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    """This function is used to add functionality to our canvas timer"""
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # After method of window to show countdown
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            marks += CHECK
        check_box.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

# Label Timer
tim = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
tim.grid(column=1, row=0)

# canvas creation for insert image
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# below line reads file and convert image to usable
tom_image = tkinter.PhotoImage(file="tomato.png")
# Now converted image can be used to show on canvas
canvas.create_image(100, 112, image=tom_image)
# to add text on canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

# Button Start
str_button = tkinter.Button(text="Start", bg=YELLOW, font=(FONT_NAME, 12, "bold"), highlightthickness=0,
                            command=start_timer)
str_button.grid(column=0, row=2)

# Button Reset
res_button = tkinter.Button(text="Reset", bg=YELLOW, font=(FONT_NAME, 12, "bold"), highlightthickness=0,
                            command=rest_timer)
res_button.grid(column=2, row=2)

# checkbox label
check_box = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
check_box.grid(column=1, row=3,)

window.mainloop()
