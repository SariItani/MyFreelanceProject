import csv
import tkinter as tk
from tkinter import messagebox

class EnterCivilId(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.geometry("250x200")
        self.master.title("Enter ID")
        self.configure(background='grey') # set the background color
        self.pack(fill='both', expand=True)

        # create ID label and entry widget
        self.id_label = tk.Label(self, text="Civil ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(self)
        self.id_entry.pack()

        # create options label and radio buttons
        self.options_label = tk.Label(self, text="Select action:")
        self.options_label.pack()
        self.action_var = tk.StringVar()
        self.green_channel_button = tk.Radiobutton(self, text="Allow through Green channel", variable=self.action_var, value="green_channel")
        self.green_channel_button.pack()
        self.self_declared_button = tk.Radiobutton(self, text="Passenger self-declared Items", variable=self.action_var, value="self_declared")
        self.self_declared_button.pack()
        self.inspect_items_button = tk.Radiobutton(self, text="Inspect items", variable=self.action_var, value="inspect_items")
        self.inspect_items_button.pack()

        # create submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_action)
        self.submit_button.pack()

        # create go back button
        self.go_back_button = tk.Button(self, text="Go Back", command=self.go_back)
        self.go_back_button.pack()

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

        # clear the form
        self.id_entry.delete(0, tk.END)
        self.action_var.set(None)

    def go_back(self):
        self.master.destroy()
