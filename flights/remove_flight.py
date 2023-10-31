import tkinter as tk
from tkinter import PhotoImage, font
from PIL import ImageTk, Image
from tkinter import ttk
import csv

def remove_flight():
    flights = tk.Toplevel()
    flights.title("Remove Flight")

    # Set the icon photo for the Toplevel window
    image = Image.open("flights/flights_icon.png")
    icon = ImageTk.PhotoImage(image)
    flights.iconphoto(False, icon)

    flights.geometry('1400x800')
    flights.configure(bg='white')

    # Load the top image
    top_image = Image.open('flights/flight.png')
    top_image = top_image.resize((900, 300), Image.ANTIALIAS)
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(flights, image=top_image, bg='white')
    header_label.image = top_image
    header_label.pack()

    # Section Line
    canvas = tk.Canvas(flights, width=1400, height=2, bg='#ADD8E6', highlightthickness=0)
    canvas.pack()

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")

    welcome_label = tk.Label(flights, text="Remove a Flight", font=custom_font, bg="white", fg="#ADD8E6")
    welcome_label.pack(pady=20)

    # Create labels and entry widgets for takeoff and landing country names
    takeoff_country_label = ttk.Label(flights, text="Takeoff Country")
    takeoff_country_label.pack()
    takeoff_country_entry = ttk.Entry(flights)
    takeoff_country_entry.pack()

    landing_country_label = ttk.Label(flights, text="Landing Country")
    landing_country_label.pack()
    landing_country_entry = ttk.Entry(flights)
    landing_country_entry.pack()

    def remove_from_csv():
        # Get the takeoff and landing country names
        takeoff_country = takeoff_country_entry.get()
        landing_country = landing_country_entry.get()

        # Read the existing data from the CSV file
        with open("flights/flights.csv", "r") as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)

        # Check if the flight with the specified takeoff and landing countries exists in the CSV data
        for row in rows:
            if row[2] == takeoff_country and row[3] == landing_country:
                # Remove the row with the specified takeoff and landing countries
                rows.remove(row)

        # Write the updated data back to the CSV file
        with open("flights/flights.csv", "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(rows)

        # Clear the entry widgets after removing
        takeoff_country_entry.delete(0, tk.END)
        landing_country_entry.delete(0, tk.END)

    remove_button = tk.Button(flights, text="Remove", command=remove_from_csv, foreground="white", border=0, background="#ADD8E6")
    remove_button.pack(pady=10)

    # Section Line
    canvas = tk.Canvas(flights, width=1400, height=2, bg='#ADD8E6', highlightthickness=0)
    canvas.pack()

    close_btn = tk.Button(flights, text="Close", command=flights.destroy, foreground="white", border=0, background="#ADD8E6")
    close_btn.pack()

# Call the remove_flight function to display the window
if __name__ == "__main__":
    remove_flight()
