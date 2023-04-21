import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv

class SeeReport(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("See Report")
        self.geometry("300x300")
        self.resizable(False, False)

        # create labels to display metrics
        total_fine_label = tk.Label(self, text="Total Customs Fine Collected: ")
        total_fine_label.pack(pady=5)

        avg_fine_label = tk.Label(self, text="Average Fine Per Passenger: ")
        avg_fine_label.pack(pady=5)

        high_fine_label = tk.Label(self, text="Passengers with Fine Greater Than 5000 KD: ")
        high_fine_label.pack(pady=5)

        # create go back button
        self.go_back_button = tk.Button(self, text="Go Back", command=self.destroy)
        self.go_back_button.pack()

        # read passenger data from database/passengers.csv
        with open("database/passengers.csv", "r") as file:
            passenger_data = csv.reader(file)
            next(passenger_data) # skip header row

            # calculate metrics
            total_fine = 0
            num_passengers = 0
            high_fine_passengers = []
            for passenger in passenger_data:
                fine = int(passenger[4])
                total_fine += fine
                num_passengers += 1
                if fine > 5000:
                    high_fine_passengers.append(passenger)

            avg_fine = total_fine / num_passengers

            # update label values with metrics
            total_fine_label.config(text=f"Total Customs Fine Collected: {total_fine} KD")
            avg_fine_label.config(text=f"Average Fine Per Passenger: {avg_fine:.2f} KD")
            high_fine_label.config(text=f"Passengers with Fine Greater Than 5000 KD: {len(high_fine_passengers)}")