from window import Window
from button import Button
import tkinter as tk
import time
import threading


class Frame:
    def __init__(self, window):
        self.root = window
    
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
            print("in", in_color, "out", out_color)
            time.sleep(0.01)
            # create increasingly paler gray colors
            frame.config(bg="#%02x%02x%02x" % (in_color[0],in_color[1] , in_color[2]))
            if out_color[0] == in_color[0] and out_color[1] == in_color[1] and out_color[2] == in_color[2]:
               print("BROKE")
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
    
    def fade_in_out(self, label, in_color=None, out_color=None, frame=None, forever=False):
        in_color_list = str(in_color)
        out_color_list = str(out_color)       

        while True:
            print(in_color, out_color)
            self.fade_label(label, in_color, out_color, frame, forever)
            
            if forever == False:
                in_color_list = list(in_color_list.strip('[]').replace('"', '').replace(' ', '').split(','))
                out_color_list = list(out_color_list.strip('[]').replace('"', '').replace(' ', '').split(','))
            
                for x in range(len(in_color_list)):
                    in_color_list[x] = int(in_color_list[x])
                    out_color_list[x] = int(out_color_list[x])
                
            print(in_color, out_color)
            if forever:
                out_color = self.get_home_color()
                in_color = [255,255,255]
            print(in_color, out_color, "SADASD")
            self.fade_label(label, out_color, in_color, frame, forever)
        
            if forever == False:    
                label.destroy()
                break
    
    def welcome(self):
        frame = tk.Frame(self.root, width=Window(self.root).screen_size()['width']-500, height=Window(self.root).screen_size()['height']-500, bg='#2b4252')
       
        welcome_label = tk.Label(frame, text="Welcome To Time Boxing A.I.", anchor='center', fg='white', bg='#2b4252', font=('Helvetica', 40))
        welcome_label.place(anchor="c", relx=.5, rely=.5)        
        frame.place(anchor="c", relx=.5, rely=.5)               
        
        self.fade_in_out(welcome_label, in_color=[43, 66, 82], out_color=[255,255,255], frame=frame)
        welcome_label2 = tk.Label(frame, text="We're Getting Things Ready For You", anchor='center', fg='white', bg='#2b4252', font=('Helvetica', 40))
        welcome_label2.place(anchor="c", relx=.5, rely=.5)
        self.fade_in_out(welcome_label2, in_color=[43, 66, 82], out_color=[255,255,255], frame=frame)
        
        #43, 66, 82
        
    def get_screen_size(self):
        width = Window(self.root).screen_size()['width']
        height = Window(self.root).screen_size()['height']
        
        return {'width': width, 'height': height}
    
    def get_window_size(self):
        height = self.root.winfo_height()
        width = self.root.winfo_width()
        
        return {'width': width, 'height': height}
    
    def get_home_color(self):
        return [34, 44, 51]
    
    def create_label_list(self):
        label_list = []
        
    
    def home(self):
        screen = self.get_screen_size()
        
        home_frame = tk.Frame(self.root, bg='#222c33')                                          
        home_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10) 
        
        left_frame = tk.Frame(home_frame, bg='#1e2f3b')
        self.fade_in_frame(home_frame, [43, 66, 82], [34, 44, 51])
        left_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10) 
        
        home_design_label = tk.Label(left_frame, text="Time Boxing A.I.", fg='#222c33',bg='#222c33', font=('Helvetica', 40))        
        home_design_label.pack(side='left', fill='both', expand=True) 
                
        label_animation = threading.Thread(target=self.fade_in_out, args=(home_design_label,[34, 44, 51], [255,255,255] , left_frame, True))
        label_animation.start()
        
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
        
        view_schedule_btn = Button(center_right_frame).create(text_var="View My Schedules", bg_color='#1e2f3b', width="30", height="3", font_color='#1e2f3b', font=('Helvetica', 12))
        create_schedule_btn = Button(center_right_frame).create(text_var="Create Schedule", bg_color='#1e2f3b', width="30", height="3", font_color='#1e2f3b',font=('Helvetica', 12))
        
        view_schedule_btn.place(relx=0.5, rely=0.2, anchor='center')
        create_schedule_btn.place(relx=0.5, rely=0.5, anchor='center')
        
        
        #self.fade_in_frame(right_frame, [34, 44, 51], [30, 47, 59]) 
        