from window import Window
import tkinter as tk
import time
import threading
import os
from database import Db

FRAMECOLOR = [43, 66, 82]

# command = lambda : controller.show_frame(Page2))

class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        self.parent = parent
        self.controller = controller
        self.home()
    
    def fade_label(self, label, current_color=None, rgb=None, frame=None, forever=False):
        original_rgb = self.get_home_color()
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        
        while True:
            time.sleep(0.000000000000001)
            # create increasingly paler gray colors     
            label.config(fg="#%02x%02x%02x" % (current_color[0],current_color[1] , current_color[2]))       
            if r == current_color[0] and g == current_color[1] and b == current_color[2]:
                if forever:
                    while True:
                        if current_color == original_rgb:
                            break
                        
                        if current_color[0] > original_rgb[0]:
                            current_color[0]-=1
                        if current_color[1] > original_rgb[1]:
                            current_color[1]-=1
                        if current_color[2] > original_rgb[2]:
                            current_color[2]-=1
                        label.config(fg="#%02x%02x%02x" % (current_color[0],current_color[1] , current_color[2]))
                break
            
            if current_color[0] < r:
                current_color[0]+=1
            else:
                current_color[0]-=1
                
            if current_color[1]!=g:
                if current_color[1] < g:
                    current_color[1]+=1
                else:
                    current_color[1]-=1
                
            if current_color[2]!= b:
                if current_color[2] < b:
                    current_color[2]+=1
                else:
                    current_color[2]-=1
            
            frame.update()      
    
    def fade_in_frame(self, frame, in_color=None, out_color=None):        
        
        while True:
            time.sleep(0.01)
            # create increasingly paler gray colors
            frame.config(bg="#%02x%02x%02x" % (in_color[0],in_color[1] , in_color[2]))
            if out_color[0] == in_color[0] and out_color[1] == in_color[1] and out_color[2] == in_color[2]:
               break 
            
            if in_color[0] < out_color[0]:
                in_color[0]+=1
            elif in_color[0] > out_color[0]:
                in_color[0]-=1
            
            if in_color[1] < out_color[1]:
                in_color[1]+=1
            elif in_color[1] > out_color[1]:
                in_color[1]-=1
                
            if in_color[2] < out_color[2]:
                in_color[2]+=1
            elif in_color[2] > out_color[2]:
                in_color[2]-=1
            
            frame.update()
    
    # in_color is the current color of the frame and out_color is the desired color to be faded into
    def fade_out_frame(self, frame, in_color=None, out_color=None, destroy=False):
        self.forever = False
        while True:
            if out_color[0] == in_color[0] and out_color[1] == in_color[1] and out_color[2] == in_color[2]:
               break 
           
            time.sleep(0.000001)            
           
            frame.config(bg="#%02x%02x%02x" % (in_color[0], in_color[1], in_color[2]))
            
            if in_color[0] < out_color[0]:
                in_color[0]+=1
            elif in_color[0] > out_color[0]:
                in_color[0]-=1
            
            if in_color[1] < out_color[1]:
                in_color[1]+=1
            elif in_color[1] > out_color[1]:
                in_color[1]-=1
                
            if in_color[2] < out_color[2]:
                in_color[2]+=1
            elif in_color[2] > out_color[2]:
                in_color[2]-=1
            
            frame.update()
    
    def fade_in_out(self, label, in_color=None, out_color=None, frame=None, forever=False):
        in_color_list = str(in_color)
        out_color_list = str(out_color)       

        while True:
            
            self.fade_label(label, in_color, out_color, frame, forever)
            
            if forever == False:
                in_color_list = list(in_color_list.strip('[]').replace('"', '').replace(' ', '').split(','))
                out_color_list = list(out_color_list.strip('[]').replace('"', '').replace(' ', '').split(','))
            
                for x in range(len(in_color_list)):
                    in_color_list[x] = int(in_color_list[x])
                    out_color_list[x] = int(out_color_list[x])
                
            if forever:
                out_color = self.get_home_color()
                in_color = [255,255,255]
            
            self.fade_label(label, out_color, in_color, frame, forever)
        
            if forever == False:    
                label.destroy()
                break
    
    def welcome(self):
        frame = tk.Frame(self, width=Window(self).screen_size()['width']-500, height=Window(self).screen_size()['height']-500, bg='#2b4252')
       
        welcome_label = tk.Label(frame, text="Welcome To Time Boxing A.I.", anchor='center', fg='white', bg='#2b4252', font=('Helvetica', 40))
        welcome_label.place(anchor="c", relx=.5, rely=.5)        
        frame.place(anchor="c", relx=.5, rely=.5)               
        
        self.fade_in_out(welcome_label, in_color=[43, 66, 82], out_color=[255,255,255], frame=frame)
        welcome_label2 = tk.Label(frame, text="We're Getting Things Ready For You", anchor='center', fg='white', bg='#2b4252', font=('Helvetica', 40))
        welcome_label2.place(anchor="c", relx=.5, rely=.5)
        self.fade_in_out(welcome_label2, in_color=[43, 66, 82], out_color=[255,255,255], frame=frame)
        
        #43, 66, 82
        
    def get_window_size(self):
        height = self.winfo_height()
        width = self.winfo_width()
        
        return {'width': width, 'height': height}
    
    def get_home_color(self):
        return [34, 44, 51]
    
    def create_label_list(self):
        label_list = []
    
    def fade_home(self, frame=[], in_color=None, out_color=None):
        for x in frame:
            self.fade_out_frame(x, in_color, out_color)    
    
    def reset_home_color(self, frame):
        frame.config(bg='#%02x%02x%02x' % (34, 44, 52))
        frame.update()
    
    def home(self):
        ## Entire home page frame ##
        home_frame = tk.Frame(self, bg='#222c33')                                          
        home_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10) 

        home_frame.config(bg='#222c33')
        
        #self.reset_home_color(home_frame)
        
        ## Frame for the fading logo ##
        left_frame = tk.Frame(home_frame, bg='#1e2f3b')
        self.fade_in_frame(home_frame, [43, 66, 82], [34, 44, 51])
        left_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10) 

        ## Fades in entire frame on start up ##
        
        home_design_label = tk.Label(left_frame, text="Time Boxing A.I.", fg='#222c33',bg='#222c33', font=('Helvetica', 40))        
        home_design_label.pack(side='left', fill='both', expand=True) 
        
        self.forever = True
        ## Fades the logo in and out on a loop forever ##
        label_animation = threading.Thread(target=self.fade_in_out, args=(home_design_label,[34, 44, 51], [255,255,255] , left_frame, lambda:self.forever))
        label_animation.start()
        
        ## Frame for schedule options ##
        right_frame = tk.Frame(home_frame, bg='#1e2f3b')
        right_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
        top_right_frame = tk.Frame(right_frame, bg='#1e2f3b')
        top_right_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)
        center_right_frame = tk.Frame(right_frame, bg='#1e2f3b')
        center_right_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)
        bottom_right_frame = tk.Frame(right_frame, bg='#1e2f3b')
        bottom_right_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)
        
        time_to_get_better_label = tk.Label(top_right_frame, text="It's Time To Get Better.", fg="white", bg="#1e2f3b", font=('Helvetica', 20))
        time_to_get_better_label.place(relx=0.5, rely=0.5, anchor='center')
        
        view_schedule_btn = tk.Button(center_right_frame, text="View My Schedules", compound='c',
                                        highlightcolor='#1e2f3b', width="35", height="4", foreground='#1e2f3b', font=('Helvetica', 12),
                                        command=lambda:self.controller.show_frame(Schedule))                                        
        create_schedule_btn = tk.Button(center_right_frame, text="Create Schedule", compound='c',
                                      highlightcolor='#1e2f3b', width="35", height="4", foreground='#1e2f3b', font=('Helvetica', 12))        
        
        view_schedule_btn.place(relx=0.5, rely=0.2, anchor='center')
        create_schedule_btn.place(relx=0.5, rely=0.5, anchor='center')
        

class Schedule(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.view()
    
    def day(self):
        pass
    
    def week(self):
        pass
    
    def month(self):
        pass
        
    def change_frame_color(self):
        self.config(background='#222c33')
    
    def back_home(self):
        self.controller.show_frame(StartPage)
    
    def view(self):        
        self.change_frame_color()
        
        back_btn = tk.Button(self.controller, text="Back",highlightcolor='#1e2f3b', width="10", height="2", foreground='#1e2f3b', 
                             font=('Helvetica', 12), command=lambda:self.back_home())
        back_btn.place(relx=0, rely=0)
        
        db = Db()
        
        
        