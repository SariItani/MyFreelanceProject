# show the following option menu:
    # 1. Enter Civil ID
    # he/she should see following options,
    # A. Allow through Green channel 
    # B. Passenger self-declared Items
    # C. Inspect items #add a number to “Customs Fine” field in passenger.txt from 0 to 20,000 KD (user input)
    # D. Go Back to previous menu
    # 2. See Report
    # he/she should see following metrics,
    # i) Total Customs Fine Collected
    # ii) Average fine per passenger
    # iii) Records of passengers with fine greater than 5000 KD
    # 3. Logout
    # call login scene
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from screens import login_screen as l
import passenger_management.see_report as s
import passenger_management.enter_civil_id as e


class CustomsOfficerScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.geometry("350x150")
        self.master.title("Customs Officer Screen")
        self.configure(background='grey') # set the background color
        self.pack(fill='both', expand=True)

        # create menu
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        # create passenger menu
        self.passenger_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Options", menu=self.passenger_menu)
        self.passenger_menu.add_command(label="Enter ID", command=self.enter_id)
        self.passenger_menu.add_command(label="See Report", command=self.see_report)

        # create logout menu
        self.menu.add_command(label="Logout", command=self.logout)

    def enter_id(self):
        e.EnterCivilId(self.master)

    def see_report(self):
        s.SeeReport(self.master)


    def logout(self):
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.master.withdraw()
            l.LoginScreen(tk.Tk())
