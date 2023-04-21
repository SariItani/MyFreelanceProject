import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class SearchPassenger(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Search Passenger")
        self.geometry("300x300")
        self.resizable(False, False)

        # create a label and entry for Civil ID
        id_label = tk.Label(self, text="Enter Civil ID:")
        id_label.pack(pady=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.pack(pady=5)

        # create a button to search for passenger
        search_button = tk.Button(self, text="Search", command=self.search_passenger)
        search_button.pack(pady=5)

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
            # create a new window to display passenger details
            passenger_window = tk.Toplevel(self)
            passenger_window.title("Passenger Details")
            passenger_window.geometry("300x300")
            passenger_window.resizable(False, False)

            # create labels to display passenger details
            details_label = tk.Label(passenger_window, text="Passenger Details:")
            details_label.pack(pady=5)

            name_label = tk.Label(passenger_window, text=f"Name: {passenger_dict[self.id_entry.get()][0]}")
            name_label.pack(pady=5)

            age_label = tk.Label(passenger_window, text=f"Age: {passenger_dict[self.id_entry.get()][1]}")
            age_label.pack(pady=5)

            gender_label = tk.Label(passenger_window, text=f"Gender: {passenger_dict[self.id_entry.get()][2]}")
            gender_label.pack(pady=5)

            status_label = tk.Label(passenger_window, text=f"Status: {passenger_dict[self.id_entry.get()][3]}")
            status_label.pack(pady=5)
