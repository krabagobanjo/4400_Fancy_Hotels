from tkinter import *
from FH_presenter import *
from FH_model import *

def main():
    dbmodel = FH_dbmodel()
    app = FH_presenter(dbmodel)
    app.protocol("WM_DELETE_WINDOW", lambda: callback(app, dbmodel))
    app.mainloop()

def callback(app, dbmodel):
    dbmodel.close_connection()
    app.destroy()

if __name__ == "__main__":
    main()
