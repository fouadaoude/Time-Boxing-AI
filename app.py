from window import Window
from frame import Frame
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    window = Window(root=root)
    window.create()
    #welcome = Frame(root).welcome()
    frame = Frame(root).home()
    root.mainloop()
"""ss"""