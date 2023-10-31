import tkinter as tk
from tkinter import PhotoImage, font
from PIL import ImageTk, Image
from tkinter import ttk
import csv

def add_flight():
    flights = tk.Toplevel()
    flights.title("Add Flight")

    # Set the icon photo for the Toplevel window
    image = Image.open("flights/flights_icon.png")
    icon = ImageTk.PhotoImage(image)
    flights.iconphoto(False, icon)

    flights.geometry('1400x800')
    flights.configure(bg='white')

    # Load the top image
    top_image = Image.open('flights/flight.png')
    top_image = top_image.resize((1400, 300), Image.ANTIALIAS)
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(flights, image=top_image, bg='white')
    header_label.image = top_image
    header_label.pack()

    # Section Line
    canvas = tk.Canvas(flights, width=1400, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")

    welcome_label = tk.Label(flights, text="Add a Flight", font=custom_font, bg="white", fg="#00B2EE")
    welcome_label.pack(pady=20)

    # Create labels and entry widgets for flight information
    airline_label = ttk.Label(flights, text="Airline")
    airline_label.pack()
    airline_entry = ttk.Entry(flights)
    airline_entry.pack()

    flight_number_label = ttk.Label(flights, text="Flight Number")
    flight_number_label.pack()
    flight_number_entry = ttk.Entry(flights)
    flight_number_entry.pack()

    takeoff_country_label = ttk.Label(flights, text="Takeoff Country")
    takeoff_country_label.pack()
    takeoff_country_entry = ttk.Entry(flights)
    takeoff_country_entry.pack()

    landing_country_label = ttk.Label(flights, text="Landing Country")
    landing_country_label.pack()
    landing_country_entry = ttk.Entry(flights)
    landing_country_entry.pack()

    cost_label = ttk.Label(flights, text="Cost")
    cost_label.pack()
    cost_entry = ttk.Entry(flights)
    cost_entry.pack()

    def add_to_csv():
        # Get the data from entry widgets
        airline = airline_entry.get()
        flight_number = flight_number_entry.get()
        takeoff_country = takeoff_country_entry.get()
        landing_country = landing_country_entry.get()
        cost = cost_entry.get()

        # Append the data to the CSV file
        with open("flights/flights.csv", "a", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([airline, flight_number, takeoff_country, landing_country, cost])

        # Clear the entry widgets after adding
        airline_entry.delete(0, tk.END)
        flight_number_entry.delete(0, tk.END)
        takeoff_country_entry.delete(0, tk.END)
        landing_country_entry.delete(0, tk.END)
        cost_entry.delete(0, tk.END)

    add_button = tk.Button(flights, text="Add", command=add_to_csv, activebackground="#009ACD",foreground="white", border=0, background="#00B2EE")
    add_button.pack(pady=10)

    # Section Line
    canvas = tk.Canvas(flights, width=1400, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

    close_btn = tk.Button(flights, text="Close", command=flights.destroy, foreground="white", border=0, background="#00B2EE", activebackground="#009ACD")
    close_btn.pack()

# Call the add_flight function to display the window
if __name__ == "__main__":
    add_flight()
