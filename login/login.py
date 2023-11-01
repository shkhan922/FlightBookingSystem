import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk
import csv
import os  # Import the os module to exit the program

from agency.agency_menu import show_agency_menu
from error_window import show_error_window

def login_attempt(username, password, root, login_button):
    # Read login credentials from a CSV file
    with open('login/login_credentials.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row[0] == username and row[1] == password:
                root.destroy()
                show_agency_menu(row[2])  # Pass admin name as a parameter
                return
    # messagebox.showerror("Error", "Login Failed!")
    show_error_window("Login Failed!")

def enable_login_button(event, username_entry, password_entry, login_button):
    if username_entry.get() and password_entry.get():
        login_button['state'] = 'normal'
    else:
        login_button['state'] = 'disabled'

def login_window():
    root = tk.Tk()
    # Convert PNG to ICO
    image = Image.open("login/login_icon.png")
    icon = ImageTk.PhotoImage(image)
    
    root.title("Login")
    root.call('wm', 'iconphoto', root._w, icon)
    root.geometry('450x200')
    root.config(bg="#E0E0E0")  # Light gray background color

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")

    title_label = tk.Label(root, text="Login", bg="#E0E0E0", font=custom_font, fg="#00B2EE")
    title_label.pack(pady=20)

    # Section Line
    canvas = tk.Canvas(root, width=1640, height=2, highlightthickness=0)
    canvas.pack()

    form_frame = tk.Frame(root, bg="#E0E0E0")
    form_frame.pack()

    # Username Label and Entry
    username_label = tk.Label(form_frame, text="Username:", bg="#E0E0E0", fg="#00B2EE")
    username_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    username_entry = tk.Entry(form_frame)
    username_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

    # Password Label and Entry
    password_label = tk.Label(form_frame, text="Password:", bg="#E0E0E0", fg="#00B2EE")
    password_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    password_entry = tk.Entry(form_frame, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

    button_frame = tk.Frame(root, bg="#00B2EE")
    button_frame.pack(pady=20,fill="x",side="bottom")

    login_button = tk.Button(button_frame, text="Login", bg="#00B2EE", activebackground="#009ACD",fg="white", borderwidth=0, width=25, state="disabled", command=lambda: login_attempt(username_entry.get(), password_entry.get(), root, login_button))
    login_button.grid(row=0, column=0, padx=10, sticky='we')
    exit_button = tk.Button(button_frame, text="Exit", bg="#00B2EE", activebackground="#009ACD", fg="white",borderwidth=0, width=25,command=lambda: exit_program(root))
    exit_button.grid(row=0, column=1, padx=10, sticky='we')

    login_button.bind("<Enter>", lambda e: login_button.config(bg="#00B2EE"))
    login_button.bind("<Leave>", lambda e: login_button.config(bg="#00B2EE"))

    enable_login_button(None, username_entry, password_entry, login_button)
    username_entry.bind("<KeyRelease>", lambda e: enable_login_button(e, username_entry, password_entry, login_button))
    password_entry.bind("<KeyRelease>", lambda e: enable_login_button(e, username_entry, password_entry, login_button))

    root.mainloop()

def exit_program(root):
    root.destroy()
    os._exit(0)  # Use os._exit to exit the program completely

login_window()
