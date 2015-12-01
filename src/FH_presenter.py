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
        self.saved_frame = None

    def username_validation(self, username):
        reg = r"((c|m|C|M)\d{4}$)"
        mch = re.findall(reg, username)
        return True if len(mch) > 0 and mch[0][0] == username else False

    def register(self, username, confirmPassword, password, email):
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
        username = username.capitalize()
        query = "username={}"
        cust_mode = True
        if self.username_validation(username):
            query_list = [username]
            if (username[0] == "C"):
                user = self.dbmodel.get_data("cust_login", query_list)
            elif(username[0] == "M"):
                user = self.dbmodel.get_data("mgmt_login", query_list)
                cust_mode = False
            else:
                return None
            #we should only have one user
            if len(user) == 0:
                return None
            elif len(user) > 1:
                return None #this should never happen
            else:
                if password == user[0][1]:
                    if cust_mode:
                        self.show_frame(MainPageCustomer)
                    else:
                        self.show_frame(MainPageManager)
                    self.curr_user = username
                else:
                    print("Bad password")
        return

    def get_avail_rooms1(self, location, startdate, enddate):
        #check location, startdate, enddate format
        query_list = [enddate, startdate, location]
        plist = self.dbmodel.get_data("find_rooms", query_list)
        frame = MakeReservations(self.container, self, plist, startdate, enddate, location)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        self.curr_frame.destroy()
        self.curr_frame = frame

    def get_update_rooms1(self, location, start_date, end_date):
        query_list = [enddate, startdate, location]
        plist = self.dbmodel.get_data("find_rooms", query_list)

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
        frame = MakeReservationDrop(self.container, self, entries, startdate, enddate, location)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        self.curr_frame.destroy()
        self.curr_frame = frame
        return

    def add_card(self, name, cardnum, expdate, cvv):
        self.dbmodel.insert_data("add_cardnum", [cardnum, name, expdate, cvv, self.curr_user])
        tkinter.messagebox.showwarning("","Card added!")
        self.restore_frame()
        self.curr_frame.get_cards()

    def del_card(self, cardnum):
        self.dbmodel.del_data("delete_cardnum", [cardnum])
        tkinter.messagebox.showwarning("","Card removed!")
        self.restore_frame()
        self.curr_frame.get_cards()

    def get_cards(self):
        card_list = self.dbmodel.get_data("find_cardnums", [self.curr_user])
        return [x[0] for x in card_list]

    def make_reservation(self, room_list, start_date, end_date, cardnum):
        #check valid start_date, end_date, cardnum
        #insert into reservation
        # last_id = self.dbmodel.get_data("get_last_reservID", None)
        #add_reserv_2
        cost = self.curr_frame.calc_cost()
        last_id = 42
        frame = ConfirmationPage(self.container, self, last_id)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        self.curr_frame.destroy()
        self.curr_frame = frame

    def get_reserv_by_id(self, resid):
        res_entry = self.dbmodel.get_data("get_reserv_by_id", [resid])
        if len(res_entry) < 1:
            return #no entry found
        elif len(res_entry) > 1:
            return #something screwed up
        else:
            start_date = res_entry[0][0]
            end_date = res_entry[0][1]
            frame = UpdateReservationPage2(self.container, self, start_date, end_date, resid)
            frame.grid(row=0, column=0, sticky="nsew")
            self.curr_frame.destroy()
            self.curr_frame = frame
            self.curr_frame.tkraise()

    def get_update_reserv(self, resid, start_date, end_date):
        rooms = self.dbmodel.get_data("get_update_reserv", [resid, start_date, end_date])
        frame = UpdateReservationPage3(self.container, self, rooms, resid, start_date, end_date)
        frame.grid(row=0, column=0, sticky="nsew")
        self.curr_frame.destroy()
        self.curr_frame = frame
        self.curr_frame.tkraise()

    def update_reserv(self, resid, start_date, end_date, rooms):
        tkinter.messagebox.showwarning("","Reservation updated")
        self.show_frame(MainPageCustomer)

    def get_cancel_reserv(self, resid):
        res_entry = self.dbmodel.get_data("get_cancel_reserv", [resid])
        if len(res_entry) < 1:
            return #no entry found
        else:
            # you get list of reservationID start_date end_date tot_cost Rcardnum Rusername cancelled HreservationID Hroomnum Hlocation roomnum location category numpeople cpday
            frame = CancelReservationPage2(self.container, self, res_entry)
            frame.grid(row=0, column=0, sticky="nsew")
            self.curr_frame.destroy()
            self.curr_frame = frame
            self.curr_frame.tkraise()

    def save_frame(self, to_save, next_frame):
        self.saved_frame = to_save
        self.curr_frame = next_frame(self.container, self)
        self.curr_frame.grid(row=0, column=0, sticky="nsew")
        self.curr_frame.tkraise()

    def restore_frame(self):
        self.curr_frame.destroy()
        self.curr_frame = self.saved_frame
        self.curr_frame.tkraise()

    def cancel_reservation(self, resid):
        # self.dbmodel.del_data("cancel_reserv_1", [resid])
        # self.dbmodel.del_data("cancel_reserv_2", [resid])
        tkinter.messagebox.showwarning("","Reservation cancelled!")
        self.show_frame(MainPageCustomer)

    def get_reviews(self, location):
        #need updated query for location
        review_list = self.dbmodel.get_data("get_reviews", [location])
        # review_list = []
        frame = ViewReviewPage2(self.container, self, review_list)
        frame.grid(row=0, column=0, sticky="nsew")
        self.curr_frame.destroy()
        self.curr_frame = frame
        self.curr_frame.tkraise()

    def add_review(self, rating, location, comment):
        add_list = [rating, location, comment, self.curr_user]
        self.dbmodel.insert_data("give_review", add_list)
        tkinter.messagebox.showwarning("","Review added!")
        self.show_frame(MainPageCustomer)

    def get_pop_rooms(self):
        room_list = [] #need sql query
        frame = PopularRoom(self.container, self, room_list)
        frame.grid(row=0, column=0, sticky="nsew")
        self.curr_frame.destroy()
        self.curr_frame = frame
        self.curr_frame.tkraise()

    def get_rev_report(self):
        rev_list = []
        frame = RevenueReport(self.container, self, rev_list)
        frame.grid(row=0, column=0, sticky="nsew")
        self.curr_frame.destroy()
        self.curr_frame = frame
        self.curr_frame.tkraise()

    def get_reserv_report(self):
        reserv_list = []
        # reserv_list = self.dbmodel.get_data
        frame = ReservationReport(self.container, self, reserv_list)
        frame.grid(row=0, column=0, sticky="nsew")
        self.curr_frame.destroy()
        self.curr_frame = frame
        self.curr_frame.tkraise()
