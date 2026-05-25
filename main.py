import math
import os
from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 # 25-minute work
SHORT_BREAK_MIN = 5 # 5-minute short break
LONG_BREAK_MIN = 20 # 20-minute long break

IMAGE = "/data/tomato.png"
dir_path = os.path.dirname(os.path.abspath(__file__)) # get the path of the current file

window = Tk() # create a window
reps = 0


# timer mechanism
def timer_start():
    """
    timer start
    """
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1 # increase the reps by 1

    if reps % 8 == 0: # if the reps is 8th
        countdown(long_break_sec)  # count down from 20 minutes (long break)
        timer_title_label.config(text="Break", fg=RED) # change the text of the timer label

    elif reps % 2 == 0: # if the reps is even
        countdown(short_break_sec) # count down from 5 minutes (short break)
        timer_title_label.config(text="Break", fg=PINK) # change the text of the timer label

    else: # if the reps is odd
        countdown(work_sec)  # count down from 25 minutes (work)
        timer_title_label.config(text="Work", fg=GREEN) # change the text of the timer label
def timer_reset():
    """
    timer reset
    :return:
    """
    pass

# countdown mechanism
def countdown(count):
    """
    countdown function
    :param count: countdown time
    """
    count_min = math.floor(count / 60) # calculate the minutes
    count_sec = count % 60 # calculate the seconds

    if count_sec < 10: # if the seconds are less than 10, add a leading zero
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # update the text of the timer label

    if count > 0: # if the countdown time is greater than 0
        window.after(1000, countdown, count - 1) # call the function after 1 second
    else: # if the countdown time is 0
        timer_start() # call the function to start the timer

# UI setup
def create_window():
    """
    create a window, set a title, set the size, and set the padding
    """
    window.title("Pomodoro") # set the title of the window
    window.config(padx=100, pady=50) # set the padding of the window\
    window.tk.call("tk_setPalette", YELLOW) # set the background color of the window
def create_canvas():
    """
    create a canvas
    """
    global canvas, timer_text
    tomato_img = PhotoImage(file=dir_path + IMAGE)  # create an image

    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # create a canvas
    canvas.tomato_img = tomato_img # assign the image to a variable
    canvas.create_image(100, 112, image=tomato_img) # place the image
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(column=1, row=1) # place the canvas
def create_labels():
    """
    create the labels, set the text, and place them on the window
    """
    global timer_title_label

    timer_title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW) # create the label
    timer_title_label.grid(column=1, row=0) # place the label on the window

    check_label = Label(text="✓", font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW) # create the label
    check_label.grid(column=1, row=3) # place the label on the window
def create_btns():
    """
    create the buttons, set the text, and place them on the window
    """
    start_btn = Button(text="Start", command=timer_start, bg=YELLOW, highlightthickness=0) # create the button
    start_btn.grid(column=0, row=2) # place the button on the window

    reset_btn = Button(text="Reset", command=timer_reset, bg=YELLOW, highlightthickness=0)  # create the button
    reset_btn.grid(column=2, row=2) # place the button on the window

create_window() # call the function to create the window
create_canvas() # call the function to create the canvas
create_labels() # call the function to create the labels
create_btns() # call the function to create the buttons
window.mainloop() # continuously run the program
