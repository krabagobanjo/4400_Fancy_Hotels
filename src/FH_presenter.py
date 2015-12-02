from FH_model import *
from tkinter import *
import tkinter.messagebox
from FH_views import *
import re
from datetime import *
from types import *

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
        self.save_list = []

    def username_validation(self, username):
        reg = r"((c|m|C|M)\d{4}$)"
        mch = re.findall(reg, username)
        return True if len(mch) > 0 and mch[0][0] == username else False

    def email_validation(self,email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        else:
            return True

    def register(self, username, confirmPassword, password, email):
        # insert_string = "username={}, password={}, email={}"
        if not self.check_duplicate_users(username):
            if not self.username_validation(username):
                tkinter.messagebox.showwarning("","invalid username")
            elif not self.email_validation(email):
                tkinter.messagebox.showwarning("","invalid email")
            elif len(password) < 5 or len(password) > 15:
                tkinter.messagebox.showwarning("","invalid password, must be between 5 and 15 characters")
            elif password != confirmPassword:
                tkinter.messagebox.showwarning("","password doesnt equal confirm password")
            elif len(username) == 0 or len(confirmPassword) == 0 or len(password) == 0 or len(email) == 0:
                tkinter.messagebox.showwarning("","empty fields are not allowed")
            else:
                self.dbmodel.insert_data("newcust",[username,password,email] )
                self.show_frame(LoginPage)
        else:
            tkinter.messagebox.showwarning("","Username taken")


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
                    tkinter.messagebox.showwarning("","Invalid password!")

        return

    def check_reservation_dates(self, start, end):
        present = datetime.now()
        start_date = start
        end_date = end

        newstart = start_date.split("-")
        newend = end_date.split("-")

        if datetime(int(newstart[0]), int(newstart[1]), int(newstart[2])) < present:
            tkinter.messagebox.showwarning("","Error! Invalid date")
            return False
        if datetime(int(newstart[0]), int(newstart[1]), int(newstart[2])) > datetime(int(newend[0]), int(newend[1]), int(newend[2])):
            tkinter.messagebox.showwarning("","Error! Invalid date")
            return False
        return True

    def calc_refund(self, start, end, total_cost):
        present = datetime.now()
        start_date = start
        end_date = end
        if isinstance(start_date, str):
            newstart = start_date.split("-")
            newend = end_date.split("-")
            newer_start = datetime(int(newstart[0]), int(newstart[1]), int(newstart[2]))
            newer_end = datetime(int(newend[0]), int(newend[1]), int(newend[2]))
        else:
            newer_start = start_date
            newer_end  = end_date

        a = newer_start - present

        if a <= timedelta(days=1):
            return 0
        elif a <= timedelta(days=3):
            return total_cost*.8
        else:
            return total_cost

    def calc_cost_create(self, start, end, room_list, intvars):
        cost = 0
        start_date = start
        end_date = end
        newstart = start_date.split("-")
        newend = end_date.split("-")
        newer_start = datetime(int(newstart[0]), int(newstart[1]), int(newstart[2]))
        newer_end = datetime(int(newend[0]), int(newend[1]), int(newend[2]))
        timediff = newer_end - newer_start
        timediff = timediff.days
        for room in room_list:
            cost += (room[3] * timediff)
        for i in range(len(intvars)):
            if intvars[i].get() == 1:
                cost+=(room_list[i][4] * timediff)
        return cost

    def calc_cost(self, start, end, room_list):
        cost = 0
        start_date = start
        end_date = end
        if isinstance(start_date, str):
            newstart = start_date.split("-")
            newend = end_date.split("-")
            newer_start = datetime(int(newstart[0]), int(newstart[1]), int(newstart[2]))
            newer_end = datetime(int(newend[0]), int(newend[1]), int(newend[2]))
        else:
            newer_start = start_date
            newer_end  = end_date
        timediff = newer_end - newer_start
        timediff = timediff.days
        for room in room_list:
            cost += (room[3] * timediff)
        return cost


    def get_avail_rooms1(self, location, startdate, enddate):
        #check location, startdate, enddate format
        if self.check_reservation_dates(startdate, enddate):
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
        self.restore_resdrop_frame()

    def del_card(self, cardnum):
        self.dbmodel.del_data("delete_cardnum", [cardnum])
        tkinter.messagebox.showwarning("","Card removed!")
        self.restore_resdrop_frame()

    def get_cards(self):
        card_list = self.dbmodel.get_data("find_cardnums", [self.curr_user])
        ret = [x[0] for x in card_list]
        return ret

    def make_reservation(self, room_list, start_date, end_date, location, cardnum, intvars):
        #check valid start_date, end_date, cardnum
        #insert into reservation
        #start_date, end_date, tot_cost, Rcardnum, Rusername
        if self.check_reservation_dates(start_date, end_date):
            if not cardnum:
                return
            cost = self.calc_cost_create(start_date, end_date, room_list, intvars)
            self.dbmodel.insert_data("add_reserv_1", [start_date, end_date, cost, cardnum, self.curr_user])
            resid = self.dbmodel.get_data("get_last_reservID")
            resid = resid[0][0]
            #HreservationID, Hroomnum, Hlocation
            for room in room_list:
                self.dbmodel.insert_data("add_reserv_2", [resid, room[0], location])
            #SreservationID, Srooomnum, Slocation 3
            for i in range(len(intvars)):
                if intvars[i].get() == 1:
                    self.dbmodel.insert_data("add_reserv_3", [resid, room_list[i][0], location])
            frame = ConfirmationPage(self.container, self, resid)
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
        if self.check_reservation_dates(start_date, end_date):
            self.dbmodel.mult_queries("update_reserv_view_update")
            self.dbmodel.update_data("update_reserv_view_update_two",[start_date,end_date])
            self.dbmodel.mult_queries("update_reserv_view_update_three")
            rooms = self.dbmodel.get_data("update_reserv_view_update_four",[resid])
            rooms = [(room[0], room[2], room[3], room[4], room[7]) for room in rooms]
            # if len(rooms < 1):
            frame = UpdateReservationPage3(self.container, self, rooms, resid, start_date, end_date)
            frame.grid(row=0, column=0, sticky="nsew")
            self.curr_frame.destroy()
            self.curr_frame = frame
            self.curr_frame.tkraise()

    def update_reserv(self, resid, start_date, end_date):
        if self.check_reservation_dates(start_date, end_date):
            self.dbmodel.update_data("update_reserv", [start_date, end_date, resid])
            tkinter.messagebox.showwarning("","Reservation updated")
            self.show_frame(MainPageCustomer)

    def get_cancel_reserv(self, resid):
        res_entry = self.dbmodel.get_data("get_cancel_reserv", [resid])
        print(res_entry)
        if len(res_entry) < 1:
            return #no entry found
        else:
            # you get list of reservationID start_date end_date tot_cost Rcardnum Rusername cancelled HreservationID Hroomnum Hlocation roomnum location category numpeople cpday
            start_date = str(res_entry[0][1])
            end_date = str(res_entry[0][2])
            room_list = [(x[10], x[12], x[13], x[14], x[15], x[16]) for x in res_entry]
            cost = res_entry[0][3]
            frame = CancelReservationPage2(self.container, self, resid, room_list, start_date, end_date, cost)
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

    def save_resdrop_frame(self, next_frame, pop_list, startdate, enddate, location):
        self.save_list = [pop_list, startdate, enddate, location]
        self.curr_frame.destroy()
        self.curr_frame = next_frame(self.container, self)
        self.curr_frame.grid(row=0, column=0, sticky="nsew")
        self.curr_frame.tkraise()

    def restore_resdrop_frame(self):
        pop_list = self.save_list[0]
        startdate = self.save_list[1]
        enddate = self.save_list[2]
        location = self.save_list[3]
        self.curr_frame.destroy()
        self.curr_frame = MakeReservationDrop(self.container, self, pop_list, startdate, enddate, location)
        self.curr_frame.grid(row=0, column=0, sticky="nsew")
        self.curr_frame.tkraise()

    def cancel_reservation(self, resid):
        # self.dbmodel.del_data("cancel_reserv_1", [resid])
        # self.dbmodel.del_data("cancel_reserv_2", [resid])
        self.dbmodel.update_data("cancel_reservation", [resid])
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
        self.dbmodel.mult_queries("pop_report_view_update")
        room_list = self.dbmodel.get_data("get_pop_report", None)
        frame = PopularRoom(self.container, self, room_list)
        frame.grid(row=0, column=0, sticky="nsew")
        self.curr_frame.destroy()
        self.curr_frame = frame
        self.curr_frame.tkraise()

    def get_rev_report(self):
        rev_list = self.dbmodel.get_data("get_rev_report")
        frame = RevenueReport(self.container, self, rev_list)
        frame.grid(row=0, column=0, sticky="nsew")
        self.curr_frame.destroy()
        self.curr_frame = frame
        self.curr_frame.tkraise()

    def get_reserv_report(self):
        self.dbmodel.mult_queries("reserv_report_view_update")
        reserv_list = self.dbmodel.get_data("get_reserv_report", None)
        frame = ReservationReport(self.container, self, reserv_list)
        frame.grid(row=0, column=0, sticky="nsew")
        self.curr_frame.destroy()
        self.curr_frame = frame
        self.curr_frame.tkraise()

    def check_duplicate_users(self, username):
        reserv_list = self.dbmodel.get_data("cust_login", [username])
        if len(reserv_list)>0:
            tkinter.messagebox.showwarning("","username already exists")
            return True
        else:
            return False
