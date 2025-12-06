import pandas as pd
#from datetime import datetime
#import time
#import subprocess
import secrets
#import psutil
#from statistics import stdev
import ctypes
from tkinter import Label
from tkinter import Tk
#import shutil
from Widgets import *
#from PIL import Image, ImageTk

class glbl_var:
    def __init__(self):
        self.want_middle_name= True
        self.want_last_name = True
        self.required_first_name = ''
        self.required_middle_name = ''
        self.required_last_name = ''
        self.desired_gender = 'Female'
        self.NameLabel = ''
GV = glbl_var()

def generate_random_integer(minimum, maximum):
    secretsGenerator = secrets.SystemRandom()
    return secretsGenerator.randint(minimum, maximum)

def filter_names(name_order, baby_gender):
    Headings = baby_names_dataframe.columns.tolist()
    init = baby_names_dataframe.filter(items=Headings)

    cond = init['Names'].str.contains('', na=False, regex=False)
    filtered_dataframe = init.loc[cond]

    if True:#not (Animated==''):
        filtered_dataframe = filtered_dataframe.loc[filtered_dataframe[name_order] == True]
    #     filtered_dataframe = init
    filtered_dataframe = filtered_dataframe.loc[filtered_dataframe[baby_gender] == True]
    filtered_dataframe.reset_index(inplace=True)
    return filtered_dataframe
    
def get_value_at_cell(rowindex, heading='Names', frame=''):
    if len(frame) == 0:
        frame = baby_names_dataframe
    val = frame.at[rowindex, heading]
    if str(val).lower().strip() == 'nan':
        return ''
    else:
        return val

def generate_name(gender, include_middle_name=True, include_last_name=False):
    include_middle_name = GV.want_middle_name
    include_last_name = GV.want_last_name
    gender = GV.desired_gender
    if GV.required_first_name == '':
        first_names = filter_names('First', gender)
        fist_index = generate_random_integer(0, len(first_names)-1)
        first_name = get_value_at_cell(fist_index, frame=first_names)
    else:
        first_name = GV.required_first_name
    if include_middle_name:
        middle_name = first_name
        ready = False
        while not ready:
            middle_names = filter_names('Middle', gender)
            middle_index = generate_random_integer(0, len(middle_names)-1)
            middle_name = get_value_at_cell(middle_index, frame=middle_names)
            if not middle_name == first_name:
                ready = True
    elif not (GV.required_middle_name == ''):
        middle_name = GV.required_middle_name
    else:
        middle_name = ''
    if include_last_name:
        ready = False
        last_name = first_name
        while not ready:
            last_names = filter_names('Last', gender)
            last_index = generate_random_integer(0, len(last_names)-1)
            last_name = get_value_at_cell(last_index, frame=last_names)
            if not ((last_name == first_name) or (last_name == middle_name)):
                ready = True
    elif not (GV.required_last_name == ''):
        last_name = GV.required_last_name
    else:
        last_name = ''
    name = first_name + ' ' + middle_name + ' ' + last_name
    Name_Label = name.strip()
    GV.NameLabel.change_text(Name_Label)
    return name.strip()

def create_window(ttl='Input Info'):
    root = Tk()
    root.title(ttl)
    return root

def set_window_dimensions(width=960, height=540):
    window_width = width
    window_height = height
    positionHorizontal = round(screenwidth_in_pixels - window_width - (.0234375*screenwidth_in_pixels))
    positionVertical = round(.5*(screenheight_in_pixels - height))
    root.geometry('{}x{}+{}+{}'.format(width, height, positionHorizontal, 
                                       positionVertical))

def basic_parameters():
    FirstEntery = Label_Widget(root)
    first_label='Please Type Desired First Name Then Press Enter or Leave Empty'
    FirstEntery.add_widget(first_label)
    FirstEntery.place_here(1, 1, 0, 0)
    FIRST_Name = Textinput_Widget(root)
    FIRST_Name.add_widget(20, 1)
    FIRST_Name.place_here(FirstEntery.x+FirstEntery.width/2, 
                          FirstEntery.y-FirstEntery.height/2, 1, 0)
    FButt = Button_Widget(root)
    FButt.add_widget('Enter', setName, multiargument=True,
                                 args=['First', FIRST_Name])
    FButt.place_here(FIRST_Name.x+FIRST_Name.width/2+FButt.width/2, 
                          FirstEntery.y-FirstEntery.height/2, 1, 0)
    
    middleEntery = Label_Widget(root)
    middle_label='Please Type Desired Middle Name Then Press Enter or Leave Empty'
    middleEntery.add_widget(middle_label)
    middleEntery.place_here(FirstEntery.x-FirstEntery.width/2, 
                            FirstEntery.y+FirstEntery.height, 
                            0, 1)
    middle_Name = Textinput_Widget(root)
    middle_Name.add_widget(20, 1)
    middle_Name.place_here(middleEntery.x+middleEntery.width/2, 
                          middleEntery.y-middleEntery.height/2, 1, 0)
    MButt = Button_Widget(root)
    MButt.add_widget('Enter', setName, multiargument=True,
                                 args=['Middle', middle_Name])
    MButt.place_here(middle_Name.x+middle_Name.width/2+MButt.width/2, 
                          middleEntery.y-middleEntery.height/2, 1, 0)
    
    lastEntery = Label_Widget(root)
    last_label='Please Type Desired Last Name Then Press Enter or Leave Empty'
    lastEntery.add_widget(last_label)
    lastEntery.place_here(middleEntery.x-middleEntery.width/2, 
                            middleEntery.y+middleEntery.height, 
                            0, 1)
    last_Name = Textinput_Widget(root)
    last_Name.add_widget(20, 1)
    last_Name.place_here(lastEntery.x+lastEntery.width/2, 
                          lastEntery.y-lastEntery.height/2, 1, 0)
    LButt = Button_Widget(root)
    LButt.add_widget('Enter', setName, multiargument=True,
                                 args=['Last', last_Name])
    LButt.place_here(last_Name.x+last_Name.width/2+LButt.width/2, 
                          lastEntery.y-lastEntery.height/2, 1, 0)
    AlsoGenerateMiddleName = Button_Widget(root)
    AlsoGenerateMiddleName.add_widget('Toggle Me To Generate Middle Name',
                                      toggleMe, multiargument=True,
                                 args=['Middle', AlsoGenerateMiddleName])
    AlsoGenerateMiddleName.place_here(lastEntery.x-lastEntery.width/2, 
                            lastEntery.y+lastEntery.height, 
                            0, 1)
    AlsoGenerateMiddleName.change_color(background='green')
    
    AlsoGeneratelastName = Button_Widget(root)
    AlsoGeneratelastName.add_widget('Toggle Me To Generate Last Name',
                                      toggleMe, multiargument=True,
                                 args=['Last', AlsoGeneratelastName])
    AlsoGeneratelastName.place_here(AlsoGenerateMiddleName.x+AlsoGenerateMiddleName.width/2, 
                            lastEntery.y+lastEntery.height, 
                            1, 1)
    AlsoGeneratelastName.change_color(background='green')
    
    GenderButton = Button_Widget(root)
    GenderButton.add_widget('Toggle Me To Set Gender',
                                      toggleMe, multiargument=True,
                                 args=['Gender', GenderButton])
    GenderButton.place_here(AlsoGeneratelastName.x+AlsoGeneratelastName.width/2, 
                            AlsoGeneratelastName.y+AlsoGeneratelastName.height, 
                            1, 1)
    GenderButton.change_color(background='purple')
    
    GenerateButton = Button_Widget(root)
    GenerateButton.add_widget('Generate Baby Name',
                                      generate_name, multiargument=True,
                                 args=[GV.desired_gender, GV.want_middle_name, GV.want_last_name])
    GenerateButton.place_here(GenderButton.x+GenderButton.width/2, 
                            GenderButton.y+GenderButton.height, 
                            1, 1)
    GV.NameLabel = Label_Widget(root)
    GV.NameLabel.add_widget('')
    GV.NameLabel.place_here(777-GV.NameLabel.width, 
                            420, 
                            0, 1)
    
    root.mainloop()

def toggleMe(position, button):
    if position == 'Middle':
        if GV.want_middle_name:
            GV.want_middle_name = not GV.want_middle_name
            button.change_color(background='red')
        else:
            GV.want_middle_name = not GV.want_middle_name
            button.change_color(background='green')
    elif position == 'Last':
        if GV.want_last_name:
            GV.want_last_name = not GV.want_last_name
            button.change_color(background='red')
        else:
            GV.want_last_name = not GV.want_last_name
            button.change_color(background='green')
    else:
        if GV.desired_gender == 'Female':
            GV.desired_gender = 'Male'
            button.change_color(background='blue')
        else:
            GV.desired_gender = 'Female'
            button.change_color(background='purple')

def setName(pos, txtbx):
    if pos == 'First':
        GV.required_first_name = str(txtbx.inputboxes[0].get(1.0, "end-1c"))
    elif pos == 'Middle':
        GV.required_middle_name = str(txtbx.inputboxes[0].get(1.0, "end-1c"))
    else:
        GV.required_last_name = str(txtbx.inputboxes[0].get(1.0, "end-1c"))

root = create_window(ttl='Input Info')
u = ctypes.windll.user32
[screenwidth_in_pixels, screenheight_in_pixels] = [u.GetSystemMetrics(0), u.GetSystemMetrics(1)]
set_window_dimensions()
baby_names_dataframe = pd.read_csv('Names.csv', delimiter=',', header=0,
                                    skip_blank_lines=True, na_values='')
basic_parameters()

exit()
