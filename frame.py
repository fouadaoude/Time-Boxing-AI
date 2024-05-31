from window import Window
import tkinter as tk
import time
import threading

FRAMECOLOR = [43, 66, 82]

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
    
    # in_color is the current color of the frame and out_color is the desired color to be faded into
    def fade_out_frame(self, frame, in_color=None, out_color=None, destroy=False):
        while True:
            if out_color[0] == in_color[0] and out_color[1] == in_color[1] and out_color[2] == in_color[2]:
               break 
           
            #time.sleep(0.000001)            
           
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
    
    # Destroys frames
    def destroy(self, frame):
        frame.destroy()
    
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
    
    def fade_home(self, frame=[], in_color=None, out_color=None):
        print("FRAME", frame[1])
        for x in frame:
            print(x)
            self.fade_out_frame(x, in_color, out_color)    
    
    def home(self):
        screen = self.get_screen_size()
        
        ## Entire home page frame ##
        home_frame = tk.Frame(self.root, bg='#222c33')                                          
        home_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10) 
        
        ## Frame for the fading logo ##
        left_frame = tk.Frame(home_frame, bg='#1e2f3b')
        ## Fades in entire frame on start up ##
        self.fade_in_frame(home_frame, [43, 66, 82], [34, 44, 51])
        left_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10) 
        
        home_design_label = tk.Label(left_frame, text="Time Boxing A.I.", fg='#222c33',bg='#222c33', font=('Helvetica', 40))        
        home_design_label.pack(side='left', fill='both', expand=True) 
        
        ## Fades the logo in and out on a loop forever ##
        label_animation = threading.Thread(target=self.fade_in_out, args=(home_design_label,[34, 44, 51], [255,255,255] , left_frame, True))
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
                                        command=lambda:[self.fade_home([
                                                        left_frame, right_frame,top_right_frame,
                                                        center_right_frame, bottom_right_frame, home_frame], 
                                                                [30, 47, 59], [43, 66, 82]),                                                                                                      
                                                        #self.fade_out_frame(home_frame, [34, 44, 51], [43, 66, 82]),                                                        
                                                        Schedule(self.root).view()])
        create_schedule_btn = tk.Button(center_right_frame, text="Create Schedule", compound='c',
                                      highlightcolor='#1e2f3b', width="35", height="4", foreground='#1e2f3b', font=('Helvetica', 12))        
        
        view_schedule_btn.place(relx=0.5, rely=0.2, anchor='center')
        create_schedule_btn.place(relx=0.5, rely=0.5, anchor='center')
        

class Schedule:
    def __init__(self, window):
        self.root = window
    
    def day(self):
        pass
    
    def week(self):
        pass
    
    def month(self):
        pass
        
    def view(self):
        print("Click")
        