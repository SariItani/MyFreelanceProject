import csv
from tkinter import messagebox
import bcrypt
import tkinter as tk
import immigration_officer_screen
import customs_officer_screen

class LoginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Login Screen")
        self.pack()

        # create username label and entry widget
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        # create password label and entry widget
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="\u25CF")
        self.password_entry.pack()

        # create login button
        self.login_button = tk.Button(self, text="Login", command=self.pick_screen)
        self.login_button.pack()

    def login(self, username, password):
        with open("login.txt", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 3:
                    continue
                if row[1] == username:
                    if bcrypt.checkpw(password.encode(), row[2].encode()):
                        messagebox.showinfo("Login", "Login successful")
                        return row[3]
                    else:
                        break
            else:
                messagebox.showerror("Login Error", "Incorrect username or password")


    def pick_screen(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.login(username, password)
        screen = None  # Set screen to None initially
        if role is not None:
            print("Picking screen...")
            if role == "Immigration Officer":
                screen = immigration_officer_screen.ImmigrationOfficerScreen(self.master)
            elif role == "Customs Officer":
                screen = customs_officer_screen.CustomsOfficerScreen(self.master)
        if screen is not None:  # Check if screen was assigned
            screen.mainloop()
        else:
            print("Role Not Found.")


# create an instance of the LoginScreen class
root = tk.Tk()
screen = LoginScreen(root)
screen.mainloop()
