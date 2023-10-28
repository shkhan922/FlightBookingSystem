import tkinter as tk
from tkinter import ttk
from admin_window import AdminWindow

class LoginWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Login")
        self.master.geometry("400x200")
        self.pack()

        self.style = ttk.Style()
        self.style.configure("TButton", foreground="black", background="lightblue")
        self.style.configure("TLabel", foreground="black")
        self.style.configure("TEntry", foreground="black")

        # Create a frame for labels and text entry
        login_frame = ttk.Frame(self)
        login_frame.grid(row=0, column=0, padx=10, pady=10)

        # Username Label and Entry
        username_label = ttk.Label(login_frame, text="Username:", style="TLabel")
        username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.username_entry = ttk.Entry(login_frame, style="TEntry")
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Password Label and Entry
        password_label = ttk.Label(login_frame, text="Password:", style="TLabel")
        password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.password_entry = ttk.Entry(login_frame, show="*", style="TEntry")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Login Button
        login_button = ttk.Button(login_frame, text="Login", style="TButton", command=self.on_successful_login)
        login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")

         # Login Button
        login_button = ttk.Button(login_frame, text="Exit", style="TButton", command=self.master.destroy)
        login_button.grid(row=2, column=2, columnspan=2, padx=10, pady=10, sticky="we")

    def on_successful_login(self):
        username = self.username_entry.get()
        if username == "admin":
            admin_app = AdminWindow(self.master)
            self.pack_forget()  # Hide the LoginWindow
            admin_app.pack()  # Display the AdminWindow

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
