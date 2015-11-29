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
        Button(self, text = "Update your reservation",font = Main_Font, relief = FLAT).grid(row = 5, column = 0)
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
        Button(self, text = "Search",font = Main_Font, relief = RAISED, command = lambda: presenter.get_avail_rooms1(self.location.get(), self.startdate.get(), self.enddate.get())).grid(row = 6, column = 3)
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

    def populate_list(self, to_populate):
        colcount = -1
        rowcount = 1
        self.room_choice_vars = []
        self.room_choice = IntVar()
        for i in to_populate:
            rowcount = rowcount + 1
            colcount = -1
            for value in i:
                if value == "Atlanta" or value == "Orlando" or value == "Savannah" or value == "Charlotte" or value == "Miami":
                    pass
                else:
                    colcount = colcount + 1
                    Label(self, text = value, font = Main_Font).grid(row = rowcount, column = colcount)
        for i in range(len(to_populate)):
            var = IntVar()
            RB = Checkbutton(self, variable = var)
            self.room_choice_vars.append(var)
            RB.grid(row = i + 2, column = 5)

        Button(self, text = "Check Details", font = Main_Font).grid(row = len(to_populate)+2, column = 5)

        for i in range(len(to_populate)):
            RB = Radiobutton(self, variable = self.room_choice, value = i + 1)
            RB.grid(row = i + 2, column = 5)
