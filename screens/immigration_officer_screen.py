# show following option menu:
    # 1. Existing passenger
    # see lsit of values related to Civil ID
    # select one of following options,
    # A. Arrival Approved
    # B. Arrival Rejected
    # C. Departure Approved
    # D. Departure Rejected
    # E. Go Back to previous menu
    # Now we change status to Departed or Arrived accordingly.
    # 2. New passenger
    # add new entry to passenger.txt: Civil ID, Name, Date of Birth, Gender, Customs Fine, and Status
    # 3. Search Passenger
    # he/she should be able to see all details of a passenger after entering passenger’s Civil ID.
    # 4. Logout
    # call login scene
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from screens import login_screen as l
import passenger_management.add_passenger_entry as a
import passenger_management.search_passenger as s
import passenger_management.change_passenger_status as c

class ImmigrationOfficerScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Immigration Officer Screen")
        self.master.geometry("350x150")
        self.pack()

        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        self.passenger_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Passenger", menu=self.passenger_menu)
        self.passenger_menu.add_command(label="Existing Passenger", command=self.change_passenger_status)
        self.passenger_menu.add_command(label="New Passenger", command=self.add_passenger_entry)
        self.passenger_menu.add_command(label="Search Passenger", command=self.search_passenger)
        self.passenger_menu.add_separator()
        self.passenger_menu.add_command(label="Logout", command=self.logout)

    def change_passenger_status(self):
        c.ChangePassengerStatus(self.master)

    def add_passenger_entry(self):
        a.AddPassengerEntry(self.master)

    def search_passenger(self):
        s.SearchPassenger(self.master)

    def logout(self):
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.master.withdraw()
            l.LoginScreen(tk.Tk())
