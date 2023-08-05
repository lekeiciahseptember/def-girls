import re

# User database (simulated)
user_database = {}

# Function to validate a strong password
def is_strong_password(password):
    if len(password) < 8:
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[!@#$%^&*()_+{}:;<>,.?~]", password):
        return False

    return True

# Function to register a new user
def register():
    username = input("Enter a username: ")

    if username in user_database:
        print("Username already taken.")
        return

    password = input("Enter a password: ")
    if not is_strong_password(password):
        print("Password is not strong enough.")
        return

    user_database[username] = password
    print("Registration successful!")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_database and user_database[username] == password:
        print("Login successful!")
    else:
        print("Login failed. Please check your username and password.")


while True:
    print("\n1. Register\n2. Login\n3. Quit")
    choice = input("Select an option: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please select a valid option.")

            

