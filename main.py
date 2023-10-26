import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # To work with images

def book_flight():
    selected_flight = flight_combobox.get()
    passenger_name = name_entry.get()
    print(f"Booking {selected_flight} for {passenger_name}")

# Create the main window
root = tk.Tk()
root.title("Flight Booking System")

# Set the canvas size
canvas = tk.Canvas(root, width=1000, height=800)
canvas.pack()

# Load and display an image
image = Image.open("agency.png")  # Replace "airplane.jpg" with the path to your image
photo = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Flight options
flights = ["Flight 1", "Flight 2", "Flight 3"]
flight_label = ttk.Label(root, text="Select Flight:")
flight_label.pack()
flight_combobox = ttk.Combobox(root, values=flights)
flight_combobox.pack()

# Passenger details
name_label = ttk.Label(root, text="Passenger Name:")
name_label.pack()
name_entry = ttk.Entry(root)
name_entry.pack()

# Book button
book_button = ttk.Button(root, text="Book Flight", command=book_flight)
book_button.pack()

root.mainloop()
