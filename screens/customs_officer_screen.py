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
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from login_screen import LoginScreen
import passenger_management.enter_civil_id as e
import passenger_management.see_report as s


class CustomsOfficerScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Customs Officer Screen")
        self.master.geometry("220x150")
        self.pack()

        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        self.passenger_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Passenger", menu=self.passenger_menu)
        self.passenger_menu.add_command(label="Enter Civil ID", command=self.enter_civil_id)
        self.passenger_menu.add_command(label="See Report", command=self.see_report)
        self.passenger_menu.add_separator()
        self.passenger_menu.add_command(label="Logout", command=self.logout)

    def enter_civil_id(self):
        e.EnterCivilID(self.master)

    def see_report(self):
        s.SeeReport(self.master)

    def logout(self):
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.master.withdraw()
            LoginScreen(tk.Tk())
