import csv
import tkinter as tk
from tkinter import ttk


def see_report(self):
    # read passenger data from file and calculate total fines and number of passengers
    total_fines = 0
    num_passengers = 0
    passengers_with_fine_greater_than_5000 = []
    with open("database/passengers.txt", "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            num_passengers += 1
            fines = int(row[3])
            total_fines += fines
            if fines > 5000:
                passengers_with_fine_greater_than_5000.append(row)

    # calculate average fine per passenger
    if num_passengers == 0:
        average_fine_per_passenger = 0
    else:
        average_fine_per_passenger = total_fines / num_passengers

    # create a new window to show the report
    self.report_window = tk.Toplevel(self.master)
    self.report_window.title("Customs Fine Report")
    self.report_window.geometry("500x400")

    # create labels for the report metrics
    total_fines_label = tk.Label(self.report_window, text=f"Total Customs Fine Collected: {total_fines} KD")
    total_fines_label.pack()
    average_fine_label = tk.Label(self.report_window, text=f"Average Fine per Passenger: {average_fine_per_passenger:.2f} KD")
    average_fine_label.pack()

    # create a table to show passengers with fines greater than 5000
    if passengers_with_fine_greater_than_5000:
        table_label = tk.Label(self.report_window, text="Passengers with Fine greater than 5000 KD:")
        table_label.pack()
        table = ttk.Treeview(self.report_window, columns=("name", "age", "nationality", "fines"))
        table.heading("#0", text="Civil ID")
        table.heading("name", text="Name")
        table.heading("age", text="Age")
        table.heading("nationality", text="Nationality")
        table.heading("fines", text="Fines (KD)")
        for row in passengers_with_fine_greater_than_5000:
            table.insert("", "end", text=row[0], values=(row[1], row[2], row[4], row[3]))
        table.pack()
    else:
        no_passengers_label = tk.Label(self.report_window, text="No passengers with fine greater than 5000 KD.")
        no_passengers_label.pack()

    # create a close button to close the report window
    close_button = tk.Button(self.report_window, text="Close", command=self.report_window.destroy)
    close_button.pack()
