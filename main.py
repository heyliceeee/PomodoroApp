from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 # 25-minute work
SHORT_BREAK_MIN = 5 # 5-minute short break
LONG_BREAK_MIN = 20 # 20-minute long break


# UI setup
def create_window():
    """
    create a window, set a title, set the size, and set the padding
    """
    window.title("Pomodoro") # set the title of the window

window = Tk() # create a window
create_window() # call the function to create the window
window.mainloop() # continuously run the program
