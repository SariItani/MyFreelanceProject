import bcrypt
import immigration_officer_screen
import customs_officer_screen

def authenticate(username: str, password: str) -> str:
    with open('login.txt', 'r') as f:
        data = f.readlines()

    for line in data:
        fields = line.strip().split(',')
        if fields[1] == username:
            hashed_password = fields[2].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return fields[3] # return the role
            else:
                return None # password is incorrect

    return None # username not found

username = input("Enter username: ") # now CLI, later to be GUI
password = input("Enter password: ") # now CLU, later to be GUI

role = authenticate(username, password)
if role is not None:
    print("Authentication successful!")
    if role == "Immigration officer":
        # call Immigration Officer screen
        pass
    elif role == "Customs officer":
        # call Customs Officer screen
        pass
else:
    print("Incorrect username or password.")
