# In the login.txt file, you will store ID, Username, Password, Role (Immigration officer or Customs officer)
# In passenger.txt, you will store Civil ID, Name, Date of Birth, Gender, Customs Fine, and Status (dict: Civil ID as Key and other information as list values)
import tkinter as tk
from screens.login_screen import LoginScreen

if __name__ == '__main__':
    root = tk.Tk()
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='static/logo.png'))
    root.title("Welcome Officer")
    LoginScreen(root)
    root.mainloop()
