import pyautogui
import time

from tkinter import *


# time.sleep(10)
# print(pyautogui.position())

def coutdown():
    window = Tk()
    window.geometry('500x500')
    window.wm_attributes('-topmost', 'true')
    window.wm_overrideredirect(1)
    window.wm_attributes("-transparentcolor", "white")
    # window.wm_attributes("-disabled", True)
    text = Text(window, font=("Helvetica", 300), )

    count = 10
    for i in range(0, 10):
        count -= 1
        text.insert(INSERT, str(count))
        text.pack()
        time.sleep(1)
        window.update()
        text.delete(1.0, END)

    window.destroy()


while True:
    # print(pyautogui.size())
    time.sleep(5)
    pyautogui.moveTo(416, 318, 2)
    time.sleep(4)
    pyautogui.click()
    pyautogui.moveTo(795, 721, 2)
    time.sleep(4)
    pyautogui.click()
    time.sleep(1200)

    coutdown()
