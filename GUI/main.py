# In the login.txt file, you will store ID, Username, Password, Role (Immigration officer or Customs officer)
# In passenger.txt, you will store Civil ID, Name, Date of Birth, Gender, Customs Fine, and Status (dict: Civil ID as Key and other information as list values)
import tkinter as tk
import immigration_officer_screen as i
from login_screen import LoginScreen
import customs_officer_screen as c


root = tk.Tk()
app = LoginScreen(root)
root.mainloop()

# Once the user has logged in, you can get the user's role and create the appropriate screen
if app.role == "Immigration Officer":
    screen = i.ImmigrationOfficerScreen(root)
elif app.role == "Customs Officer":
    screen = c.CustomsOfficerScreen(root)
screen.mainloop()
