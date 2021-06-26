from tkinter import *
from pyautogui import position
from keyboard import is_pressed

window = Tk()
window.geometry('600x400')
window.wm_attributes('-topmost', 'true')
text = Text(window, font=("Helvetica", 20), height=20, width=100)

click1 = ''
click2 = ''
while True:
    x, y = position()
    posStrx = str(x)
    posStry = str(y)
    mousepos = posStrx + ',' + posStry
    if is_pressed('ctrl+1'):
        click1 = mousepos
    if is_pressed('ctrl+2'):
        click2 = mousepos

    text.insert(1.0, 'Position:' + mousepos)
    text.insert(2.0, '\n' + 'Click1:' + click1)
    text.insert(3.0, '\n' + 'Click2:' + click2)
    text.pack()
    window.update()
    text.delete(1.0, END)
