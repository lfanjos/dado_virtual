import tkinter as tk
from random import randint
from time import time, sleep
import dice_rolling_support
from PIL import ImageTk

global img
global _img0


class Toplevel1:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'

        top.geometry("400x350+468+138")
        top.minsize(120, 1)
        top.maxsize(2906, 845)
        top.resizable(0, 0)
        top.title("Toplevel 0")
        top.configure(background="#ffffff")

        self.top = top

        self.title_lbl = tk.Label(self.top)
        self.title_lbl.place(relx=0.0, rely=0.0, height=41, width=404)
        self.title_lbl.configure(background="#d9d9d9")
        self.title_lbl.configure(compound='left')
        self.title_lbl.configure(disabledforeground="#a3a3a3")
        self.title_lbl.configure(font="-family {Segoe UI} -size 24 -weight bold")
        self.title_lbl.configure(foreground="#000000")
        self.title_lbl.configure(text='''Dado Virtual''')

        self.dice_lbl = tk.Label(self.top)
        self.dice_lbl.place(relx=0.275, rely=0.143, height=211, width=194)
        self.dice_lbl.configure(anchor='w')
        self.dice_lbl.configure(background="#ffffff")
        self.dice_lbl.configure(compound='left')
        self.dice_lbl.configure(disabledforeground="#a3a3a3")
        self.dice_lbl.configure(foreground="#000000")
        photo_location = "C:\\Users\\lfanj\\PycharmProjects\\studies\\games\\dice_rolling\\face1.jpg"
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.dice_lbl.configure(image=_img0)

        self.roll_btn = tk.Button(self.top)
        self.roll_btn.place(relx=0.325, rely=0.8, height=24, width=147)
        self.roll_btn.configure(activebackground="#ececec")
        self.roll_btn.configure(activeforeground="#000000")
        self.roll_btn.configure(background="#d9d9d9")
        self.roll_btn.configure(compound='left')
        self.roll_btn.configure(disabledforeground="#a3a3a3")
        self.roll_btn.configure(foreground="#000000")
        self.roll_btn.configure(highlightbackground="#d9d9d9")
        self.roll_btn.configure(highlightcolor="black")
        self.roll_btn.configure(pady="0")
        self.roll_btn.configure(text='''Rolar Dado''')
        self.roll_btn.configure(command=self.btn_func)

    def btn_func(self):
        self.roll_btn.configure(state="disabled")
        t_end = time() + 2.5

        while time() <= t_end:
            photo_location = f"C:\\Users\\lfanj\\PycharmProjects\\studies\\games\\dice_rolling\\face{randint(1, 6)}.jpg"
            global img
            img = ImageTk.PhotoImage(file=photo_location)
            self.dice_lbl.configure(image=img)
            self.top.update()
            sleep(0.2)
        self.roll_btn.configure(state="active")


def start_up():
    dice_rolling_support.main()


if __name__ == '__main__':
    dice_rolling_support.main()
