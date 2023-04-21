import csv
import tkinter as tk
from tkinter import messagebox

class EnterCivilId(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("320x220")
        self.title("Enter ID")
        self.configure(background='grey') # set the background color

        # create ID label and entry widget
        self.id_label = tk.Label(self, text="Civil ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(self)
        self.id_entry.pack()

        # create options label and radio buttons
        self.options_label = tk.Label(self, text="Select action:")
        self.options_label.pack(pady=5)
        self.action_var = tk.StringVar()
        self.green_channel_button = tk.Radiobutton(self, text="Allow through Green channel", variable=self.action_var, value="green_channel")
        self.green_channel_button.pack(pady=5)
        self.self_declared_button = tk.Radiobutton(self, text="Passenger self-declared Items", variable=self.action_var, value="self_declared")
        self.self_declared_button.pack(pady=5)
        self.inspect_items_button = tk.Radiobutton(self, text="Inspect items", variable=self.action_var, value="inspect_items")
        self.inspect_items_button.pack(pady=5)

        # create fines input field, initially hidden
        self.fines_label = tk.Label(self, text="Fines amount (0 to 20000):")
        self.fines_entry = tk.Entry(self)
        self.hide_fines_input()

        # create submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_action)
        self.submit_button.pack(side="left")

        # create go back button
        self.go_back_button = tk.Button(self, text="Go Back", command=self.go_back)
        self.go_back_button.pack(side="right")

        # trace the selected action variable to show or hide the fines entry
        self.action_var.trace("w", self.show_hide_fines)

    def show_fines_input(self):
        self.fines_label.pack()
        self.fines_entry.pack()

    def hide_fines_input(self):
        self.fines_label.pack_forget()
        self.fines_entry.pack_forget()
    
    def show_hide_fines(self, *args):
        if self.action_var.get() == "inspect_items":
            self.show_fines_input()
        else:
            self.hide_fines_input()

    def submit_action(self):
        civil_id = self.id_entry.get()
        action = self.action_var.get()
        fines = 0

        # Update fines based on the selected action
        if action == "inspect_items":
            try:
                fines = int(self.fines_entry.get())
            except ValueError:
                messagebox.showerror("Invalid Fines", "Fines amount must be a valid integer between 0 and 20000.")
                return

            if fines < 0 or fines > 20000:
                messagebox.showerror("Invalid Fines", "Fines amount must be between 0 and 20000.")
                return

        # Update passenger file with the new fines amount
        with open("database/passengers.txt", "r") as f:
            reader = csv.reader(f)
            rows = []
            added = False
            for row in reader:
                if row[0] == civil_id:
                    if row[4]:
                        row[4] = str(int(row[4]) + fines)
                    else:
                        row[4] = str(fines)
                    messagebox.showinfo("Fines Updated", f"Fines of {fines} KD have been added to passenger with ID {civil_id}")
                    added = True
                rows.append(row)
            if added == False:
                messagebox.showinfo("Civil ID not found", f"passenger with ID {civil_id} doesn't exist.")

        with open("database/passengers.txt", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        # clear the form
        self.id_entry.delete(0, tk.END)
        self.action_var.set(None)


    def go_back(self):
        self.destroy()
