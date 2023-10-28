import tkinter as tk
from tkinter import ttk

class ErrorWindow(tk.Frame):
    def __init__(self, parent, on_close):
        super().__init__(parent)
        self.parent = parent
        self.on_close = on_close
        self.create_error_ui()

    def create_error_ui(self):
        error_label = ttk.Label(self, text="Error: Invalid username or password.")
        error_label.pack(padx=10, pady=10)

        ok_button = ttk.Button(self, text="OK", command=self.close_window)
        ok_button.pack(padx=10, pady=10)

    def close_window(self):
        self.on_close()
