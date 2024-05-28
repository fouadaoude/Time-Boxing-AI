import tkinter as tk

class Button:
    def __init__(self, frame):
        self.frame = frame
        
    def create(self, text_var="", side_var="", font_color="", font="", bg_color="", width="", height="", pack=False):
        btn = tk.Button(self.frame, text=text_var, compound='c',highlightbackground=bg_color, width=width, height=height, foreground=font_color,
                        font=font)
        
        if pack:
            btn.pack(side=side_var)
            
        return btn