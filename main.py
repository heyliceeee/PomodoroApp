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

# UI setup
def create_window():
    """
    create a window, set a title, set the size, and set the padding
    """
    window.title("Pomodoro") # set the title of the window
    window.config(padx=100, pady=50) # set the padding of the window\
    window.config(bg=YELLOW) # set the background color of the window
def create_canvas():
    """
    create a canvas
    """
    canvas = Canvas(width=200, height=224) # create a canvas
    canvas.config(bg=YELLOW, highlightthickness=0) # set the background color of the canvas

    tomato_img = PhotoImage(file=dir_path + IMAGE) # create an image
    canvas.tomato_img = tomato_img # assign the image to a variable
    canvas.create_image(100, 112, image=tomato_img) # place the image
    canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.pack() # place the canvas

create_window() # call the function to create the window
create_canvas() # call the function to create the canvas
window.mainloop() # continuously run the program
