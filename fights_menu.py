import tkinter as tk
from tkinter import PhotoImage, font

def show_flights_menu():
    flights = tk.Toplevel()
    flights.title("Explore Flights")
    flights.geometry('800x600')
    flights.configure(bg='#E0E0E0')

    # Load the top image
    header_image = PhotoImage(file="flight.png")  # Adjust the file name as needed
    header_label = tk.Label(flights, image=header_image)
    header_label.pack(pady=20)

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=14, weight="bold")
    
    welcome_label = tk.Label(flights, text="Hi Davey, welcome to the Flights section", bg="#E0E0E0", font=custom_font)
    welcome_label.pack(pady=20)

    # Buttons for Flights Menu
    btn_frame = tk.Frame(flights, bg='#E0E0E0')
    btn_frame.pack(pady=20)  # Adjust as needed

    view_all_btn = tk.Button(btn_frame, text="View All Flights", width=15, height=2, bg="#ADD8E6", borderwidth=2)
    view_all_btn.grid(row=0, column=0, padx=10)

    view_by_country_btn = tk.Button(btn_frame, text="View Flights by Country", width=20, height=2, bg="#ADD8E6", borderwidth=2)
    view_by_country_btn.grid(row=0, column=1, padx=10)

    add_flight_btn = tk.Button(btn_frame, text="Add Flight", width=15, height=2, bg="#ADD8E6", borderwidth=2)
    add_flight_btn.grid(row=0, column=2, padx=10)

    remove_flight_btn = tk.Button(btn_frame, text="Remove Flight", width=15, height=2, bg="#ADD8E6", borderwidth=2)
    remove_flight_btn.grid(row=0, column=3, padx=10)

    close_btn = tk.Button(flights, text="Close", command=flights.destroy, width=15, height=2, bg="#ADD8E6", borderwidth=2)
    close_btn.pack(pady=20)