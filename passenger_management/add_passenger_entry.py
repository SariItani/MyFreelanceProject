import tkinter as tk
from tkinter import ttk
import csv

class AddPassengerEntry(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry("300x200")
        self.title("Add New Passenger")

        # create labels and entry widgets
        self.civil_id_label = tk.Label(self, text="Civil ID")
        self.civil_id_entry = tk.Entry(self)

        self.name_label = tk.Label(self, text="Name")
        self.name_entry = tk.Entry(self)

        self.dob_label = tk.Label(self, text="Date of Birth")
        self.dob_entry = tk.Entry(self)

        self.gender_label = tk.Label(self, text="Gender")
        self.gender_entry = tk.Entry(self)

        # create button widgets
        self.add_button = tk.Button(self, text="Add Passenger", command=self.add_passenger)
        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy)

        # place widgets on the form
        self.civil_id_label.grid(row=0, column=0, padx=5, pady=5)
        self.civil_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.name_label.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.dob_label.grid(row=2, column=0, padx=5, pady=5)
        self.dob_entry.grid(row=2, column=1, padx=5, pady=5)

        self.gender_label.grid(row=3, column=0, padx=5, pady=5)
        self.gender_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button.grid(row=4, column=0, padx=5, pady=5)
        self.cancel_button.grid(row=4, column=1, padx=5, pady=5)

    def add_passenger(self):
        # get input values from user
        civil_id = self.civil_id_entry.get()
        name = self.name_entry.get()
        dob = self.dob_entry.get()
        gender = self.gender_entry.get()

        # create string in required format
        passenger_str = f"{civil_id},{name},{dob},{gender},0,Pending\n"

        # write passenger string to the passengers.txt file
        with open("database/passengers.txt", "a") as f:
            f.write(passenger_str)

        # display success message and close the form
        tk.messagebox.showinfo("Success", "Passenger added successfully!")
        self.destroy()
