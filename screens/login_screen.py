import csv
from tkinter import messagebox
import bcrypt
import tkinter as tk
from screens import customs_officer_screen
from screens import immigration_officer_screen

class LoginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.geometry("220x150")
        self.master.title("Login Screen")
        self.configure(background='grey') # set the background color
        self.pack(fill='both', expand=True)

        # # create a logo image
        # self.logo = tk.PhotoImage(file="GUI/logo.png")
        # self.logo_label = tk.Label(self, image=self.logo)
        # self.logo_label.pack(pady=20)
        # self.master.iconphoto(False, self.logo)

        # # create a background texture image
        # bg_image = tk.PhotoImage(file='GUI/background_texture.jpg')
        # bg_label = tk.Label(self, image=bg_image)
        # bg_label.image = bg_image # keep a reference to prevent the image from being garbage collected
        # bg_label.place(relx=0.5, rely=0.5, anchor='center')

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

        self.protocol("WM_DELETE_WINDOW", self.quit_app)


    def login(self, username, password):
        with open("database/login.txt", "r") as f:
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
                print("Picked Immigration Officer screen.")
                screen = immigration_officer_screen.ImmigrationOfficerScreen(self.master)
            elif role == "Customs Officer":
                print("Picked Customs Officer screen.")
                screen = customs_officer_screen.CustomsOfficerScreen(self.master)
        if screen is not None:  # Check if screen was assigned
            self.destroy()  # Remove all widgets from the screen
            screen.mainloop()
        else:
            print("Role Not Found.")
        
    def quit_app(self):
        if tk.messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.destroy()
