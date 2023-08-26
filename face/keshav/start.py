import tkinter as tk
from tkinter import font
from tkinter import messagebox as mb

# Create the main application window
login_app = tk.Tk()
login_app.title('Login')
login_app.geometry('300x200')  # Set the initial size of the window
login_app.config(background='white')
font_ = font.Font(size=20)

# Create a label and entry for user ID
user_label = tk.Label(login_app, text='User ID:')
user_label.pack()
uname = tk.StringVar()
user_entry = tk.Entry(login_app, textvariable=uname)
user_entry.pack()

# Create a label and entry for password
pass_label = tk.Label(login_app, text='Password:')
pass_label.pack()
pwd = tk.StringVar()
pass_entry = tk.Entry(login_app, textvariable=pwd, show='*')  # Show * instead of the actual password
pass_entry.pack()

# Function to handle the login button click
def login():
    userid = uname.get()
    password = pwd.get()
    p = open('opr.txt').read()  # Assuming 'pwd.txt' contains the password
    if userid == 'admin' and password == p:
        print('Login successful')
        mb.showinfo('Success', 'Login successful')
    else:
        print('Login failed')
        mb.showerror('Error', 'Login failed')
    try:
        with open('opr.txt', 'r') as file:
            p = file.read()
            if userid == 'admin' and password == p:
                print('Login successful')
                mb.showinfo('Success', 'Login successful')
            else:
                print('Login failed')
                mb.showerror('Error', 'Login failed')
    except FileNotFoundError:
        print("Password file not found")
        mb.showerror('Error', 'Password file not found')

# Create and configure a custom font for the button
custom_font = font.Font(family='Helvetica', size=12)
# Create the login button
submit_button = tk.Button(login_app, text='Submit', font=custom_font, command=login)
submit_button.pack()

# Start the Tkinter main loop
login_app.mainloop()
