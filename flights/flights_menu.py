import tkinter as tk
from tkinter import font, ttk
from PIL import ImageTk, Image

from flights.view_flights import view_flights
from flights.view_flights_filtered import view_flights_filtered
from flights.add_flight import add_flight
from flights.remove_flight import remove_flight

def show_flights_menu():
    flights = tk.Toplevel()
    flights.title("Explore Flights")
    
    # Set the icon photo for the Toplevel window
    image = Image.open("flights/flights_icon.png")
    icon = ImageTk.PhotoImage(image)
    flights.iconphoto(False, icon)
    
    flights.geometry('1640x600')
    flights.configure(bg='white')

    # Load the top image
    top_image = Image.open('flights/flight.png')
    top_image = top_image.resize((1640, 300), Image.ANTIALIAS)  # Resize the image to fit the label
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(flights, image=top_image, bg='white')
    header_label.image = top_image  # Keep a reference to the image to prevent it from being garbage collected
    header_label.pack()


    # Section Line
    canvas = tk.Canvas(flights, width=1640, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")
    
    welcome_label = tk.Label(flights, text="Hi Davey, welcome to the Flights section", bg="white", font=custom_font, fg="#00B2EE")
    welcome_label.pack(pady=20)

    # Section Line
    canvas = tk.Canvas(flights, width=1640, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

    # Buttons for Flights Menu
    btn_frame = tk.Frame(flights, bg='#00B2EE')
    btn_frame.pack(pady=20, fill="x",side="bottom")

    view_all_btn = tk.Button(btn_frame, text="View All Flights", width=35, height=2, fg="white", bg="#00B2EE", activebackground="#009ACD", borderwidth=0, command=view_flights)
    view_all_btn.grid(row=0, column=0, padx=10)

    view_by_country_btn = tk.Button(btn_frame, text="View Flights by Country", width=45, height=2, fg="white", bg="#00B2EE",activebackground="#009ACD", borderwidth=0, command=view_flights_filtered)
    view_by_country_btn.grid(row=0, column=1, padx=10)

    add_flight_btn = tk.Button(btn_frame, text="Add Flight", width=35, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD", command=add_flight)
    add_flight_btn.grid(row=0, column=2, padx=10)

    remove_flight_btn = tk.Button(btn_frame, text="Remove Flight", width=35, height=2, fg="white", bg="#00B2EE", activebackground="#009ACD", borderwidth=0, command=remove_flight)
    remove_flight_btn.grid(row=0, column=3, padx=10)

    close_btn = tk.Button(btn_frame, text="Close", command=flights.destroy, width=35, height=2, fg="white", bg="#00B2EE", activebackground="#009ACD", borderwidth=0)
    close_btn.grid(row=0, column=4, padx=10)

# Call the show_flights_menu function to display the window
if __name__ == "__main__":
    show_flights_menu()
