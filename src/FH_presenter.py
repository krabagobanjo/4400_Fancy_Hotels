from FH_model import *
from tkinter import *
from FH_views import *

class FH_presenter(Tk):
    def __init__(self, dbmodel):
        Tk.__init__(self)

        self.dbmodel = dbmodel
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        frame = LoginPage(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.curr_frame = frame
        frame.tkraise()

    def register(self, username, password, email):
        print(username)
        print(password)
        print(email)

        self.dbmodel.insert_data("newcust",[username,password,email] )
        self.show_frame(MainPageManager)


    def show_frame(self, callee):
        '''Show a frame for the given class'''
        frame = callee(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        self.curr_frame.destroy()
        self.curr_frame = frame

    def login(self, username, password):
        #TODO - Regex to check username and password validity
        users = dbmodel.get_data("login", username) #should only have one user
        if len(users) == 0:
            pass #message box: you done fucked up
        elif len(users) > 1:
            pass #this should never happen
        else:
            pass #check password match
        pass
