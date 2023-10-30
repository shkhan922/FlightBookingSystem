import tkinter as tk
from login_window import LoginWindow

if __name__ == "__main__":
    root = tk.Tk()
    login_app = LoginWindow(root)
    login_app.pack()  # Display the LoginWindow
    root.mainloop()
