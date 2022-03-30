import tkinter as tk
import dice_rolling


def main(*args):
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    global _top1, _w1
    _top1 = root
    _w1 = dice_rolling.Toplevel1(_top1)
    root.mainloop()


if __name__ == '__main__':
    dice_rolling.start_up()
