''' 
This program's intended use is to produce and provide
a list or type of data that will display the user a schedule
based on how long it usually takes to complete a specific
task, or how importantly ranked is it by the user to complete,
and etc.

Created by Fouad M. Aoude
'''

from prettytable import PrettyTable
from termcolor import colored
from datetime import date
from collections import defaultdict
import time
import re
import os
import calendar


morning_hours = ['12am', '1am', '2am', '3am', '4am', '5am', '6am', '7am', '8am', '9am', '10am', '11am']
afternoon_hours = ['12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm']


class Schedule:
    
    def __init__(self) -> None:
        os.system('clear')
        
        self.schedule = {}
    
    def format_time(self, time=None, meridiem=None):
        if time == None or meridiem == None:
            return None
        
        print("time -1",time)
        
        time = str(time.lower())
        time = time.replace(" ", "")
        meridiem = meridiem.lower()
        meridiem = meridiem.replace(" ", "")
        
        if meridiem[-2:] not in ['am', 'pm']:
            return None
        
        time = ''.join(filter(str.isdigit, time))
        print('time 0',time[:2])
        # check if length of time is less than 6 (Should be 5 Total with correct format)      
        if len(time) == 3:
            print('teeemy')
            if ':' not in time:
                time = '0' + time[0] + ':' + time[1:]  
                
        print(time)
                
        if len(time) < 6 and int(time[:2]) < 13:        
            # check if only the hour was entered ex -> "4" and not "10"
            if len(time) < 2:         
                print("time 1", time)                   
                time = '0' + time + ':00'
            # check if only the hour was entered ex -> "10" and not "4"
            elif len(time) == 2:
                # check if the first number is 0
                if time[0] == '0' and time[1]:
                    print("time 2", time)                   
                    # if first char is zero add the second char and add :00
                    time = time + ':00'
                # check if the first char is greater than 0 ex -> "10" and not "01"
                elif int(time[0]) > 0:                    
                    print("time 3", time)                   
                    time = time + ':00'
            # check if length of time is greater than 2 chars ex -> "10:" or "100"
            elif len(time) > 2:
                # check if third char has ":"                                                    
                if time[2] != ':':
                    print("time 4", time)                   
                    #print('timmy',time[2:])
                    # check if length of 2 chars starting from end and is less than 2                      
                    if len(time[2:]) < 3:                        
                        if int(time[:1]) > 10:
                            print("too big")
                            time = '0' + time[:1] + ':' + time[1:]    
                        #elif int(time[:1]) > 10:
                        #    time = ''
                        #if int(time[0]) < 1
                        # use whole string until 2nd index add a '0' then add the rest of the time
                        #time = time[:2] + '0' + time[2:]
                        print("time 5", time)
                        #time = time[:2] + ':' + time[2:]                                    
                        print("time 6", time)        
                    elif len(time[2:]) > 1:
                        print("time 6.5", time)        
                        time = time[:2] + ':' + time[2:]
                    
                if len(time[2:]) < 1:                    
                    time = time + '00'
                    print('time 7 ',time)            
                elif len(time[3:]) > 2:                    
                    time = time[:-1]
                    print("time 8",time[3:])            
        else:
            return None
        
        print("Good", time)
        print(len(time))

    '''
    is_valid_time() returns True if is a valid 12 hr time/format
    '''
    def is_valid_time(self, time=None):                
        if time == None:
            return False
                        
        # To check if user inputted time is valid
        time_format = "(1[012]|[1-9]):[0-5][0-9](\\s)?(am|pm)"
        
        compiled_format = re.compile(time_format)
        
        if re.search(compiled_format, time) or time in morning_hours or time in afternoon_hours:
            print("Passed",time)
            return True
        else:
            return False
         
    
    ''' 
    The purpose of get_schedule() function is to ask the user what they do on a daily and 
    also what they could do better, the importance of the task on a scale of 1-5
    '''
    def get_schedule(self):         
        
        # bed_time and wake_time hold strings for user inputted wake time and bed time
        bed_time = ''
        wake_time = ''                        
        
        ''' error handling while True loop so if user enters wrong data to re ask or restart loop. '''
        while True:
            mac_clear_terminal()       
            # Ask user for their wake up time
            # loop to handle errors for asking user wake_time
            while True:
                wake_time = input('What time do you wake up? ')
                wake_time = wake_time.lower().replace(" ", '')
                print("wake_time",wake_time)
                # not in morning_hours or afternoon_hours list and is digit and string does not include am or pm 
                if wake_time[0:1].isdigit() and wake_time[-2:] not in ['am', 'pm']:
                    # is integer and is between 1 and 12
                    if int(wake_time[0:1]) > 0 and int(wake_time[0:1]) < 13:
                        mac_clear_terminal()
                        while True:                                                                                    
                            print(colored('Wake Time: ' + wake_time, 'light_yellow'))
                            meridiem = input(colored("am or pm? ", 'light_yellow'))
                            if meridiem.lower() in ['am', 'pm']:
                                wake_time = wake_time + meridiem
                                break 
                            else:
                                mac_clear_terminal()
                                print(colored("Please enter a valid 12hr time.", 'red'))
                                
                    # is an integer but is not between 1 and 12, restart loop
                    else:                                       
                        mac_clear_terminal()                               
                        print(colored("Please enter a valid 12hr time.", 'red'))
                        continue
                # checks if the user entry is a valid time with meridiem(AM/PM)                
                if self.is_valid_time(wake_time):
                    mac_clear_terminal()
                    break      
                # if input is not a valid time or format re run loop                                
                else:                    
                    mac_clear_terminal()       
                    print(self.is_valid_time(wake_time))
                    print(colored("Please enter a valid 12hr time.", 'red'))
                    continue
            
            # loop to handle errors for asking user bed_time
            # error handling for asking user bed_time
            while True:                                       
                print(colored('Wake Time: ' + wake_time, 'green'))
                bed_time = input('What time do you go to bed? ')
                bed_time = bed_time.lower()
                bed_time = bed_time.lower().replace(" ", '')
                
                #is digit and string does not include am or pm                    
                if bed_time[0:1].isdigit() and bed_time[-2:] not in ['am', 'pm']:                    
                    mac_clear_terminal()    
                    if int(bed_time[0:1]) > 0 and int(bed_time[0:1]) < 13:
                        while True:                                                        
                            print(colored("Wake Time: " + wake_time, 'green'))
                            print(colored("\nBed Time: " + bed_time, 'light_yellow'))
                            
                            meridiem = input(colored("am or pm? ", 'light_yellow'))
                            if meridiem.lower() in ['am', 'pm']:
                                bed_time = bed_time + meridiem
                                break         
                            else:
                                mac_clear_terminal()
                                print(colored("Please enter a valid 12hr time.", 'red'))
                    # is an integer but is not between 1 and 12, restart loop
                    else:
                        mac_clear_terminal()       
                        print(colored("Please enter a valid 12hr time.", 'red'))
                        continue
                # checks if the user entry is a valid time with meridiem(AM/PM)                
                if self.is_valid_time(bed_time):
                    mac_clear_terminal()
                    break      
                # if input is not a valid time or format re run loop
                else:
                    mac_clear_terminal()       
                    print(colored("Please enter a valid 12hr time.", 'red'))
                    continue
            
            mac_clear_terminal()
            print(colored('Wake Time: ' + wake_time, 'green'))
            print(colored('Bed Time: ' + bed_time, 'green'))
            #test_dict.setdefault(1, {})[4] = 7
            #Dictionary after nesting : {1: {4: 7}}
            #print(calendar.day_name[today.weekday()])
            today = date.today()
            print("TODAY", today)
            
            curr_weekday = str(calendar.day_name[today.weekday()])
            curr_day_num = str(today)
            curr_month = str(calendar.month_name[today.month])
            
            today = curr_weekday + ', ' + curr_month + ' ' + curr_day_num[8:]
            
            self.schedule.setdefault('immutable_times', {})['wake_time'] = wake_time
            self.schedule['immutable_times']['bed_time'] = bed_time
            self.schedule.setdefault('today', {})['date'] = str(today)
            self.schedule['today']['current_time'] = time.strftime("%I:%M %p")       
            
            self.schedule['categories'] = {}
            
            break
    
    ''' 
    get_data() purpose is to get user input on new categories, tasks to get done and their level of importance
    '''
    def get_data(self):
        ''' schedule dict intention is to hold key (string) for the [categories] and another dict for value for [importance] (integer) and [task] (string) '''                  
        categories = []
        category = ""
        time_of_task = []
        tasks = []
        importance = []
        
        while True:
            mac_clear_terminal()
            today = date.today()
    
            #print(calendar.day_name[today.weekday()])
            
            num = int(input("How many categories would you like to enter? "))
            if int(num) > 5:
                print(colored("Choose a value of 5 or under", 'red'))
                continue
            else:                               
                for x in range(num):
                    category_dict = {}  
                    category = input("Please enter category #" + str(x+1) + " ")
                    task = input("Please enter task for " + colored(category, 'light_yellow') + " ")
                    # time_for_task takes data in the form of hours, i.e. 0.5 = half an hour or 1 = an hour
                    time_for_task = input("How long will this task take to complete? ")
                    # importance_lvl takes an integer 1-10 that will determine what time the task should be completed
                    importance_lvl = input("How important is this task to you? [1-10] ")            
                    
                    tasks.append(task)
                    time_of_task.append(time_for_task)
                    importance.append(importance_lvl)
                    
                    category_dict['importance_lvl'] = importance[x]
                    category_dict['time_for_task'] = time_of_task[x]
                    category_dict['task'] = tasks[x]         
                    
                    
                    if 'categories' not in self.schedule.keys():                        
                        self.schedule.setdefault('categories', {})[category] = category_dict           
                    else:                       
                        self.schedule['categories'][category] = category_dict
                
                work = ""
                while work.lower() not in ['y', 'n']:
                    work = input("Do you have work today? [y/n] ")
                    
                    if work.lower() == 'y':                    
                        start_work = ""
                        while not self.is_valid_time(start_work) and start_work != self.schedule['immutable_times']['wake_time']:
                            start_work = input("What time do you start work? ")
                        finish_work = ""
                        while not self.is_valid_time(finish_work) and finish_work != self.schedule['immutable_times']['bed_time']:
                            finish_work = input("What time do you finish work? ")
                            
                        self.schedule['immutable_times']['work'] = {
                            'scheduled' : True,
                            'start_work' : start_work,
                            'finish_work' : finish_work
                        }
                    
                    elif work.lower() == 'n':
                        self.schedule['immutable_times']['work'] = {
                            'scheduled' : False,
                            'start_work' : 'N/A',
                            'finish_work' : 'N/A'
                        }                  
                    
                mac_clear_terminal()
                self.create_table(categories=categories, tasks=tasks, importance=importance, time_of_task=time_of_task)
                print("self.schedule AFTER", self.schedule)
                break
    
    def get_todays_date(self):
        today = list(self.schedule['today'].values())[0]
        return today
    
    def create_schedule(self):
        if self.schedule:
            categories = []
            new_schedule = {}            
            
            hours_in_day = morning_hours + afternoon_hours
            
            for x in range(len(hours_in_day)):
                if hours_in_day[x] not in new_schedule.keys():
                    new_schedule[hours_in_day[x]] = ""
            
            new_schedule[self.schedule['immutable_times']['wake_time']] = 'wake_time'
            new_schedule[self.schedule['immutable_times']['bed_time']] = 'bed_time'
            
            for key, val in new_schedule.items():
                if val == 'wake_time':
                    break
                else:
                    new_schedule[key] = 'sleep'
            
            bed_time = False
            for key, val in new_schedule.items():
                if bed_time:
                    new_schedule[key] = 'sleep'
                elif val == 'bed_time':
                    bed_time = True                    
            
            importance_order = {}
            for key, val in self.schedule['categories'].items():
                for cat_key, cat_val in val.items():         
                    if cat_key == 'importance_lvl':
                        importance_order[int(cat_val)] = key
            
            importance_order = dict(sorted(importance_order.items()))
            print('self.schedule', self.schedule)
            if self.schedule['immutable_times']['work']['scheduled'] == True:
                start_work = self.schedule['immutable_times']['work']['start_work']
                finish_work = self.schedule['immutable_times']['work']['finish_work']
                for x in range(len(hours_in_day)):
                    if hours_in_day[x] == start_work:
                        while hours_in_day[x] != finish_work:                     
                            new_schedule[hours_in_day[x]] = 'work'
                            if x == len(hours_in_day):
                                break
                            x+=1
                        if hours_in_day[x] == finish_work:
                            new_schedule[hours_in_day[x]] = 'work'
            else:                    
                
                '''pos = list(new_schedule.keys()).index(self.schedule['immutable_times']['wake_time'])
                items = list(new_schedule.items())
                if self.schedule['immutable_times']['wake_time']: 
                    items.insert(pos, ('Phone', '123-456-7890'))
                    mydict = dict(items)'''
                                                                                  
            for category in self.schedule['categories'].keys():
                categories.append(category)
                
    
    def create_table(self, categories=None, tasks=None, importance=None, time_of_task=None):
        headers = []
        headers.append(self.get_todays_date())
        today_month_and_day = headers[0]
        hours_in_day = morning_hours + afternoon_hours
        print("HOURS IN DAY", hours_in_day)
        table = PrettyTable()
        
        # while the user inputted category list isnt the same list length and the amount of hours, keep looping until they are
        while len(categories) != len(hours_in_day):
            if len(categories) > len(hours_in_day):
                hours_in_day.append("")
            elif len(categories) < len(hours_in_day):
                categories.append("")
        
        
        self.create_schedule()
        
        
        
        table.add_column(today_month_and_day, hours_in_day)
        
        table.add_column('Task', categories)
        #print(self.schedule['categories'])
        print(table)

    def display_today_schedule(self, schedule):
        
        for am_hour in morning_hours:
            print(am_hour)
            print()
            

def mac_clear_terminal():
    os.system('clear')

schedule = Schedule()
schedule.get_schedule()
schedule.get_data()
#schedule.format_time('04:1', '// aapm')