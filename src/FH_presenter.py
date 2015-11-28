from FH_model import *
from tkinter import *
import tkinter.messagebox
from FH_views import *
import re
import datetime


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

    def username_validation(self, username):
        #((c|m|C|M)\d{4})
        if(len(username) != 5):
            print("says wrong len");
            return False
        for index in range(len(username)):
            if(index == 0):
                if(username[index] != "c" and username[index] != "m"):
                    print("says c or m prob")
                    return False
            if(index != 0):
                print("says not int")
                if(not username[index].isdigit()):
                    return False
        return True

    def register(self, username, confirmPassword, password, email, caller):

        if not self.username_validation(username):
            tkinter.messagebox.showwarning("","invalid username")
        elif len(password) < 5 or len(password) > 15:
            tkinter.messagebox.showwarning("","invalid password, must be between 5 and 15 characters")
        elif password != confirmPassword:
            tkinter.messagebox.showwarning("","password doesnt equal confirm password")
        else:
            self.dbmodel.insert_data("newcust",[username,password,email] )
            self.show_frame(MainPageManager)


    def show_frame(self, caller):
        '''Show a frame for the given class'''
        frame = caller(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        self.curr_frame.destroy()
        self.curr_frame = frame

    def login(self, username, password):
        #TODO - Regex to check username and password validity
        cust_mode = True
        if (username[0].lower() == "c"):
            query_list = ['Username="'+username+'"']
            user = dbmodel.get_data("cust_login", query_list)
        elif(username[0].lower() == "m"):
            user = dbmodel.get_data("mgmt_login", query_list)
            cust_mode = False
        else:
            #throw error
            pass
        #we should only have one user
        if len(user) == 0:
            pass #message box: you done fucked up
        elif len(user) > 1:
            pass #this should never happen
        else:
            if password == user[1]:
                if cust_mode:
                    self.show_frame(self, MainPageCustomer)
                else:
                    self.show_frame(self, MainPageManager)
                pass #authenticate
            else:
                pass #throw error
        pass
