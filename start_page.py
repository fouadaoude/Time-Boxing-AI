#MAC
from window import Window
import tkinter as tk
from tkinter import ttk
import time
import threading
import os, sys, ctypes
from database import Db
import flet as ft
import psutil
import inspect

FRAMECOLOR = [43, 66, 82]

class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        self.parent = parent
        self.controller = controller
        self.stop_thread = threading.Event()
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
    
    def updated_fade_label(self, label=None, fg=None, bg=None, stop_thread=False):
        try:
            time.sleep(0.5)
            if fg and bg and len(fg) == 3 and len(bg) == 3:     
                while True:                      
                    if self.thread_stopped() == True:                        
                        break
                    label.config(fg="#%02x%02x%02x" % (fg[0], fg[1], fg[2]))
                    if fg == bg:           
                        while True:   
                            #print(fg)     
                            if fg[0] != 255:
                                fg[0] += 1
                            if fg[1] != 255:
                                fg[1] += 1
                            if fg[2] != 255:
                                fg[2] += 1
                            
                            label.config(fg="#%02x%02x%02x" % (fg[0], fg[1], fg[2]))
                            self.update()
                            
                            if fg == [255, 255, 255]:
                                break
                    
                    # Check if RGB values in foreground are smaller than background RGB values
                    if fg[0] > bg[0]:
                        fg[0] -= 1
                    elif fg[0] < bg[0]:
                        fg[0] += 1
                    
                    if fg[1] > bg[1]:
                        fg[1] -= 1
                    elif fg[1] < bg[1]:
                        fg[1] += 1
                        
                    if fg[2] > bg[2]:
                        fg[2] -= 1    
                    elif fg[2] < bg[2]:
                        fg[2] += 1
                    
                    self.update()          
        finally:
            print("Fade Home Label Terminated")            
    
    # Returns whether the thread is True or False
    def thread_stopped(self):
        return self.stop_thread.isSet()
    
    def get_thread_id(self):
        if hasattr(self.thread, '_thread_id'):
            return self.thread._thread_id
        for id, thread_ in threading._active.items():            
            if thread_ is self.thread:
                return id
    
    def kill_thread(self):
        t_id = self.get_thread_id()      

        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(t_id, ctypes.py_object(SystemExit))   
        if res > 1:            
            ctypes.pythonapi.PyThreadState_SetAsyncExc(t_id, 0)
            print("Kill Thread Failed.")   
            
        self.stop_thread.set()
    
    def home(self):
        ## Entire home page frame ##
        home_frame = tk.Frame(self, bg='#222c33')                                          
        home_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10) 

        home_frame.config(bg='#222c33')
        
        ## Frame for the fading logo ##
        left_frame = tk.Frame(home_frame, bg='#1e2f3b')
        #self.fade_in_frame(home_frame, [43, 66, 82], [34, 44, 51])
        left_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10) 

        ## Fades in entire frame on start up ##
        
        #home_design_label = tk.Label(left_frame, text="Time Boxing A.I.", fg='#222c33',bg='#222c33', font=('Helvetica', 40))        
        home_design_label = tk.Label(left_frame, text="Time Boxing A.I.", fg='white',bg='#222c33', font=('Helvetica', 40))        
        home_design_label.pack(side='left', fill='both', expand=True)
                
        ## Fades the logo in and out on a loop until stop_thread.set() is called##
        self.thread = threading.Thread(target=self.updated_fade_label, args=(home_design_label, [255, 255, 255], [43, 66, 82]))
        self.thread.daemon = True
        self.thread.start()        
        
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
                                        command=lambda:[self.controller.show_frame(ScheduleView)])                    
        #view_schedule_btn.bind("<Button-1>", lambda event:[self.kill_thread(t)])                    
        view_schedule_btn.bind("<Button-1>", lambda event:[self.kill_thread()])
        create_schedule_btn = tk.Button(center_right_frame, text="Create Schedule", compound='c',
                                      highlightcolor='#1e2f3b', width="35", height="4", foreground='#1e2f3b', font=('Helvetica', 12),
                                      command=lambda:self.controller.show_frame(ScheduleCreate)) 
        create_schedule_btn.bind("<Button-1>", lambda event:[self.kill_thread()])               
        
        view_schedule_btn.place(relx=0.5, rely=0.2, anchor='center')
        create_schedule_btn.place(relx=0.5, rely=0.5, anchor='center')
        
class ScheduleView(tk.Frame):
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
        
        self.create_treeview()
        # back_btn to go back to main menu
        back_btn = tk.Button(self, text="Back",highlightcolor='#1e2f3b', width="10", height="2", foreground='#1e2f3b', 
                             font=('Helvetica', 12), command=lambda:[self.back_home()])
        back_btn.place(relx=0, rely=0)
                
        
        # db = Db()
        
    def create_treeview(self, tree=None):
        try:
            tree_frame = tk.Frame(self, padx=10, pady=10)
            
            db = Db()
            table = db.get_table_names('TimeBoxingAI')            
            view_schedule_tree = ttk.Treeview(tree_frame, columns=(table), show='headings', 
                                              style='unwrap.Treeview', selectmode='browse')        
            view_schedule_tree.pack(side='left', fill='both', expand=True, pady=50)
            
            for col in table:
                view_schedule_tree.column(col, minwidth=0, width=160, anchor='center', stretch='yes')
                view_schedule_tree.heading(col, text=col)
                
            tree_frame.pack(fill='both', expand=True)
            #view_schedule_tree.heading("#0", text="name")
            
        except:
            print("Something went wrong adding columns to treeview")
        else:
            print("Added Columns to Treeview Successfully.")
            
class ScheduleCreate(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        self.parent = parent
        
        self.view()
    
    def change_frame_color(self):
        self.config(background='black')
    
    def back_home(self):        
        self.controller.show_frame(StartPage)
    
    def view(self):
        self.change_frame_color()        
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # frame for entire ScheduleCreate page
        new_schedule_frame = tk.Frame(self)  
        # back_btn to go back to main menu
        back_btn = tk.Button(new_schedule_frame, text="Back",highlightcolor='#1e2f3b', width="10", height="2", foreground='#1e2f3b', 
                             font=('Helvetica', 12), command=lambda:self.back_home())
        back_btn.grid(column=0, row=0, sticky='w')        
        
        # self.create_schedule_for_frame is "for" the "for" label and radio buttons that exists in the page
        self.create_schedule_for_frame(new_schedule_frame)
        self.sleep_time_frame(new_schedule_frame)
        self.work_time_frame(new_schedule_frame)
        self.tasks_frame(new_schedule_frame)
        
        new_schedule_frame.grid(row=0, column=0, sticky='nsew')
        
    def create_schedule_for_frame(self, frame):        
        
        schedule_create_time = tk.StringVar()
        
        for_frame = tk.Frame(frame)
        
        create_schedule_for_label = tk.Label(for_frame, text="Create Schedule For:", anchor='w', justify='left', pady=20, font=('Helvetica', 15))
        create_schedule_for_label.grid(sticky='w', row=1, column=0)
        
        today_btn = tk.Radiobutton(for_frame, justify='left', anchor='w', text="Today", variable=schedule_create_time, value="today",font=('Helvetica', 15))
        today_btn.grid(sticky='w', row=1, column=1)
        
        week_btn = tk.Radiobutton(for_frame, justify='left', anchor='w', text="Week", variable=schedule_create_time, value="week",font=('Helvetica', 15))
        week_btn.grid(sticky='w', row=1, column=2)
        
        month_btn = tk.Radiobutton(for_frame, justify='left', anchor='w', text="Month", variable=schedule_create_time, value="month",font=('Helvetica', 15))
        month_btn.grid(sticky='w', row=1, column=3)
        
        year_btn = tk.Radiobutton(for_frame, justify='left', anchor='w', text="Year", variable=schedule_create_time, value="year",font=('Helvetica', 15))
        year_btn.grid(sticky='w', row=1, column=4)
                
        for_frame.grid(row=1, column=0)

    def sleep_time_frame(self, frame):
        sleep_wake_time_frame = tk.Frame(frame)
        
        wake_time_var = tk.StringVar()
        sleep_time_var = tk.StringVar()
        
        wake_time_lbl = tk.Label(sleep_wake_time_frame, text="What Time Do You Wake Up?", font=('Helvetica', 15))
        wake_time_lbl.grid(sticky='w', row=1, column=0)
        
        wake_time_entry = tk.Entry(sleep_wake_time_frame, textvariable=wake_time_var, font=('Helvetica', 15), width=6)
        wake_time_entry.grid(sticky='w', row=1, column=1)
        
        sleep_time_lbl = tk.Label(sleep_wake_time_frame, text="What Time Do You Sleep?", font=('Helvetica', 15), pady=10)
        sleep_time_lbl.grid(sticky='w', row=2, column=0)
        
        sleep_time_entry = tk.Entry(sleep_wake_time_frame, textvariable=sleep_time_var, font=('Helvetica', 15), width=6)
        sleep_time_entry.grid(sticky='w', row=2, column=1)
        
        sleep_wake_time_frame.grid(row=3, column=0, sticky='w')
  
    def work_time_frame(self, frame):
        work_time_frame = tk.Frame(frame)
        
        work_time_var = tk.StringVar()
        
        work_time_lbl = tk.Label(work_time_frame, text="What Time Do You Have Work?", font=('Helvetica', 15))
        work_time_lbl.grid(sticky='w', row=1, column=0)
        
        work_time_entry = tk.Entry(work_time_frame, textvariable=work_time_var, font=('Helvetica', 15), width=6)
        work_time_entry.grid(sticky='w', row=1, column=1)
        
        work_time_frame.grid(row=4, column=0, sticky='w')
    
    def tasks_frame(self, frame):
        tasks_frame = tk.Frame(frame)
        create_task_frame = tk.Frame(self, highlightbackground='red', highlightthickness=2, borderwidth=1)
        
        style = ttk.Style()
        style.theme_use('default')
        style.configure('My.TSpinbox', arrowsize=18)        
        
        tasks_lbl = tk.Label(tasks_frame, text="Tasks", font=('Helvetica', 15))
        tasks_lbl.grid(sticky='w', row=1, column=0)
        
        tab_control = ttk.Notebook(create_task_frame)
        
        tasks_count = tk.IntVar()
        
        tasks_count_box = ttk.Spinbox(tasks_frame, from_=0, to=10, width=6, textvariable=tasks_count, style='My.TSpinbox')         
        tasks_count_box.configure(
            command=lambda widget=tasks_count_box: self.update_tabs(tab_control, self.tasks_count(widget), create_task_frame))
        tasks_count_box.grid(sticky='e', row=1, column=1)                
        
        create_task_frame.grid(sticky='nsew', row=1, column=0)
        tasks_frame.grid(sticky='w', row=5, column=0, pady=10)
    
    # create_task(self) creates dictionary for task including the
    # name, description, importance, etc.
    def create_task(self, name, time, importance_level, description, wake_time, work_time, sleep_time):
        return {
            name:{
                "time": {"hour": time["hour"],
                         "minute": time["minute"]},
                
                "importance_level": importance_level,
                "description": description,
                "wake_time": wake_time,
                "work_time": work_time,
                "sleep_time": sleep_time
            }}
        
    def update_tabs(self, tab_control, tasks_count, frame):        
        # checks if there are any tasks and if max tab count is reached
        if tasks_count != 0 and len(tab_control.winfo_children()) != 10:
            while len(tab_control.winfo_children()) < tasks_count:
                tab = ttk.Frame(tab_control)           
                #tab.grid(sticky='nsew', row=1, column=0)     
                task_name_var = tk.StringVar()
                
                style = ttk.Style()
                style.theme_use('default')
                style.configure('My.TSpinbox', arrowsize=18)

                task_name_lbl = ttk.Label(tab, text="Task Name ", font=('Helvetica', 15))
                task_name_lbl.grid(sticky='w', row=2, column=0)
                
                task_name_entry = ttk.Entry(tab, textvariable=task_name_var, font=('Helvetica', 15), width=15)
                task_name_entry.grid(sticky='w', row=3, column=0)                
                
                task_desc_lbl = ttk.Label(tab, text="Task Description", font=('Helvetica', 15))
                task_desc_lbl.grid(sticky='w', row=4, column=0)
                
                task_desc_box = tk.Text(tab)
                task_desc_box.grid(sticky='nsew', row=5, column=0)
                                
                task_name_entry.bind("<KeyRelease>", lambda event: [tab_control.tab(tab, text=task_name_var.get())])
                
                importance_lvl_var = tk.IntVar()
                importance_frame = ttk.Frame(tab)
                importance_frame.grid(sticky='nsew', row=6, column=0, pady=10)
                
                importance_lvl_lbl = ttk.Label(importance_frame, text="Importance Level", font=('Helvetica', 15))
                importance_lvl_lbl.grid(sticky='nsew', row=0, column=0)
                
                importance_lvl_box = ttk.Spinbox(importance_frame, from_=0, to=10, width=6, textvariable=importance_lvl_var, style='My.TSpinbox')
                importance_lvl_box.grid(sticky='nsew', row=0, column=1)
                
                tab_control.grid(sticky='nsew', row=0, column=0)
                
                frame.grid_columnconfigure(0, weight=1)
                frame.grid_rowconfigure(0, weight=1)        
                
                tab_control.add(tab, text=str(tasks_count))                
        
        # deletes tabs if theres more tabs than requested
        while len(tab_control.winfo_children()) > tasks_count:
            for item in tab_control.winfo_children():
                item.destroy()
                break      
        
    # task_name_frame creates label and entry to change the name of task and tab
    def task_name_frame(self, tab_control, frame):
        print("INDEX tab",tab_control.index(tab_control.select()))
        print("TAB name", tab_control.tab(tab_control.select(), "text"))

    def tab_len(self, tab_control):
        return len(tab_control.winfo_children())
    
    def tasks_count(self, int_var):
        return int(int_var.get())        