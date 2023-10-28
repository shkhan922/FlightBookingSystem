import tkinter as tk
from admin_window import AdminWindow

class LoginWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Login")
        self.master.geometry("400x200")
        self.pack()  # Add this line to pack the LoginWindow

        # Username Entry
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        # Password Entry
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # Login Button
        self.login_button = tk.Button(self, text="Login", command=self.on_successful_login)
        self.login_button.pack()

    def on_successful_login(self):
        username = self.username_entry.get()
        # Check username and password here
        if username == "admin":
            admin_app = AdminWindow(self.master)
            self.pack_forget()  # Hide the LoginWindow
            admin_app.pack()  # Display the AdminWindow
