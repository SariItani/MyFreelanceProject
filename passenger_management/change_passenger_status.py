import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class ChangePassengerStatus(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Change Passenger Status")
        self.geometry("280x250")
        self.resizable(False, False)

        # create a label and entry for Civil ID
        id_label = tk.Label(self, text="Enter Civil ID:")
        id_label.pack(pady=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.pack(pady=5)

        # create a label and dropdown for selecting status
        status_label = tk.Label(self, text="Select Status:")
        status_label.pack(pady=5)
        self.status_var = tk.StringVar()
        status_dropdown = tk.OptionMenu(self, self.status_var, "Arrival Approved", "Arrival Rejected", "Departure Approved", "Departure Rejected")
        status_dropdown.pack(pady=5)

        # create a button to close the popup window
        cancel_button = tk.Button(self, text="Go Back", command=self.destroy)
        cancel_button.pack(pady=5)

        # create a button to submit the status
        submit_button = tk.Button(self, text="Submit", command=self.update_status)
        submit_button.pack(pady=5)

    def update_status(self):
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
            # update the passenger's status in the dictionary
            passenger_dict[self.id_entry.get()][-1] = self.status_var.get()
            # write the updated information back to database/passengers.txt
            with open("database/passengers.txt", "w") as file:
                for id_, info in passenger_dict.items():
                    file.write(id_ + "," + ",".join(info) + "\n")
            # close the popup window
            messagebox.showinfo("Success", "Passenger status has been updated.")
            self.destroy()
