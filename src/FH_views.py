from FH_presenter import *
from tkinter import *
import pymysql

TITLE_FONT = ("Times", 20, "italic")
Main_Font = ("Times", 14)

class LoginPage(Frame):

    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        loglabel = Label(self, text="Login Page", font=TITLE_FONT)
        loglabel.grid(row = 1, column = 1, columnspan = 2, sticky = N+S+E+W)

        photo = PhotoImage(file = "crest.gif")
        header = Label(self, image = photo)
        header.image= photo
        header.grid(row=0, column =  1, columnspan = 2)


        Label(self, text = "").grid(row = 2, column = 0)

        self.uservar = StringVar()
        self.pwordvar = StringVar()


        user = Label(self, text = "Username", font = Main_Font)
        user.grid(row = 3, column = 0)

        password = Label(self, text = "Password",font = Main_Font)
        password.grid(row = 4, column = 0)

        e_user = Entry(self, width = 30, textvariable = self.uservar)
        e_user.grid(row = 3, column = 1)

        e_password = Entry(self, width = 30, textvariable = self.pwordvar)
        e_password.grid(row = 4, column = 1)

        login_button = Button(self, text="Login", font = Main_Font, relief = RAISED, command=lambda: presenter.show_frame(MainPageCustomer))
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
        Entry(self, width = 20, textvariable = password).grid(row = 5, column = 1)
        Entry(self, width = 20, textvariable = confirmPassword).grid(row = 6, column = 1)
        Entry(self, width = 20, textvariable = email).grid(row = 7, column = 1)

        Label(self, text = "").grid(row =8)

        button = Button(self, text="Submit",font = Main_Font, relief = RAISED,
                           command=lambda: presenter.register(username.get(), confirmPassword.get(), password.get(), email.get(), RegisterPage))
        button.grid(row = 9, column = 1)

class MainPageCustomer(Frame):

    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)

        photo = PhotoImage(file = "crest.gif")
        header = Label(self, image = photo)
        header.image= photo
        header.grid(row=0, column =  0, columnspan = 2)


        label = Label(self, text="Choose Functionality", font=TITLE_FONT)
        label.grid(column = 0, row = 1, columnspan = 2)

        Label(self, text = "Welcome!", font = ("Times",18)).grid(row = 3, column = 0)
        Button(self, text = "Make a New Reservation",font = Main_Font, relief = FLAT, command=lambda: presenter.show_frame(SearchRooms)).grid(row = 4, column = 0)
        Button(self, text = "Update your reservation",font = Main_Font, relief = FLAT, command=lambda: presenter.show_frame(UpdateReservationPage1)).grid(row = 5, column = 0)
        Button(self, text = "Cancel Reservation",font = Main_Font, relief = FLAT).grid(row = 6, column = 0)
        Button(self, text = "Provide Feedback",font = Main_Font, relief = FLAT).grid(row = 7, column = 0)
        Button(self, text = "View Feedback",font = Main_Font, relief = FLAT).grid(row = 8, column = 0)

        button = Button(self, text="Go to the Login page",font = Main_Font,
                           command=lambda: presenter.show_frame(LoginPage))
        button.grid(row = 9, column = 0)




class MainPageManager(Frame):

    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        Label(self, text = "Choose Functionality", font = TITLE_FONT).grid(row = 1, column = 0, columnspan = 2)
        Label(self, text = "Welcome!", font = ("Times", 18)).grid(row = 2, column = 0)
        Button(self, text = "View Reservation Report",font = Main_Font, relief = FLAT).grid(row = 3, column = 0)
        Button(self, text = "View Popular Room Category Report",font = Main_Font, relief = FLAT).grid(row = 4, column = 0)
        Button(self, text = "View Revenue Report",font = Main_Font, relief = FLAT).grid(row = 5, column = 0)
        Button(self, text="Go to the Login page",font = Main_Font,
                           command=lambda: presenter.show_frame(LoginPage)).grid(row = 6, column = 0)
        photo = PhotoImage(file = "crest.gif")
        header = Label(self,image=photo)
        header.image = photo
        header.grid(row = 0, column = 0, columnspan =2)

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
        Button(self, text = "Search",font = Main_Font, relief = RAISED, command = lambda: presenter.show_frame(MakeReservations)).grid(row = 6, column = 3)

        self.location = StringVar()
        locations = OptionMenu(self,self.location, "Atlanta", "Charlotte", "Savannah", "Orlando", "Miami")
        locations.configure(width = 20, font = Main_Font)
        locations.grid(row = 2, column = 1)

class MakeReservations(Frame):
    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        Label(self, text = "Make Reservations", font = TITLE_FONT).grid(row = 0, column = 2, columnspan = 2)
        Label(self, text = "Room Number", font = Main_Font).grid(row = 1, column = 0)
        Label(self, text = "Room Category", font = Main_Font).grid(row = 1, column = 1)
        Label(self, text = "# of People Allowed", font = Main_Font).grid(row = 1, column = 2)
        Label(self, text = "Cost Per Day", font = Main_Font).grid(row = 1, column = 3)
        Label(self, text = "Cost of Extra Bed Per Day", font = Main_Font).grid(row = 1, column = 4)
        Label(self, text = "Select Room", font = Main_Font).grid(row = 1, column = 5)

        mylocation = "Atlanta"
        mystart = "11/20/2015"
        myend = "11/25/2015"

        self.cnx = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_76", passwd="YlVIp1tI", db="cs4400_Group_76")
        cursor = self.cnx.cursor()
        sql = """ SELECT Hroomnum, Hlocation FROM Reservation_Has_Room WHERE Hlocation = "{}" """.format(mylocation)
        cursor.execute(sql)
        occupied_room_data = list(cursor.fetchall())
        self.cnx.commit()
        cursor.close()

        cursor2 = self.cnx.cursor()
        sql2 = """ SELECT roomnum, location FROM Room WHERE location = "{}" """.format(mylocation)
        cursor2.execute(sql2)
        room_data = list(cursor2.fetchall())
        self.cnx.commit()
        cursor2.close


        open_room_data = []

        for x in room_data:
            if x not in occupied_room_data:
                open_room_data.append(x)

        cursor3 = self.cnx.cursor()
        sql3 = "SELECT * FROM Room"
        cursor3.execute(sql3)
        all_room_info = list(cursor3.fetchall())
        self.cnx.commit()
        cursor3.close()


        my_room_info = []

        for x in all_room_info:
            for y in open_room_data:
                if x[0:2] == y:
                    my_room_info.append(x)


        cursor4 = self.cnx.cursor()
        sql4 = """ SELECT * FROM Extra_Bed WHERE Rlocation = "{}" """.format(mylocation)
        cursor4.execute(sql4)
        extra_bed_info = list(cursor4.fetchall())
        self.cnx.commit()
        cursor4.close()


        complete_room_info = []

        for x in my_room_info:
            for y in extra_bed_info:
                if x[0:2] == y[0:2]:
                    roomvalue = x[:]
                    bedvalue = (y[2],)
                    final = roomvalue + bedvalue
                    complete_room_info.append(final)

        colcount = -1
        rowcount = 1


        for i in complete_room_info:
            rowcount = rowcount + 1
            colcount = -1
            for value in i:
                if value == "Atlanta" or value == "Orlando" or value == "Savannah" or value == "Charlotte" or value == "Miami":
                    pass
                else:
                    colcount = colcount + 1
                    Label(self, text = value, font = Main_Font).grid(row = rowcount, column = colcount)

        self.room_choice_vars = []

        for i in range(len(complete_room_info)):
            var = IntVar()
            RB = Checkbutton(self, variable = var)
            self.room_choice_vars.append(var)
            RB.grid(row = i + 2, column = 5)

        Button(self, text = "Check Details", font = Main_Font, command = lambda: presenter.show_frame(MakeReservationDrop)).grid(row = len(complete_room_info)+2, column = 5)



        self.populate_list(complete_room_info)
        self.room_choice = IntVar()

        for i in range(len(complete_room_info)):
            RB = Radiobutton(self, variable = self.room_choice, value = i + 1)
            RB.grid(row = i + 2, column = 5)



    def populate_list(self, to_populate):
        colcount = -1
        rowcount = 1
        for i in to_populate:
            rowcount = rowcount + 1
            colcount = -1
            for value in i:
                if value == "Atlanta" or value == "Orlando" or value == "Savannah" or value == "Charlotte" or value == "Miami":
                    pass
                else:
                    colcount = colcount + 1
                    Label(self, text = value, font = Main_Font).grid(row = rowcount, column = colcount)


class MakeReservationDrop(Frame):
	def __init__(self, parent, presenter):
		Frame.__init__(self, parent)
		Label(self, text = "Room Number", font = Main_Font).grid(row = 0, column = 0)
		Label(self, text = "Room Category", font = Main_Font).grid(row = 0, column = 1)
		Label(self, text = "# of People Allowed", font = Main_Font).grid(row = 0, column = 2)
		Label(self, text = "Cost Per Day", font = Main_Font).grid(row = 0, column = 3)
		Label(self, text = "Cost of Extra Bed Per Day", font = Main_Font).grid(row = 0, column = 4)
		Label(self, text = "Select Room", font = Main_Font).grid(row = 0, column = 5)

		
		n =[]
		#The part part of this will contain the list of checked rooms for now I'll use n 
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
		self.end_date_var = StringVar()
		self.total_cost_var = StringVar()
		
		Entry(self, textvariable = self.start_date_var).grid(row = len(n)+ 2, column = 1, columnspan = 2)
		Entry(self, textvariable = self.end_date_var).grid(row = len(n) + 2, column = 4, columnspan = 2)
		Entry(self, textvariable = self.total_cost_var).grid(row = len(n) + 3, column = 1, columnspan = 2)
		
		self.credit_card = StringVar()
		options = [ "hey", "bye" ]
		#these are just test values this would be the populated list of credit cards
		credit_card = OptionMenu (self, self.credit_card, *options)
		credit_card.configure(font = Main_Font)
		credit_card.grid(row = len(n)+ 4, column = 1, columnspan = 2)
		
		Button(self, text = "Add Card", font = Main_Font, relief = FLAT, command = lambda: presenter.show_frame(PaymentPage)).grid(row = len(n) + 4, column = 3)
		Button(self, text = "Submit", font = Main_Font, command = lambda: presenter.show_frame(ConfirmationPage)).grid(row =len(n) + 5, column = 4)
		

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
		
		options = [ "hi", "bye"]
		self.credit_card = StringVar()
		# test values this will be populated list of credit cards
		credit_card = OptionMenu (self, self.credit_card, *options)
		credit_card.configure(width = 20, font = Main_Font)
		credit_card.grid(row = 3, column = 3)
		
		Button(self, text = "Save", font = Main_Font).grid(row = 8, column = 0)
		Button(self, text = "Delete", font = Main_Font).grid(row = 8, column = 3)

class ConfirmationPage(Frame):
	def __init__(self, parent, presenter):
		Frame.__init__(self, parent)	
		Label(self, text = "Confirmation Screen", font = TITLE_FONT).grid(row = 0, column = 0, columnspan = 2)
		Label(self, text = "").grid(row = 1, column = 0)
		Label(self, text = "Your Reservation ID", font = Main_Font).grid(row = 2, column = 0)
		Label(self, text = "").grid(row = 3, column = 0)
		Label(self, text = "").grid(row = 4, column = 0)
		Label(self, text = "Please save this reservation id for all further communication", font = ("Times", 10)).grid(row = 5, column = 0, columnspan = 2)
		
		self.confirm_var = IntVar()
		
		Entry(self, textvariable = self.confirm_var, width = 10).grid(row = 2, column = 1)

class UpdateReservationPage1(Frame):
	def __init__(self, parent, presenter):
		Frame.__init__(self, parent)
		Label(self, text = "Update Reservation", font = TITLE_FONT).grid(row = 0, column = 1)
		Label(self, text = "").grid(row = 1, column = 0)
		Label(self, text = "Reservation ID", font = Main_Font).grid(row = 2, column = 0)
		
		self.res_id_var = IntVar()
		Entry(self, textvariable = self.res_id_var, width = 10).grid(row = 2, column = 1)
		
		Button(self, text = "Search", font= Main_Font, command=lambda: presenter.show_frame(UpdateReservationPage2)).grid(row = 2, column = 2)

class UpdateReservationPage2(Frame):
	def __init__(self, parent, presenter):
		Frame.__init__(self, parent)
		Label(self, text = "Current Start Date", font = Main_Font).grid(row = 0, column = 0)
		Label(self, text = "Current End Date", font = Main_Font).grid(row = 0, column = 2)
		Label(self, text = "").grid(row = 1, column = 0)
		Label(self, text = "New Start Date", font = Main_Font).grid(row = 2, column = 0)
		Label(self, text = "New End Date", font = Main_Font).grid(row = 2, column = 2)
		Label(self, text = "").grid(row = 3, column = 0)
		
		self.current_start_var = StringVar()
		self.current_end_var = StringVar()
		self.new_start_var = StringVar()
		self.new_end_var = StringVar()
		
		Entry(self, textvariable = self.current_start_var, width = 10).grid(row = 0, column = 1)
		Entry(self, textvariable = self.current_end_var, width = 10).grid(row = 0, column = 3)
		Entry(self, textvariable = self.new_start_var, width = 10).grid(row = 2, column = 1)
		Entry(self, textvariable = self.new_end_var, width = 10).grid(row = 2, column = 3)
		
		Button(self, text = "Search Availability", font = Main_Font, command=lambda: presenter.show_frame(UpdateReservationPage3)).grid(row = 4, column = 1, columnspan = 2)
		
class UpdateReservationPage3(Frame):
	def __init__(self, parent, presenter):
		Frame.__init__(self, parent)
		Label(self, text = "Room are available. Please confirm details below before submitting", font = Main_Font).grid(row = 0, column = 0, columnspan = 5)
		Label(self, text = "Room Number", font = Main_Font).grid(row = 1, column = 0)
		Label(self, text = "Room Category", font = Main_Font).grid(row = 1, column = 1)
		Label(self, text = "# of People Allowed", font = Main_Font).grid(row = 1, column = 2)
		Label(self, text = "Cost Per Day", font = Main_Font).grid(row = 1, column = 3)
		Label(self, text = "Cost of Extra Bed Per Day", font = Main_Font).grid(row = 1, column = 4)
		Label(self, text = "Select Room", font = Main_Font).grid(row = 1, column = 5)

		
		n = []
		# this will be populated with available rooms ill use n for now
		
		for i in n:
			rowcount = rowcount + 1
			colcount = -1
			for value in i:
				colcount = colcount + 1
				Label(self, text = value, font = Main_Font).grid(row = rowcount, column = colcount)
		
		Label(self, text = "Total Cost Updated", font = Main_Font).grid(row = len(n) + 2, column = 0, columnspan = 2)
		self.cost_var = IntVar()
		Entry(self, textvariable = self.cost_var, width = 10).grid(row = len(n) + 2, column = 2)
		Button(self, text = "Submit", font = Main_Font).grid(row = len(n) + 3, column = 5)
		
		