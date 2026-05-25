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

create_window() # call the create_window function
window.mainloop() # continuously run the program
