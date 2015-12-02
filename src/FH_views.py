from FH_presenter import *
from tkinter import *
import pymysql
from datetime import *
import time

TITLE_FONT = ("Times", 20, "italic")
Main_Font = ("Times", 14)

class LoginPage(Frame):

    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        loglabel = Label(self, text="Login Page", font=TITLE_FONT)
        loglabel.grid(row = 1, column = 1, columnspan = 2, sticky = N+S+E+W)
        Label(self, text = "").grid(row = 2, column = 0)

        self.uservar = StringVar()
        self.pwordvar = StringVar()


        user = Label(self, text = "Username", font = Main_Font)
        user.grid(row = 3, column = 0)

        password = Label(self, text = "Password",font = Main_Font)
        password.grid(row = 4, column = 0)

        e_user = Entry(self, width = 30, textvariable = self.uservar)
        e_user.grid(row = 3, column = 1)

        e_password = Entry(self, width = 30, textvariable = self.pwordvar, show='*')
        e_password.grid(row = 4, column = 1)

        login_button = Button(self, text="Login", font = Main_Font, relief = RAISED, command=lambda: presenter.login(self.uservar.get(), self.pwordvar.get()))
        register_button = Button(self, text="New User? Create Account", font = Main_Font, relief = FLAT, command=lambda: presenter.show_frame(RegisterPage))
        login_button.grid( row = 5, column = 1)
        Label(self,text="").grid(row = 6, column = 0)
        Label(self,text="").grid(row = 7, column = 0)
        register_button.grid(row = 8, column = 1)



class RegisterPage(Frame):

    def __init__(self, parent, presenter):

        Frame.__init__(self, parent)
        Title = Label(self, text= "New User Registration", font=TITLE_FONT)
        Title.grid(row = 2, column = 0, columnspan = 2)

        photo = PhotoImage(file = "crest.gif")
        header = Label(self, image = photo)
        header.image= photo
        header.grid(row=0, column =  0, columnspan = 2)

        Label(self, text = "").grid(row=3, column = 0)
        Label(self, text = "Username", font = Main_Font).grid(row = 4, column = 0, sticky = W)
        Label(self, text = "Password", font = Main_Font).grid(row = 5, column = 0, sticky = W)
        Label(self, text = "Confirm Password", font = Main_Font).grid(row=6, column = 0, sticky = W)
        Label(self, text = "Email", font = Main_Font).grid(row = 7, column = 0, sticky = W)

        #initialze registration variables
        username = StringVar()
        password = StringVar()
        confirmPassword = StringVar()
        email = StringVar()

        Entry(self, width = 20, textvariable = username).grid(row = 4, column = 1)
        Entry(self, width = 20, textvariable = password, show='*').grid(row = 5, column = 1)
        Entry(self, width = 20, textvariable = confirmPassword, show = '*').grid(row = 6, column = 1)
        Entry(self, width = 20, textvariable = email).grid(row = 7, column = 1)

        Label(self, text = "").grid(row =8)

        button = Button(self, text="Submit",font = Main_Font, relief = RAISED,
                           command=lambda: presenter.register(username.get(), confirmPassword.get(), password.get(), email.get()))
        button.grid(row = 9, column = 1)

class MainPageCustomer(Frame):

    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        label = Label(self, text="Choose Functionality", font=TITLE_FONT)
        label.grid(column = 0, row = 1, columnspan = 2)

        Label(self, text = "Welcome!", font = ("Times",18)).grid(row = 3, column = 0)
        Button(self, text = "Make a New Reservation",font = Main_Font, relief = FLAT, command=lambda: presenter.show_frame(SearchRooms)).grid(row = 4, column = 0)
        Button(self, text = "Update your reservation",font = Main_Font, relief = FLAT, command=lambda: presenter.show_frame(UpdateReservationPage1)).grid(row = 5, column = 0)
        Button(self, text = "Cancel Reservation",font = Main_Font, relief = FLAT, command=lambda: presenter.show_frame(CancelReservationPage1)).grid(row = 6, column = 0)
        Button(self, text = "Provide Feedback",font = Main_Font, relief = FLAT, command=lambda: presenter.show_frame(GiveReviewPage)).grid(row = 7, column = 0)
        Button(self, text = "View Feedback",font = Main_Font, relief = FLAT,command=lambda: presenter.show_frame(ViewReviewPage1)).grid(row = 8, column = 0)
        Button(self, text = "Edit Payment Info", font = Main_Font, relief = FLAT, command=lambda: presenter.show_frame(PaymentPage)).grid(row = 9, column = 0)
        button = Button(self, text="Go to the Login page",font = Main_Font,
                           command=lambda: presenter.show_frame(LoginPage))
        button.grid(row = 10, column = 0)




class MainPageManager(Frame):

    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        Label(self, text = "Choose Functionality", font = TITLE_FONT).grid(row = 1, column = 0, columnspan = 2)
        Label(self, text = "Welcome!", font = ("Times", 18)).grid(row = 2, column = 0)
        Button(self, text = "View Reservation Report",font = Main_Font, relief = FLAT, command=lambda: presenter.get_reserv_report()).grid(row = 3, column = 0)
        Button(self, text = "View Popular Room Category Report",font = Main_Font, relief = FLAT, command=lambda: presenter.get_pop_rooms()).grid(row = 4, column = 0)
        Button(self, text = "View Revenue Report",font = Main_Font, relief = FLAT, command=lambda: presenter.get_rev_report()).grid(row = 5, column = 0)

class SearchRooms(Frame):
    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        Label(self, text = "Search Rooms", font = TITLE_FONT).grid(row = 0, column = 0, columnspan = 4)
        Label(self, text = "").grid(row = 1, column = 0)
        Label(self, text = "Location",font = Main_Font).grid(row = 2, column = 0)
        Label(self, text = "").grid(row = 3, column = 0)
        Label(self, text = "Start Date",font = Main_Font).grid(row = 4, column = 0)
        Label(self, text = "End Date",font = Main_Font).grid(row = 4, column = 2)

        self.startdate = StringVar()
        self.enddate = StringVar()

        Entry(self, width = 10, textvariable = self.startdate).grid(row = 4, column = 1)
        Entry(self, width = 10, textvariable = self.enddate).grid(row = 4, column =     3)

        Label(self, text = "").grid(row = 5)
        Button(self, text = "Search",font = Main_Font, relief = RAISED, command = lambda: presenter.get_avail_rooms1(self.location.get(), self.startdate.get(), self.enddate.get())).grid(row = 6, column = 3)
        self.location = StringVar()
        locations = OptionMenu(self,self.location, "Atlanta", "Charlotte", "Savannah", "Orlando", "Miami")
        locations.configure(width = 20, font = Main_Font)
        locations.grid(row = 2, column = 1)

class MakeReservations(Frame):
    def __init__(self, parent, presenter, pop_list, startdate, enddate, location):
        Frame.__init__(self, parent)
        Label(self, text = "Make Reservations", font = TITLE_FONT).grid(row = 0, column = 2, columnspan = 2)
        Label(self, text = "Room Number", font = Main_Font).grid(row = 1, column = 0)
        Label(self, text = "Room Category", font = Main_Font).grid(row = 1, column = 1)
        Label(self, text = "# of People Allowed", font = Main_Font).grid(row = 1, column = 2)
        Label(self, text = "Cost Per Day", font = Main_Font).grid(row = 1, column = 3)
        Label(self, text = "Cost of Extra Bed Per Day", font = Main_Font).grid(row = 1, column = 4)
        Label(self, text = "Select Room", font = Main_Font).grid(row = 1, column = 5)
        # self.populate_list(pop_list)
        self.pop_list = pop_list
        self.start_date = startdate
        self.enddate = enddate
        self.location = location
        colcount = -1
        rowcount = 1
        self.room_choice_vars = []
        self.room_choice = IntVar()
        for i in pop_list:
            rowcount = rowcount + 1
            colcount = -1
            for value in i:
                if value == "Atlanta" or value == "Orlando" or value == "Savannah" or value == "Charlotte" or value == "Miami":
                    pass
                else:
                    colcount = colcount + 1
                    Label(self, text = value, font = Main_Font).grid(row = rowcount, column = colcount)

        for i in range(len(pop_list)):
            var = IntVar()
            RB = Checkbutton(self, variable = var)
            self.room_choice_vars.append(var)
            RB.grid(row = i + 2, column = 5)
        Button(self, text = "Check Details", font = Main_Font, command = lambda: presenter.get_avail_rooms2(self.start_date, self.enddate, self.location, self.pop_list, self.room_choice_vars)).grid(row = len(pop_list)+2, column = 5)


class MakeReservationDrop(Frame):
    def __init__(self, parent, presenter, pop_list, startdate, enddate, location):
        Frame.__init__(self, parent)
        Label(self, text = "Room Number", font = Main_Font).grid(row = 0, column = 0)
        Label(self, text = "Room Category", font = Main_Font).grid(row = 0, column = 1)
        Label(self, text = "# of People Allowed", font = Main_Font).grid(row = 0, column = 2)
        Label(self, text = "Cost Per Day", font = Main_Font).grid(row = 0, column = 3)
        Label(self, text = "Cost of Extra Bed Per Day", font = Main_Font).grid(row = 0, column = 4)
        Label(self, text = "Extra Bed", font = Main_Font).grid(row = 0, column = 5)
        self.pop_list = pop_list
        self.presenter = presenter
        self.start_date = startdate
        self.end_date = enddate
        self.location = location
        n = pop_list
        #The part part of this will contain the list of checked rooms for now I'll use n
        colcount = -1
        rowcount = 1
        for i in n:
            rowcount = rowcount + 1
            colcount = -1
            for value in i:
                colcount = colcount + 1
                Label(self, text = value, font = Main_Font).grid(row = rowcount, column = colcount)

        Label(self, text = "Start Date", font = Main_Font).grid(row = len(n) + 2, column =0)
        Label(self, text = "End Date", font = Main_Font).grid(row = len(n) + 2, column = 3)
        Label(self, text = "Total Cost", font = Main_Font).grid(row = len(n) + 3, column = 0)
        Label(self, text = "Use Card", font = Main_Font).grid(row = len(n) + 4, column = 0)

        self.start_date_var = StringVar()
        self.start_date_var.set(startdate)
        self.end_date_var = StringVar()
        self.end_date_var.set(enddate)
        self.total_cost_var = StringVar()


        Entry(self, textvariable = self.start_date_var).grid(row = len(n)+ 2, column = 1, columnspan = 2)
        Entry(self, textvariable = self.end_date_var).grid(row = len(n) + 2, column = 4, columnspan = 2)
        Entry(self, textvariable = self.total_cost_var).grid(row = len(n) + 3, column = 1, columnspan = 2)

        self.credit_card = StringVar()
        # options = [ "hey", "bye" ]
        options = presenter.get_cards() if presenter.get_cards() else [None]
        #these are just test values this would be the populated list of credit cards
        credit_card = OptionMenu (self, self.credit_card, *options)
        credit_card.configure(font = Main_Font)
        credit_card.grid(row = len(n)+ 4, column = 1, columnspan = 2)

        Button(self, text = "Edit Cards", font = Main_Font, relief = FLAT, command = lambda: presenter.save_resdrop_frame(PaymentPage, self.pop_list, self.start_date, self.end_date, self.location)).grid(row = len(n) + 4, column = 3)
        Button(self, text = "Submit", font = Main_Font, command = lambda: presenter.make_reservation(pop_list, self.start_date_var.get(), self.end_date_var.get(), self.location, self.credit_card.get(), self.room_choice_vars)).grid(row =len(n) + 5, column = 4)
        Button(self, text = "Update Cost", font = Main_Font, relief = RAISED, command=lambda: self.set_cost(self.room_choice_vars)).grid(row = len(n) + 5, column = 1)

        self.room_choice_vars = []
        self.room_choice = IntVar()
        for i in range(len(n)):
            var = IntVar()
            RB = Checkbutton(self, variable = var)
            self.room_choice_vars.append(var)
            RB.grid(row = i + 2, column = 5)
        self.total_cost_var.set(presenter.calc_cost_create(self.start_date, self.end_date, self.pop_list, self.room_choice_vars))

    def set_cost(self, intvars):
        self.total_cost_var.set(self.presenter.calc_cost_create(self.start_date, self.end_date, self.pop_list, self.room_choice_vars))

class PaymentPage(Frame):
    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)

        Label(self, text = "Payment Information", font = TITLE_FONT).grid(row = 0, column = 1, columnspan = 2)
        Label(self, text = "Add Card", font = ("Times", 16, "bold")).grid(row = 1, column = 0)
        Label(self, text = "").grid(row = 2, column = 0)
        Label(self, text = "Name on Card", font = Main_Font).grid(row = 3, column = 0)
        Label(self, text = "Card Numnber", font = Main_Font).grid(row = 4, column = 0)
        Label(self, text = "Expiration Date", font = Main_Font).grid(row = 5, column = 0)
        Label(self, text = "CVV", font = Main_Font).grid(row = 6, column = 0)
        Label(self, text = "").grid(row = 7, column = 0)

        self.name_var = StringVar()
        self.card_num_var = StringVar()
        self.ex_date_var = StringVar()
        self.cvv_var = StringVar()

        Entry(self, textvariable = self.name_var, width = 10).grid(row = 3, column = 1)
        Entry(self, textvariable = self.card_num_var, width = 10).grid(row = 4, column = 1)
        Entry(self, textvariable = self.ex_date_var, width = 10).grid(row = 5, column = 1)
        Entry(self, textvariable = self.cvv_var, width = 10).grid(row = 6, column = 1)

        Label(self, text = "Delete Card", font = ("Times", 16, "bold")).grid(row = 1, column = 2)
        Label(self, text = "").grid(row = 2, column = 2)
        Label(self, text = "Card Number", font = Main_Font).grid(row = 3, column = 2)

        # options = [ "hi", "bye"]
        options = presenter.get_cards()
        self.credit_card = StringVar()
        credit_card = OptionMenu (self, self.credit_card, *options)
        credit_card.configure(width = 20, font = Main_Font)
        credit_card.grid(row = 3, column = 3)

        Button(self, text = "Save", font = Main_Font, command= lambda: presenter.add_card(self.name_var.get(), self.card_num_var.get(), self.ex_date_var.get(), self.cvv_var.get())).grid(row = 8, column = 0)
        Button(self, text = "Delete", font = Main_Font, command= lambda: presenter.del_card(self.credit_card.get())).grid(row = 8, column = 3)

class ConfirmationPage(Frame):
    def __init__(self, parent, presenter, con_id):
        Frame.__init__(self, parent)
        Label(self, text = "Confirmation Screen", font = TITLE_FONT).grid(row = 0, column = 0, columnspan = 2)
        Label(self, text = "").grid(row = 1, column = 0)
        Label(self, text = "Your Reservation ID", font = Main_Font).grid(row = 2, column = 0)
        Label(self, text = "").grid(row = 3, column = 0)
        Label(self, text = "").grid(row = 4, column = 0)
        Label(self, text = "Please save this reservation id for all further communication", font = ("Times", 10)).grid(row = 5, column = 0, columnspan = 2)

        self.confirm_var = IntVar()
        self.confirm_var.set(con_id)

        Entry(self, textvariable = self.confirm_var, width = 10).grid(row = 2, column = 1)

class UpdateReservationPage1(Frame):
    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        Label(self, text = "Update Reservation", font = TITLE_FONT).grid(row = 0, column = 1)
        Label(self, text = "").grid(row = 1, column = 0)
        Label(self, text = "Reservation ID", font = Main_Font).grid(row = 2, column = 0)

        self.res_id_var = IntVar()
        Entry(self, textvariable = self.res_id_var, width = 10).grid(row = 2, column = 1)

        Button(self, text = "Search", font= Main_Font, command=lambda: presenter.get_reserv_by_id(self.res_id_var.get())).grid(row = 2, column = 2)

class UpdateReservationPage2(Frame):
    def __init__(self, parent, presenter, curr_start, curr_end, reservationID):
        Frame.__init__(self, parent)
        Label(self, text = "Current Start Date", font = Main_Font).grid(row = 0, column = 0)
        Label(self, text = "Current End Date", font = Main_Font).grid(row = 0, column = 2)
        Label(self, text = "").grid(row = 1, column = 0)
        Label(self, text = "New Start Date", font = Main_Font).grid(row = 2, column = 0)
        Label(self, text = "New End Date", font = Main_Font).grid(row = 2, column = 2)
        Label(self, text = "").grid(row = 3, column = 0)

        self.current_start_var = StringVar()
        self.current_start_var.set(curr_start)
        self.current_end_var = StringVar()
        self.current_end_var.set(curr_end)
        self.new_start_var = StringVar()
        self.new_end_var = StringVar()

        Entry(self, textvariable = self.current_start_var, width = 10).grid(row = 0, column = 1)
        Entry(self, textvariable = self.current_end_var, width = 10).grid(row = 0, column = 3)
        Entry(self, textvariable = self.new_start_var, width = 10).grid(row = 2, column = 1)
        Entry(self, textvariable = self.new_end_var, width = 10).grid(row = 2, column = 3)

        Button(self, text = "Search Availability", font = Main_Font, command=lambda: presenter.get_update_reserv(reservationID, self.new_start_var.get(), self.new_end_var.get())).grid(row = 4, column = 1, columnspan = 2)

class UpdateReservationPage3(Frame):
    def __init__(self, parent, presenter, pop_list, resid, start_date, end_date):
        Frame.__init__(self, parent)
        Label(self, text = "Room are available. Please confirm details below before submitting", font = Main_Font).grid(row = 0, column = 0, columnspan = 5)
        Label(self, text = "Room Number", font = Main_Font).grid(row = 1, column = 0)
        Label(self, text = "Room Category", font = Main_Font).grid(row = 1, column = 1)
        Label(self, text = "# of People Allowed", font = Main_Font).grid(row = 1, column = 2)
        Label(self, text = "Cost Per Day", font = Main_Font).grid(row = 1, column = 3)
        Label(self, text = "Cost of Extra Bed Per Day", font = Main_Font).grid(row = 1, column = 4)
        Label(self, text = "Select Extra Bed", font = Main_Font).grid(row = 1, column = 5)

        self.pop_list = pop_list
        self.start_date = start_date
        self.end_date = end_date
        self.resid = resid
        n = [p[0:5] for p in pop_list]
        # this will be populated with available rooms ill use n for now
        colcount = -1
        rowcount = 1
        for i in n:
            rowcount = rowcount + 1
            colcount = -1
            for value in i:
                colcount = colcount + 1
                Label(self, text = value, font = Main_Font).grid(row = rowcount, column = colcount)

        Label(self, text = "Total Cost Updated", font = Main_Font).grid(row = len(n) + 2, column = 0, columnspan = 2)
        self.cost_var = IntVar()
        Entry(self, textvariable = self.cost_var, width = 10).grid(row = len(n) + 2, column = 2)
        Button(self, text = "Submit", font = Main_Font, relief = RAISED, command=lambda: presenter.update_reserv(self.resid, self.start_date, self.end_date, presenter.calc_cost(start_date, end_date, pop_list, self.extra_bed_list))).grid(row = len(n) + 3, column = 5)

        self.room_choice_vars = []
        self.room_choice = IntVar()
        self.extra_bed_list = []
        for i in range(len(n)):
            var = IntVar()
            if pop_list[i][5]:
                var.set(1)
                self.extra_bed_list.append(i)
            RB = Checkbutton(self, variable = var)
            self.room_choice_vars.append(var)
            RB.grid(row = i + 2, column = 5)
        self.cost_var.set(presenter.calc_cost(start_date, end_date, pop_list, self.extra_bed_list))

class CancelReservationPage1(Frame):
    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        Label(self, text = "Cancel Reservation", font = TITLE_FONT).grid(row = 0, column = 1)
        Label(self, text = "Reservation ID", font = Main_Font).grid(row = 1, column = 0)
        self.res_id_var = IntVar()
        Entry(self, width = 10, textvariable = self.res_id_var).grid(row = 1, column = 1)
        Button(self, text = "Search", relief = RAISED, command=lambda: presenter.get_cancel_reserv(self.res_id_var.get())).grid(row = 1, column = 2)

class CancelReservationPage2(Frame):
    def __init__(self, parent, presenter, resid, pop_list, start_date, end_date, total_cost):
        Frame.__init__(self, parent)
        Label(self, text = "Start Date", font = Main_Font).grid(row = 0, column = 0)
        Label(self, text = "End Date", font = Main_Font).grid(row = 0, column = 3)
        self.start_date_var = StringVar()
        self.start_date_var.set(start_date)
        self.end_date_var = StringVar()
        self.end_date_var.set(end_date)
        Entry(self, textvariable = self.start_date_var).grid(row = 0, column = 1, columnspan = 2)
        Entry(self, textvariable = self.end_date_var, width = 10).grid(row = 0, column = 4, columnspan = 2)
        Label(self, text = "Room Number", font = Main_Font).grid(row = 1, column = 0)
        Label(self, text = "Room Category", font = Main_Font).grid(row = 1, column = 1)
        Label(self, text = "# of People Allowed", font = Main_Font).grid(row = 1, column = 2)
        Label(self, text = "Cost Per Day", font = Main_Font).grid(row = 1, column = 3)
        Label(self, text = "Cost of Extra Bed Per Day", font = Main_Font).grid(row = 1, column = 4)
        Label(self, text = "Select Extra Bed", font = Main_Font).grid(row = 1, column = 5)

        # view_list = [(x[10], x[12], x[13], x[14], "") for x in pop_list]

        n = pop_list
        # this will be populated with rooms ill use n for now
        colcount = -1
        rowcount = 1
        for i in n:
            rowcount = rowcount + 1
            colcount = -1
            for value in i:
                colcount = colcount + 1
                Label(self, text = value, font = Main_Font).grid(row = rowcount, column = colcount)

        self.room_choice_vars = []
        self.room_choice = IntVar()
        for i in range(len(n)):
            var = IntVar()
            RB = Checkbutton(self, variable = var)
            self.room_choice_vars.append(var)
            RB.grid(row = i + 2, column = 5)


        Label(self, text = "Total Cost of Reservation", font = Main_Font).grid(row = len(n) + 2, column = 1, columnspan = 2)
        Label(self, text = "Date of Cancellation", font = Main_Font).grid(row = len(n) + 3, column = 1, columnspan = 2)
        Label(self, text = "Amount to be refunded", font = Main_Font).grid(row = len(n) + 4, column = 1 , columnspan = 2)

        self.total_cost_var = IntVar()
        self.total_cost_var.set(total_cost)
        self.cancel_date_var = StringVar()
        self.cancel_date_var.set(time.strftime("%x"))

        #set to current date
        self.refund_var = IntVar()
        self.refund_var.set(presenter.calc_refund(start_date, end_date, total_cost))

        Entry(self, textvariable = self.total_cost_var).grid(row = len(n) + 2, column = 3, columnspan = 2)
        Entry(self, textvariable = self.cancel_date_var).grid(row = len(n) + 3, column = 3, columnspan = 2)
        Entry(self, textvariable = self.refund_var).grid(row = len(n) + 4, column = 3, columnspan = 2)

        Button(self, text = "Cancel Reservation", font = Main_Font, relief = RAISED, command=lambda: presenter.cancel_reservation(resid)).grid(row = len(n) + 5, column = 4)
        #need cancel button?


class ViewReviewPage1(Frame):
    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        Label(self, text = "View Review", font = TITLE_FONT).grid(row  = 0, column = 1)
        Label(self, text = "").grid(row = 1, column = 0)
        Label(self, text = "Hotel Location", font = Main_Font).grid(row = 2, column = 0)
        self.location = StringVar()
        locations = OptionMenu(self,self.location, "Atlanta", "Charlotte", "Savannah", "Orlando", "Miami")
        locations.configure(width = 20, font = Main_Font)
        locations.grid(row = 2, column = 1)
        Button(self, text = "Check Reviews", font = Main_Font, relief = RAISED, command=lambda: presenter.get_reviews(self.location.get())).grid(row = 3, column = 2)

class ViewReviewPage2(Frame):
    def __init__(self, parent, presenter, pop_list):
        Frame.__init__(self, parent)
        Label(self, text = "Rating", font = Main_Font).grid(row = 0, column = 0)
        Label(self, text = "Comment", font = Main_Font).grid(row = 0, column = 1)
        n = pop_list
        # this will be populated with reviews ill use n for now
        colcount = -1
        rowcount = 1
        for i in n:
            rowcount = rowcount + 1
            colcount = -1
            for value in i:
                colcount = colcount + 1
                Label(self, text = value, font = Main_Font).grid(row = rowcount, column = colcount)

        Button(self, text = "Back", font = Main_Font, relief = RAISED,command=lambda: presenter.show_frame(ViewReviewPage1)).grid(row = len(n) + 2, column = 1)


class GiveReviewPage(Frame):
    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        Label(self, text = "Give Review", font = TITLE_FONT).grid(row = 0, column = 1)
        Label(self, text = "").grid(row = 1, column = 0)
        Label(self, text = "Hotel Location", font = Main_Font).grid(row = 2, column = 0)
        Label(self, text = "").grid(row = 3, column = 0)
        Label(self, text = "Rating", font = Main_Font).grid(row = 4, column = 0)
        Label(self, text = "").grid(row = 5, column = 0)
        Label(self, text = "Comment", font = Main_Font).grid(row = 6, column = 0)
        Label(self, text = "").grid(row = 7, column = 0)

        self.location = StringVar()
        locations = OptionMenu(self,self.location, "Atlanta", "Charlotte", "Savannah", "Orlando", "Miami")
        locations.configure(font = Main_Font, width = 20)
        locations.grid(row = 2, column = 1)

        self.rating = StringVar()
        ratings = OptionMenu(self, self.rating, "Excellent", "Good","Neutral",  "Bad", "Very Bad")
        ratings.configure(font = Main_Font, width = 20)
        ratings.grid(row = 4, column = 1)

        self.comment_var = StringVar()
        Entry(self, textvariable = self.comment_var).grid(row = 6, column = 1, columnspan = 2)
        Button(self, text = "Submit", font = Main_Font, relief = RAISED, command=lambda: presenter.add_review(self.rating.get(), self.location.get(), self.comment_var.get())).grid(row = 8, column = 2)

class ReservationReport(Frame):
    def __init__(self, parent, presenter, pop_list):
        Frame.__init__(self, parent)

        self.canvas = Canvas(self, borderwidth = 0)
        self.frame = Frame(self.canvas)
        self.vsb = Scrollbar(self, orient = VERTICAL, command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.vsb.set)
        self.vsb.pack(side = RIGHT, fill = Y)
        self.canvas.pack(side = LEFT, fill = BOTH, expand = True)
        self.canvas.create_window((4,4), window = self.frame, anchor= NW, tags = "self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        Label(self.frame, text = "Reservation Report", font = TITLE_FONT).grid(row = 0, column = 1, columnspan = 2)
        Label(self.frame, text = "").grid(row = 1, column = 0)
        Label(self.frame, text = "Month", font = Main_Font).grid(row = 2, column = 0)
        Label(self.frame, text = "Location", font = Main_Font).grid(row = 2, column = 1)
        Label(self.frame, text = "Total Number of Reservations", font = Main_Font).grid(row = 2, column = 2)
        n = pop_list
        #this will be populated with report info
        colcount = -1
        rowcount = 2
        for i in n:
            rowcount = rowcount + 1
            colcount = -1
            for value in i:
                colcount = colcount + 1
                Label(self.frame, text = value, font = Main_Font).grid(row = rowcount, column = colcount)

        Button(self.frame, text = "Back", font = Main_Font, relief = RAISED,command=lambda: presenter.show_frame(MainPageManager)).grid(row = len(n) + 3, column = 1)

    def onFrameConfigure(self, event):
    	self.canvas.configure(scrollregion = self.canvas.bbox("all"))

class PopularRoom(Frame):
    def __init__(self, parent, presenter, pop_list):
        Frame.__init__(self, parent)
        Label(self, text = "Popular Room Category", font = TITLE_FONT).grid(row = 0, column = 1, columnspan = 3)
        Label(self, text = "").grid(row = 1, column = 0)
        Label(self, text = "Month", font = Main_Font).grid(row = 2, column = 0)
        Label(self, text = "Top Room Category", font = Main_Font).grid(row = 2, column = 1)
        Label(self, text = "Location", font = Main_Font).grid(row = 2, column = 2)
        Label(self, text = "Total Number of Reservations for Room Category", font = Main_Font).grid(row = 2, column = 3)

        n = pop_list
        #this will be populated with report info
        colcount = -1
        rowcount = 2
        for i in n:
            rowcount = rowcount + 1
            colcount = -1
            for value in i:
                colcount = colcount + 1
                Label(self, text = value, font = Main_Font).grid(row = rowcount, column = colcount)

        Button(self, text = "Back", font = Main_Font, relief = RAISED,command=lambda: presenter.show_frame(MainPageManager)).grid(row = len(n) + 3, column = 1)

class RevenueReport(Frame):
    def __init__(self, parent, presenter, pop_list):
        Frame.__init__(self, parent)
        Label(self, text = "Revenue Report", font = TITLE_FONT).grid(row = 0, column = 1, columnspan = 2)
        Label(self, text = "").grid(row = 1, column = 0)
        Label(self, text = "Month", font = Main_Font).grid(row = 2, column = 0)
        Label(self, text = "Location", font = Main_Font).grid(row = 2, column = 1)
        Label(self, text = "Total Revenue", font = Main_Font).grid(row = 2, column = 2)

        n = pop_list
        #this will be populated with report info
        colcount = -1
        rowcount = 2
        for i in n:
            rowcount = rowcount + 1
            colcount = -1
            for value in i:
                colcount = colcount + 1
                Label(self, text = value, font = Main_Font).grid(row = rowcount, column = colcount)

        Button(self, text = "Back", font = Main_Font, relief = RAISED,command=lambda: presenter.show_frame(MainPageManager)).grid(row = len(n) + 3, column = 1)
