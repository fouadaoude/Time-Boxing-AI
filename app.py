from start_page import StartPage, Schedule
from database import Db
from screeninfo import get_monitors
import tkinter as tk

class App(tk.Tk):
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)  
        
        self.get_primary_screen_size()
        self.title("Time Boxing AI")
        self.minsize(self.get_primary_screen_size()['width']-300, self.get_primary_screen_size()['height']-200)
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
        sizes = {
            'monitor1':{'width':0, 'height':0, 'primary':False},
            'monitor2':{'width':0, 'height':0, 'primary':False}
        }
        size_list = []
        index = 0
        size_dict = {}
        primary = False
        size=""
        x=0
        for monitor in get_monitors():
            x+=1
            size = str(monitor)     
            
            if size[-6:-1][0] == '=':
                #primary = size[-5:-1]
                primary = True
            else:
                #primary = size[-6:-1]
                primary = False
            
            ########################
            # removing extra chars #
            index = size.index('(')
            size = size[index+1:]
            index = size.index(')')
            size = size[:index]
        
            size_list = size.split(", ")
            size_list = size_list[2:4]
            
            width = size_list[0].index("=")
            size_list[0] = size_list[0][width+1:]
            
            height = size_list[1].index("=")
            size_list[1] = size_list[1][height+1:]
            # removing extra chars #
            ########################            
            monitor = 'monitor'+str(x)
            
            sizes[monitor]['width'] = int(size_list[0])
            sizes[monitor]['height'] = int(size_list[1])
            sizes[monitor]['primary'] = primary
            
                
        
        return sizes
   
    def get_primary_screen_size(self):
        sizes = self.screen_size()
        
        for monitor, val in sizes.items():
            if val['primary'] == True:
                return val
            


app = App()
app.mainloop()
    #window = Window(root=root)
    #window.create()
    #welcome = Frame(root).welcome()
    #frame = Frame(root).home()
    #root.mainloop()
