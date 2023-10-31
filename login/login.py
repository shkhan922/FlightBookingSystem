import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk

from agency.agency_menu import show_agency_menu

def login_attempt(username, password, root):
    if username == "admin" and password == "password":
        root.destroy()
        show_agency_menu()
    else:
        messagebox.showerror("Error", "Login Failed!")

def login_window():
    root = tk.Tk()
    # Convert PNG to ICO
    image = Image.open("login/login_icon.png")
    icon = ImageTk.PhotoImage(image)
    
    root.title("Login")
    root.call('wm', 'iconphoto', root._w, icon)
    root.geometry('600x400')
    root.config(bg="#E0E0E0")  # Light gray background color

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")

    title_label = tk.Label(root, text="Login", bg="#E0E0E0", font=custom_font, fg="#ADD8E6")
    title_label.pack(pady=20)

    username_label = tk.Label(root, text="Username:", bg="#E0E0E0")
    username_label.pack(pady=5, anchor='w', padx=20)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5, padx=20, fill=tk.X)

    password_label = tk.Label(root, text="Password:", bg="#E0E0E0")
    password_label.pack(pady=5, anchor='w', padx=20)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5, padx=20, fill=tk.X)

    login_button = tk.Button(root, text="Login", bg="#ADD8E6", fg="white",borderwidth=0, command=lambda: login_attempt(username_entry.get(), password_entry.get(), root))
    login_button.pack(pady=20)
    exit_button = tk.Button(root, text="Exit", bg="#ADD8E6", fg="white", borderwidth=0, command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()