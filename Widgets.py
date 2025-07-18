#from Backend import *
from tkinter import *
from tkinter import ttk

class Button_Widget():
    def __init__(self, tk):
        self.root = tk
        self.buttons = []
        self.width = 1
        self.height = 1
        self.x = 1
        self.y = 1
        self.action = ''
        self.actionargs = ''
    
    def add_widget(self, name, action, action_arg='NA', x_pix_loc=1, y_pix_loc=1,
                   ancor='center', rel=False, plaisce=False, multiargument=False, args=[]):
        self.action = action
        self.actionargs = action_arg
        if multiargument:
            if len(args) == 2:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1, self.actionargs2)))
            elif len(args) == 1:
                self.actionargs1 = args[0]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1)))
            elif len(args) == 3:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1, self.actionargs2, self.actionargs3)))
            elif len(args) == 4:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.actionargs4 = args[3]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1,
                                                                    self.actionargs2,
                                                                    self.actionargs3,
                                                                    self.actionargs4)))
            elif len(args) == 5:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.actionargs4 = args[3]
                self.actionargs5 = args[4]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1,
                                                                    self.actionargs2,
                                                                    self.actionargs3,
                                                                    self.actionargs4,
                                                                    self.actionargs5)))
            elif len(args) == 6:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.actionargs4 = args[3]
                self.actionargs5 = args[4]
                self.actionargs6 = args[5]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1,
                                                                    self.actionargs2,
                                                                    self.actionargs3,
                                                                    self.actionargs4,
                                                                    self.actionargs5,
                                                                    self.actionargs6)))
            elif len(args) == 7:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.actionargs4 = args[3]
                self.actionargs5 = args[4]
                self.actionargs6 = args[5]
                self.actionargs7 = args[6]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1,
                                                                    self.actionargs2,
                                                                    self.actionargs3,
                                                                    self.actionargs4,
                                                                    self.actionargs5,
                                                                    self.actionargs6,
                                                                    self.actionargs7)))
            elif len(args) == 8:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.actionargs4 = args[3]
                self.actionargs5 = args[4]
                self.actionargs6 = args[5]
                self.actionargs7 = args[6]
                self.actionargs8 = args[7]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1,
                                                                    self.actionargs2,
                                                                    self.actionargs3,
                                                                    self.actionargs4,
                                                                    self.actionargs5,
                                                                    self.actionargs6,
                                                                    self.actionargs7,
                                                                    self.actionargs8)))
            elif len(args) == 9:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.actionargs4 = args[3]
                self.actionargs5 = args[4]
                self.actionargs6 = args[5]
                self.actionargs7 = args[6]
                self.actionargs8 = args[7]
                self.actionargs9 = args[8]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1,
                                                                    self.actionargs2,
                                                                    self.actionargs3,
                                                                    self.actionargs4,
                                                                    self.actionargs5,
                                                                    self.actionargs6,
                                                                    self.actionargs7,
                                                                    self.actionargs8,
                                                                    self.actionargs9)))
        else:
            self.buttons.append(Button(self.root, text=name, command=lambda: self.action(self.actionargs)))
        if plaisce:
            if rel:
                self.buttons[len(self.buttons)-1].place(relx=x_pix_loc, rely=y_pix_loc, anchor=ancor)
            else:
                self.buttons[len(self.buttons)-1].place(x=x_pix_loc, y=y_pix_loc, anchor=ancor)
        self.width = self.buttons[len(self.buttons)-1].winfo_reqwidth()
        self.height = self.buttons[len(self.buttons)-1].winfo_reqheight()
        self.x = x_pix_loc
        self.y = y_pix_loc

    def place_here(self, xloc, yloc, paddingx, paddingy, ancor='center', rel=False):
        truex = (self.width/2) + paddingx + xloc
        truey = (self.height/2) + paddingy + yloc
        if rel:
            #xcenterpix = 
            self.buttons[len(self.buttons)-1].place(relx=truex, rely=truex, anchor=ancor)
        else:
            self.buttons[len(self.buttons)-1].place(x=truex, y=truey, anchor=ancor)
        self.x = truex
        self.y = truey

    def change_color(self, foreground='', background=''):
        color_dictionary = {
            'red': '#f04209',
            'blue': '#0942f0',
            'white': '#fefeff',
            'black': '#000001',
            'green': '#09f042',
            'purple': '#fe11fe',
            'yellow': '#FEFE11',
            'orange': '#ff800f',
            'periwinkle': '#ccccff'
        }
        if foreground in color_dictionary:
            foreground = color_dictionary[foreground]
        if background in color_dictionary:
            background = color_dictionary[background]
        if not foreground == '':
            try:
                self.buttons[0].config(fg=foreground)
            except Exception as err:
                print(err)
        if not background == '':
            try:
                self.buttons[0].config(bg=background)
            except Exception as err:
                print(err)

    def config_width(self, wid_pix=0, ind=0):
        wid = 0
        while self.width < wid_pix:
            self.buttons[ind].config(width=wid)
            self.width = self.buttons[len(self.buttons)-1].winfo_reqwidth()
            wid = wid + 1

    def config_height(self, he_pix=0, ind=0):
        he = 0
        while self.height < he_pix:
            self.buttons[ind].config(height=he)
            self.height = self.buttons[len(self.buttons)-1].winfo_reqheight()
            he = he + 1

    def remove_widget(self, indexes=[]):
        if indexes == []:
            self.buttons = []
        else:
            temp = []
            for index in range(0, len(self.buttons)):
                if index not in indexes:
                    temp.append(self.buttons[index])
            self.buttons = temp
    
    def destroy_widget(self):
        for i in range(0, len(self.buttons)):
            self.buttons[i].destroy()

class Label_Widget():
    def __init__(self, tk):
        self.root = tk
        self.labels = []
        self.width = 1
        self.height = 1
        self.x = 1
        self.y = 1
        self.txt = ''

    def change_color(self, bg_color='', fg_color=''):
        #fg is the label fill color
        #bg is the text color
        color_dictionary = {
            'red': '#f04209',
            'blue': '#0942f0',
            'white': '#fefeff',
            'black': '#000001',
            'green': '#09f042',
            'purple': '#fe11fe',
            'yellow': '#FEFE11',
            'orange': '#ff800f',
            'periwinkle': '#ccccff'
        }
        if fg_color in color_dictionary:
            fg_color = color_dictionary[fg_color]
        if bg_color in color_dictionary:
            bg_color = color_dictionary[bg_color]
        if not (fg_color == ''):
            self.labels[0].config(fg=fg_color)
        if not (bg_color == ''):
            self.labels[0].config(bg=bg_color)

    def change_text(self, text):
        self.labels[0].config(text=text)
        self.txt = text
    
    def add_widget(self, label, xloc=1, yloc=1, ancor='center', rel=False, plaisce=False, w='', h=''):
        self.labels.append(Label(self.root, text=label))
        if (w == '') and (not (h == '')):
            self.labels[len(self.labels)-1].config(height=h)
        elif (not (w == '')) and (h == ''):
            self.labels[len(self.labels)-1].config(width=w)
        elif (not (w == '')) and (not (h == '')):
            self.labels[len(self.labels)-1].config(width=w, height=h)
        if plaisce:
            if rel:
                self.labels[len(self.labels)-1].place(relx=xloc, rely=yloc, anchor=ancor)
            else:
                self.labels[len(self.labels)-1].place(x=xloc, y=yloc, anchor=ancor)
        self.width = self.labels[len(self.labels)-1].winfo_reqwidth()
        self.height = self.labels[len(self.labels)-1].winfo_reqheight()
        self.x = xloc
        self.y = yloc

    def place_here(self, xloc, yloc, paddingx, paddingy, ancor='center', rel=False):
        truex = (self.width/2) + paddingx + xloc
        truey = (self.height/2) + paddingy + yloc
        if rel:
            #xcenterpix = 
            self.labels[len(self.labels)-1].place(relx=truex, rely=truex, anchor=ancor)
        else:
            self.labels[len(self.labels)-1].place(x=truex, y=truey, anchor=ancor)
        self.x = truex
        self.y = truey

    def change_color(self, foreground='', background=''):
        color_dictionary = {
            'red': '#f04209',
            'blue': '#0942f0',
            'white': '#fefeff',
            'black': '#000001',
            'green': '#09f042',
            'purple': '#fe11fe',
            'yellow': '#FEFE11',
            'orange': '#ff800f',
            'periwinkle': '#ccccff'
        }
        if foreground in color_dictionary:
            foreground = color_dictionary[foreground]
        if background in color_dictionary:
            background = color_dictionary[background]
        if not foreground == '':
            try:
                self.labels[0].config(fg=foreground)
            except Exception as err:
                print(err)
        if not background == '':
            try:
                self.labels[0].config(bg=background)
            except Exception as err:
                print(err)
    
    def change_font_size(self, font_size):
        self.labels[0].config(font=("Arial", font_size, "bold"))
        self.width = self.labels[len(self.labels)-1].winfo_reqwidth()
        self.height = self.labels[len(self.labels)-1].winfo_reqheight()

class Textinput_Widget():
    def __init__(self, tk):
        self.root = tk
        self.inputboxes = []
        self.width = 1
        self.height = 1
        self.x = 1
        self.y = 1
    
    def add_widget(self, number_of_characters, number_of_lines, xloc=1, yloc=1, ancor='center', rel=False, plaisce=False):
        self.inputboxes.append(Text(self.root, width=number_of_characters, height=number_of_lines))
        if plaisce:
            if rel:
                self.inputboxes[len(self.inputboxes)-1].place(relx=xloc, rely=yloc, anchor=ancor)
            else:
                self.inputboxes[len(self.inputboxes)-1].place(x=xloc, y=yloc, anchor=ancor)
        self.width = self.inputboxes[len(self.inputboxes)-1].winfo_reqwidth()
        self.height = self.inputboxes[len(self.inputboxes)-1].winfo_reqheight()
        self.x = xloc
        self.y = yloc

    def remove_widget(self, indexes=[]):
        if indexes == []:
            self.inputboxes = []
        else:
            temp = []
            for index in range(0, len(self.inputboxes)):
                if index not in indexes:
                    temp.append(self.inputboxes[index])
            self.inputboxes = temp

    def place_here(self, xloc, yloc, paddingx=1, paddingy=1, ancor='center', rel=False):
        truex = (self.width/2) + paddingx + xloc
        truey = (self.height/2) + paddingy + yloc
        if rel:
            #xcenterpix = 
            self.inputboxes[len(self.inputboxes)-1].place(relx=truex, rely=truex, anchor=ancor)
        else:
            self.inputboxes[len(self.inputboxes)-1].place(x=truex, y=truey, anchor=ancor)
        self.x = truex
        self.y = truey

    def change_color(self, foreground='', background=''):
        color_dictionary = {
            'red': '#f04209',
            'blue': '#0942f0',
            'white': '#fefeff',
            'black': '#000001',
            'green': '#09f042',
            'purple': '#fe11fe',
            'yellow': '#FEFE11',
            'orange': '#ff800f',
            'periwinkle': '#ccccff'
        }
        if foreground in color_dictionary:
            foreground = color_dictionary[foreground]
        if background in color_dictionary:
            background = color_dictionary[background]
        if not foreground == '':
            try:
                self.inputboxes[0].config(fg=foreground)
            except Exception as err:
                print(err)
        if not background == '':
            try:
                self.inputboxes[0].config(bg=background)
            except Exception as err:
                print(err)

    def clear(self):
        self.inputboxes[0].delete("1.0",END)

    def get_text_input(self, raw=False):
        if raw:
            return self.inputboxes[0].get(1.0, "end-1c")
        else:
            return str(self.inputboxes[0].get(1.0, "end-1c")).replace('\n', '').strip()
    
    def destroy_widget(self):
        for i in range(0, len(self.inputboxes)):
            self.inputboxes[i].destroy()
        
