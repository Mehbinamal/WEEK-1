
#Predefined Demo Data
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

#Login Function
def login (username,password):
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        print("Login successful! Welcome, " + username + ".")
    else:
        print("Error: Incorrect username or password. Please try again.")

#Taking Input & calling Function
try:
    username = input("Username: ")
    password = input("Password: ")
    login(username,password)
except Exception as e:
    print (f"An Error Occured : {e}")
