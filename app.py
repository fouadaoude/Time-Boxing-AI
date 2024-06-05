from start_page import StartPage, Schedule
from database import Db
from screeninfo import get_monitors
import tkinter as tk

class App(tk.Tk):
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)  
        
        self.title("Time Boxing AI")
        self.minsize(self.screen_size()['width']-300, self.screen_size()['height']-200)
        self.geometry("300x300+50+50")  # width x height + x + y
        
        self.container.pack(side='left', fill='both', expand=True, padx=10, pady=10) 
        self.container.configure(background="#2b4252")    
        
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}  
        
        for F in (StartPage, Schedule):
            frame = F(self.container, self)
            
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky='nsew')
            
        self.show_frame(StartPage)
            
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
               
    def change_frame_color(self, frame='main', color='#2b4252'):
        if frame.lower() == 'main':
            self.config(background=color)
      
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
   

app = App()
app.mainloop()
    #window = Window(root=root)
    #window.create()
    #welcome = Frame(root).welcome()
    #frame = Frame(root).home()
    #root.mainloop()
