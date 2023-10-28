import tkinter as tk
from tkinter import ttk

class AdminWindow(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Prog2 Travel Agency")
        self.master.geometry("800x600")
        self.pack()

        # Style configuration
        style = ttk.Style()
        style.configure("TButton", foreground="black", background="lightblue")

        # Load and display an image on the admin screen
        image = tk.PhotoImage(file="agency.png")  # Replace "agency.png" with the path to your image
        canvas = tk.Canvas(self, width=image.width(), height=image.height())
        canvas.create_image(0, 0, anchor=tk.NW, image=image)
        canvas.image = image  # Store a reference to the image
        canvas.pack()

        # Welcome Label
        welcome_label = ttk.Label(self, text="Welcome, Admin!", font=("Arial", 16))
        welcome_label.pack()

        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(side=tk.BOTTOM)

        explore_flights_button = ttk.Button(button_frame, text="Explore Flights", style="TButton")
        explore_flights_button.pack(side=tk.LEFT, padx=10, pady=10)

        explore_destinations_button = ttk.Button(button_frame, text="Explore Destinations", style="TButton")
        explore_destinations_button.pack(side=tk.LEFT, padx=10, pady=10)

        book_trip_button = ttk.Button(button_frame, text="Book a Trip", style="TButton")
        book_trip_button.pack(side=tk.LEFT, padx=10, pady=10)

        exit_button = ttk.Button(button_frame, text="Exit", style="TButton", command=self.master.destroy)
        exit_button.pack(side=tk.LEFT, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminWindow(root)
    root.mainloop()
