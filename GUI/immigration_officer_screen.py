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
import passenger_details_screen
import new_passenger_screen
import search_passenger_screen

class ImmigrationOfficerScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # create and place widgets
        self.label = tk.Label(self, text="Immigration Officer Screen")
        self.label.pack()

        self.button = tk.Button(self, text="Logout", command=self.logout)
        self.button.pack()

    def logout(self):
        # handle logout button press
        pass
