import tkinter as tk

class AdminWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Prog2 Travel Agency")
        self.master.geometry("600x400")
        self.pack()  # Add this line to pack the AdminWindow

        # Image Display
        self.image_label = tk.Label(self, text="Your image goes here")
        self.image_label.pack()

        # Explore Flights Button
        self.explore_flights_button = tk.Button(self, text="Explore Flights")
        self.explore_flights_button.pack()

        # Explore Destinations Button
        self.explore_destinations_button = tk.Button(self, text="Explore Destinations")
        self.explore_destinations_button.pack()

        # Book a Trip Button
        self.book_trip_button = tk.Button(self, text="Book a Trip")
        self.book_trip_button.pack()

        # Exit Button
        self.exit_button = tk.Button(self, text="Exit", command=self.master.destroy)
        self.exit_button.pack()
