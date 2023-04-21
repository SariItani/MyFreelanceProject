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
import passenger_management.enter_civil_id as e
import passenger_management.see_report as s


class CustomsOfficerScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.geometry("350x150")
        self.master.title("Customs Officer Screen")
        self.configure(background='grey') # set the background color
        self.pack(fill='both', expand=True)

        # create enter ID button
        self.enter_id_button = tk.Button(self, text="Enter ID", command=self.enter_id)
        self.enter_id_button.pack()

        # create see report button
        self.see_report_button = tk.Button(self, text="See Report", command=self.see_report)
        self.see_report_button.pack()

    def enter_id(self):
        # create a new window to enter ID
        self.enter_id_window = tk.Toplevel(self.master)
        self.enter_id_window.title("Enter ID")
        self.enter_id_window.geometry("200x100")

        # create ID label and entry widget
        self.id_label = tk.Label(self.enter_id_window, text="Civil ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(self.enter_id_window)
        self.id_entry.pack()

        # create options label and radio buttons
        self.options_label = tk.Label(self.enter_id_window, text="Select action:")
        self.options_label.pack()
        self.action_var = tk.StringVar()
        self.green_channel_button = tk.Radiobutton(self.enter_id_window, text="Allow through Green channel", variable=self.action_var, value="green_channel")
        self.green_channel_button.pack()
        self.self_declared_button = tk.Radiobutton(self.enter_id_window, text="Passenger self-declared Items", variable=self.action_var, value="self_declared")
        self.self_declared_button.pack()
        self.inspect_items_button = tk.Radiobutton(self.enter_id_window, text="Inspect items", variable=self.action_var, value="inspect_items")
        self.inspect_items_button.pack()

        # create submit button
        self.submit_button = tk.Button(self.enter_id_window, text="Submit", command=self.submit_action)
        self.submit_button.pack()

    def submit_action(self):
        civil_id = self.id_entry.get()
        action = self.action_var.get()
        fines = 0

        # Update fines based on the selected action
        if action == "inspect_items":
            fines = int(input("Enter fines amount (0 to 20000): "))
            if fines < 0 or fines > 20000:
                messagebox.showerror("Invalid Fines", "Fines amount must be between 0 and 20000.")
                return

        # Update passenger file with the new fines amount
        with open("database/passengers.txt", "r") as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                if len(row) >= 4 and row[0] == civil_id:
                    row[3] = str(int(row[3]) + fines)
                rows.append(row)

        with open("database/passengers.txt", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        messagebox.showinfo("Fines Updated", f"Fines of {fines} KD have been added to passenger with ID {civil_id}")

        # close the enter ID window
        self.enter_id_window.destroy()

    def see_report(self):
        # TODO: Implement this method to show the fines report for customs officers
        pass

    def logout(self):
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.master.withdraw()
            l.LoginScreen(tk.Tk())
