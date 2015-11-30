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
        self.curr_user = None

    def username_validation(self, username):
        reg = r"((c|m|C|M)\d{4}$)"
        match = re.match(reg, username)
        return True if match and match(0) == username else False

    def register(self, username, confirmPassword, password, email, caller):
        #We should remove the caller param, not needed
        # insert_string = "username={}, password={}, email={}"
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
        query = "username={}"
        cust_mode = True
        if self.username_validation(username):
            if (username[0].lower() == "c"):
                query_list = [username]
                user = self.dbmodel.get_data("cust_login", query_list)
            elif(username[0].lower() == "m"):
                user = self.dbmodel.get_data("mgmt_login", query_list)
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
                    self.curr_user = username
                    pass #authenticate
                else:
                    pass #throw error
            pass

    def get_avail_rooms1(self, location, startdate, enddate):
        query = """(M.HreservationID IS NULL OR '{}' > R.end_date OR '{}' < R.start_date) AND L.location = "{}" """
        #check location, startdate, enddate format
        query_list = [enddate, startdate, location]
        plist = self.dbmodel.get_data("find_rooms", query_list)
        frame = MakeReservations(self.container, self, plist, startdate, enddate, location)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        self.curr_frame.destroy()
        self.curr_frame = frame

    # def add_card(self, )

    def get_avail_rooms2(self, startdate, enddate, location, prev_queries, intvars):
        selected_rooms = []
        entries = []
        for i in range(len(intvars)):
            if intvars[i].get() == 1:
                selected_rooms.append(prev_queries[i][0])
        if len(selected_rooms) < 1:
            print("No rooms selected!")
            return
        for room in selected_rooms:
            for vals in prev_queries:
                if vals[0] == room:
                    entries.append(vals)
        frame = MakeReservationDrop(self.container, self, entries, startdate, enddate)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        self.curr_frame.destroy()
        self.curr_frame = frame
        return

    def add_card(self, name, cardnum, expdate, cvv):
        self.dbmodel.insert_data([cardnum, name, expdate, cvv, self.curr_user])
        tkinter.messagebox.showwarning("","Card added!")

    def get_cards(self):
        card_list = self.dbmodel.get_data(find_cardnums, [self.curr_user])
        return [x[0] for x in card_list]

    def make_reservation(self, room_list, start_date, end_date, cardnum):
        #check valid start_date, end_date, cardnum
        #insert into reservation
        last_id = self.dbmodel.get_data("get_last_reservID", None)
        #add_reserv_2
        frame = ConfirmationPage(self.container, self, last_id)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        self.curr_frame.destroy()
        self.curr_frame = frame
