from FH_presenter import *
from tkinter import *

TITLE_FONT = ("Helvetica", 18, "bold")

class StartPage(Frame):

    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        label = Label(self, text="This is the start page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text="Go to Page One",
                            command=lambda: presenter.show_frame(PageOne))
        button2 = Button(self, text="Go to Page Two",
                            command=lambda: presenter.show_frame(PageTwo))
        button1.pack()
        button2.pack()

class PageOne(Frame):

    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        label = Label(self, text="This is page 1", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page",
                           command=lambda: presenter.show_frame(StartPage))
        button.pack()

class PageTwo(Frame):

    def __init__(self, parent, presenter):
        Frame.__init__(self, parent)
        label = Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page",
                           command=lambda: presenter.show_frame(StartPage))
        button.pack()
