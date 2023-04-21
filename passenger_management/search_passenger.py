import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class SearchPassenger(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Search Passenger")
        self.geometry("300x300")
        self.resizable(False, False)

        # create labels to display passenger details
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack(pady=5)

        self.age_label = tk.Label(self, text="Date of Birth:")
        self.age_label.pack(pady=5)

        self.gender_label = tk.Label(self, text="Gender:")
        self.gender_label.pack(pady=5)

        self.fines_label = tk.Label(self, text="Fines:")
        self.fines_label.pack(pady=5)

        self.status_label = tk.Label(self, text="Status:")
        self.status_label.pack(pady=5)

        # create a label and entry for Civil ID
        id_label = tk.Label(self, text="Enter Civil ID:")
        id_label.pack(pady=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.pack(pady=5)

        # create a button to search for passenger
        search_button = tk.Button(self, text="Search", command=self.search_passenger)
        search_button.pack(pady=5)
        
        # create a button to close the popup window
        cancel_button = tk.Button(self, text="Go Back", command=self.destroy)
        cancel_button.pack(pady=5)

    def search_passenger(self):
        # convert the information in database/passengers.txt to a dictionary
        with open("database/passengers.txt", "r") as file:
            passenger_data = file.readlines()
        passenger_dict = {}
        for passenger in passenger_data:
            passenger = passenger.strip().split(",")
            passenger_dict[passenger[0]] = passenger[1:]

        # check if the ID exists in the dictionary
        if self.id_entry.get() not in passenger_dict:
            messagebox.showerror("Error", "Civil ID not found.")
        else:
            # update the labels with passenger details
            self.name_label.config(text=f"Name: {passenger_dict[self.id_entry.get()][0]}")
            self.age_label.config(text=f"Date of Birth: {passenger_dict[self.id_entry.get()][1]}")
            self.gender_label.config(text=f"Gender: {passenger_dict[self.id_entry.get()][2]}")
            self.fines_label.config(text=f"Fines: {passenger_dict[self.id_entry.get()][3]}")
            self.status_label.config(text=f"Status: {passenger_dict[self.id_entry.get()][4]}")
