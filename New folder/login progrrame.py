username = ("rajat 123")
password = ("5656")

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

if username_input == username and password_input == password:
    print("Login successful!")

else:
    print("Invalid username or password. Please try again.")
