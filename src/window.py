import tkinter as tk
import os
import re
from screeninfo import get_monitors

class Window:
    def __init__(self, root, frame=None):
        self.root = root
        self.frame = frame
    
    def create(self):
             
        if self.window_status() == "open":
            return "already running"
        
        #self.root = tk.Tk()
        self.root.title("Time Boxing AI")
        self.root.configure(background="#2b4252")
        self.root.minsize(self.screen_size()['width']-300, self.screen_size()['height']-200)
        self.root.geometry("300x300+50+50")  # width x height + x + y
        #self.root.mainloop()        
    
    def window_status(self):
        # return status of window if already open or not available
        
        try:
            if 'normal' == self.frame.state():
                    return "open"
        except:
            return "closed"
            
    def screen_size(self):
        # width, height
        sizes = ""
        size_list = []
        index = 0
        size_dict = {}
        
        for monitor in get_monitors():
            sizes = str(monitor)             
        
        ########################
        # removing extra chars #
        index = sizes.index('(')
        sizes = sizes[index+1:]
        index = sizes.index(')')
        sizes = sizes[:index]
    
        size_list = sizes.split(", ")
        size_list = size_list[2:4]
        
        width = size_list[0].index("=")
        size_list[0] = size_list[0][width+1:]
        
        height = size_list[1].index("=")
        size_list[1] = size_list[1][height+1:]
        # removing extra chars #
        ########################
        
        size_dict['width'] = int(size_list[0])
        size_dict['height'] = int(size_list[1])
        
        return size_dict

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
