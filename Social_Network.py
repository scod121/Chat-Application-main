# 19CS10027
# Divyansh Bhatia
# Chat Application

# Imports each and every method and class of module tkinter and tkinter.ttk

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext        # Import scrolledtext method from tkinter module
import PIL.ImageTk      # Importing ImageTk, Image methods from PIL module
import PIL.Image
from tkinter import filedialog      # Import filedialog method from tkinter module
import numpy as np
import matplotlib.pyplot as plt

global name         # Defining global variables here
global list
global y
global t

list = []           # Initializing global variables here
name = ""
y = t = ""

# Class User to store user information
# Like user id, contacts list and groups list
class user:
    def __init__(self, infoLine):       # init function of the class user
        self._user_id = ""
        self._contact_list = []
        self._group_list = []
        infoLine = infoLine.replace('<', '')        # Removing '<' character from the input line of the file
        infoLine = infoLine.replace('>', '')        # Removing '<' character from the input line of the file
        ch = str("")
        for i in infoLine:
            if(i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
                ch = ch + i
            elif i == ':':
                self._user_id = ch
                ch = ""
            else:
                self._contact_list.append(ch)
                ch = ""

    # Method to add group to the group list of a user
    def group_addition(self, groupName):
        self._group_list.append(groupName)

    # Method to print group user information
    def print_user(self):
        print(self._user_id)
        for x in self._group_list:
            print(x)

# Class RightFrame to handle all widgets and methods regarding the Right Frame of the main window
class RightFrame(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)        # init function of the class RightFrame
        self.master = master
        self.grid(row = 1, column = 3, columnspan = 2, sticky = "SNEW")
        master.grid_columnconfigure(3, weight = 1)

        self.labelx = Label(self, text=" ")         # Creating a label
        self.labelx.grid(row = 0, column = 3, padx = 10, pady = 11, sticky = W)     # Placing the widget in the respective frame (2-D table type)

        self.label = Label(self, text = " ")        # Creating a label
        self.label.grid(row = 1, column = 3, padx = 10, pady = 3, sticky = W)       # Placing the widget in the respective frame (2-D table type)

        self.outputText3 = scrolledtext.ScrolledText(self, height = 28, width = 65, bg = "light blue", font = ("Times", 15), selectbackground = "green")
        self.outputText3.grid(row = 2, column = 3, padx = 10, rowspan = 3, columnspan = 3)      # Placing the widget in the respective frame (2-D table type)

        self.exprtext = Entry(self, bd = 5, font = ("Times", 15))       # Entry widget to get messages typed
        self.exprtext.grid(row = 5, column = 3, rowspan = 2, columnspan = 2, padx = 10, ipadx = 150, ipady = 30, sticky = "WE")     # Placing the widget in the respective frame (2-D table type)

        self.imageButton = Button(self, text = "IMAGE", font = ("Times", 10), command = self.post_image_func, relief = RAISED)      # Creating the Button to select images and post them
        self.imageButton.grid(row = 5, column = 5, padx = 25, pady = 5, ipadx = 9, ipady = 5, sticky = W)       # Placing the widget in the respective frame (2-D table type)

        self.sendButton = Button(self, text = "POST", font = ("Times", 10), command = self.post_messages, relief = RAISED, padx = 15)        # Creating the Button to post messages
        self.sendButton.grid(row = 6, column = 5, padx = 25, pady = 5, ipady = 5,  sticky = W)      # Placing the widget in the respective frame (2-D table type)

    # Printing the messages to the chat window
    def print_messages(self):
        self.outputText3.delete("1.0", END)
        g = open("messages.txt", "r")       # Opening "messages.txt" file
        x = g.readline()        # Reading lines of the file
        if x == "\n":
            x = g.readline()
        global y
        t = y
        self.images = []
        count = 0
        while len(x) != 0:
            flag = False
            y = g.readline()        # Reading lines of the file
            z = g.readline()        # Reading lines of the file
            x = x.replace('\n', "")
            y = y.replace('\n', "")
            z = z.replace('\n', "")
            k = z[0: 7]
            if k == "#IMAGE#":
                z = z.replace('#IMAGE#', "")        # Identifying the images from the incoming messages
                global img
                l = open(z, 'rb')
                img = PIL.Image.open(l)
                img = img.resize((250, 250), PIL.Image.ANTIALIAS)
                img = PIL.ImageTk.PhotoImage(img)
                self.images.append(img)
                count += 1
                flag = True
            self.outputText3.tag_config('tag-left', justify = 'left')
            self.outputText3.tag_config('tag-right', justify = 'right')
            if x == name and y == t:
                self.outputText3.insert(END, name + " :  \n", 'tag-right')
                if flag == False:
                    self.outputText3.insert(END, z + "  \n\n", 'tag-right')
                else:
                    self.outputText3.insert(END, "                                                                               ")
                    self.outputText3.image_create(END, align = "center", image = self.images[count-1])
                    self.outputText3.insert(END, "\n\n")
                self.outputText3.see(END)
            elif x == t and y == name:
                self.outputText3.insert(END, " " + t + " :\n", 'tag-left')
                if flag == False:
                    self.outputText3.insert(END, " " + z + "\n\n", 'tag-left')
                else:
                    self.outputText3.image_create(END, align = "center", image = self.images[count-1])
                    self.outputText3.insert(END, "\n\n")
                self.outputText3.see(END)
            elif x in user_ids and y == t and y not in user_ids:
                self.outputText3.insert(END, " " + x + " :\n", 'tag-left')
                if flag == False:
                    self.outputText3.insert(END, " " + z + "\n\n", 'tag-left')
                else:
                    self.outputText3.image_create(END, align = "center", image = self.images[count - 1])
                    self.outputText3.insert(END, "\n\n")
                self.outputText3.see(END)
            x = g.readline()        # Reading lines of the file
            x = g.readline()        # Reading lines of the file
        g.close()       # Closing "messages.txt" file

    # Posting messages to the chat window
    def post_messages(self):
        message = self.exprtext.get()
        if message == "":
            return
        self.exprtext.delete(0, 'end')      # Clearing Entry message box
        global t
        global y
        g = open("messages.txt", "a")       # Opening "messages.txt" file to add messages
        g.write("\n")
        g.write(name + "\n")
        g.write(t + "\n")
        g.write(message + "\n")
        g.close()       # Closing "messages.txt" file
        y = t
        self.print_messages()

    # Post images to the chat window
    def post_image_func(self):
        x = filedialog.askopenfilename(title = '"pen')      # Opening the image
        global t
        global y
        g = open("messages.txt", "a")       # Opening "messages.txt" file to post images
        g.write("\n")
        g.write(name + "\n")
        g.write(t + "\n")
        g.write("#IMAGE#" + x + "\n")
        g.close()       # Closing "messages.txt" file
        y = t
        self.print_messages()

# Class LeftFrame to handle all widgets and methods regarding the Left Frame of the main window
class LeftFrame(RightFrame):
    def __init__(self, master = None, rframe = None):       # init function of the class LeftFrame
        Frame.__init__(self, master)
        self.master = master
        self.rframe = rframe
        self.grid(row = 1, column = 0, sticky = "SNEW")
        master.grid_columnconfigure(0, weight = 1)
        master.grid_rowconfigure(0, weight = 1)
        # self.outputText = Text(self)
        # self.outputText.grid(row = 1, column = 0)

        goButton = Button(self, text = "GO", font = ("Times", 12), relief = RAISED, padx = 15)       # Creating the Button to show the contacts and group information of a user
        goButton.grid(row = 0, column = 0, padx = 5, pady = 5)      # Placing the widget in the respective frame (2-D table type)
        goButton.bind("<Button-1>", self.show_modules)

        self.label_1 = Label(self, text = "Contacts", font = ("Times", 15))         # Creating the label Contacts
        self.label_1.grid(row = 1, column = 0, padx = 10, sticky = W)       # Placing the widget in the respective frame (2-D table type)

        self.outputText1 = Listbox(self, width = 33, height = 13, font = ("Times", 15), bg = "light green")
        self.outputText1.grid(row = 2, column = 0, padx = 10, sticky = W)       # Placing the widget in the respective frame (2-D table type)
        self.outputText1.bind("<<ListboxSelect>>", self.self_save1)          # Binding the widget to the self_save2 function

        self.label_2 = Label(self, text = "Groups", font = ("Times", 15))       # Creating the label Groups
        self.label_2.grid(row = 3, column = 0, padx = 10, sticky = W)       # Placing the widget in the respective frame (2-D table type)

        self.outputText2 = Listbox(self, width = 33, height = 13, font = ("Times", 15), bg = "light green")
        self.outputText2.grid(row = 4, column = 0, padx = 10,  sticky = W)      # Placing the widget in the respective frame (2-D table type)

        self.outputText2.bind("<<ListboxSelect>>", self.self_save2)         # Binding the widget to the self_save2 function

        self.showChatButton = Button(self, text = "SHOW CHAT", font = ("Times", 10), relief = RAISED, padx = 15)         # Creating the Button to show chat of a particular contact or group
        self.showChatButton.grid(row = 5, column = 0, padx = 25, pady = 5, ipady = 5)       # Placing the widget in the respective frame (2-D table type)

        self.exitButton = Button(self, text = "EXIT", font = ("Times", 10), command = exit, relief = RAISED, padx = 15)          # Creating the Button to exit or quit
        self.exitButton.grid(row = 6, column = 0, padx = 9, pady = 7, ipady = 5, sticky = W)        # Placing the widget in the respective frame (2-D table type)

    # Method to get the selected contact and store it in a global variable for future use
    def self_save1(self, event):
        if len(self.outputText1.curselection()) != 0:
            global y
            global t
            self.x = self.outputText1.get(self.outputText1.curselection())      # Getting the contact id selected
            y = self.x
            t = self.x
            self.showChatButton.bind("<Button-1>", self.show_chat)      # Binding the widget to the show_chat function function based on mouse click

    # Method to get the selected group and store it in a global variable for future use
    def self_save2(self, event):
        if len(self.outputText2.curselection()) != 0:
            global y
            global t
            self.x = self.outputText2.get(self.outputText2.curselection())      # Getting the group id selected
            y = self.x
            t = self.x
            self.showChatButton.bind("<Button-1>", self.show_chat)      # Binding the widget to the show_chat function function based on mouse click

    # To show chats with selected contact or group
    def show_chat(self, event):
        RightFrame.print_messages(self.rframe)

    # Printing contacts and groups ids in there respective listboxes of a particular user
    def print_contacts(self, Name):
        self.name = Name
        self.outputText2.delete( END)
        i = 0
        global list
        for x in list:
            if x._user_id == Name:
                for y in x._contact_list:
                    if y != "":
                        self.outputText1.insert(i, y)
                    i = i + 1
                i = 0
                for z in x._group_list:
                    if z != "":
                        self.outputText2.insert(i, z)
                    i = i + 1

    # Method to show contacts and groups of a user
    def show_modules(self, event):
        self.outputText1.delete(0, END)
        global name
        global list
        for x in list:
            if x._user_id == name:
                self.print_contacts(name)

#Window Class to describe main window and frames in it
class Window(Frame):
    def __init__(self, master = None):      # init function of the class Window
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(master, text = "     ")
        self.label.grid(row = 1, column = 1, columnspan = 2)
        self.rightFrame = RightFrame(master)
        self.leftFrame = LeftFrame(master, self.rightFrame)
        master.wm_title(160*" " + "Social Network")         # Setting title to window

# Function to get user_id from the combobox
def user_id(eventObject):
    global name
    name = eventObject.widget.get()

# initialize tkinter
root = Tk()
topFrame = Frame(root, height = 10, width = 50)
topFrame.grid(row = 0, column = 0, columnspan = 2, sticky = "SNEW")     # Placing the widget in the respective frame (2-D table type)
topFrame.grid_columnconfigure(0, weight = 1)
topFrame.grid_rowconfigure(0, weight = 0)
fileName = "social_network.txt"          # setting the title
f = open(fileName, "r")
x = f.readline()
x = f.readline()
while x[0] == '<':
    myObj = user(x)
    list.append(myObj)
    x = f.readline()

x = f.readline()
while len(x) != 0:
    ch = str("")
    group_id = ""
    x = x.replace('<', '')
    x = x.replace('>', '')
    for i in x:
        if(i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or i == '_':
            ch = ch + i
        elif i == ':':
            group_id = ch
            ch = ""
        else:
            for y in list:
                if y._user_id == ch:
                    y.group_addition(group_id)
            ch = ""
    x = f.readline()

label = Label(topFrame, text = "Select the current user  :  ", font = ("Times", 15))        # Creating a label
label.grid(row = 0, column = 0, sticky = W)     # Placing the widget in the respective frame (2-D table type)
global user_ids
user_ids = []
for x in list:
    user_ids.append(x._user_id)
users = ttk.Combobox(topFrame)
users['values'] = user_ids
users.current(0)
users.grid(row = 0, column = 1, padx = 5, pady = 5, ipady = 1, sticky = W)      # Placing the widget in the respective frame (2-D table type)
users.bind("<<ComboboxSelected>>", user_id)         # Binding the widget to the user_id function based on item selected from the box
app = Window(root)
checkbox = Checkbutton(root, text = "Keep me logged in", font = ("Times", 15))      # Creating a checkbutton showing "Keep me logged in"
checkbox.grid(row = 0, column = 4, padx = 25, sticky = E)       # Placing the widget in the respective frame (2-D table type)

# show window 
root.mainloop()
