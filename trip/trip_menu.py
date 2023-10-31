import tkinter as tk
from tkinter import PhotoImage, font
from PIL import ImageTk, Image

def show_trip_menu():
    flights = tk.Toplevel()
    flights.title("Book A Trip")
    
    # Set the icon photo for the Toplevel window
    image = Image.open("trip/trip_icon.png")
    icon = ImageTk.PhotoImage(image)
    flights.iconphoto(False, icon)
    
    flights.geometry('1640x600')
    flights.configure(bg='white')

    # Load the top image
    myimg = ImageTk.PhotoImage(Image.open('trip/trip.png'))
    header_label = tk.Label(flights, image=myimg)
    header_label.pack(pady=10)

    # Section Line
    canvas = tk.Canvas(flights, width=1640, height=2, bg='#ADD8E6', highlightthickness=0)
    canvas.pack()

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")
    
    welcome_label = tk.Label(flights, text="Hi Davey, welcome to the Trip section", bg="white", font=custom_font, fg="#ADD8E6")
    welcome_label.pack(pady=20)

    # Section Line
    canvas = tk.Canvas(flights, width=1640, height=2, bg='#ADD8E6', highlightthickness=0)
    canvas.pack()

    # Buttons for Flights Menu
    btn_frame = tk.Frame(flights, bg='#ADD8E6')
    btn_frame.pack(pady=20)

    view_all_btn = tk.Button(btn_frame, text="Add Destination", width=15, height=2, fg="white", bg="#ADD8E6", borderwidth=0)
    view_all_btn.grid(row=0, column=0, padx=10)

    view_by_country_btn = tk.Button(btn_frame, text="Remove Destination", width=20, height=2, fg="white", bg="#ADD8E6", borderwidth=0)
    view_by_country_btn.grid(row=0, column=1, padx=10)

    add_flight_btn = tk.Button(btn_frame, text="Add Connecting Flights", width=15, height=2, fg="white", bg="#ADD8E6", borderwidth=0)
    add_flight_btn.grid(row=0, column=2, padx=10)

    remove_flight_btn = tk.Button(btn_frame, text="View Trip", width=15, height=2, fg="white", bg="#ADD8E6", borderwidth=0)
    remove_flight_btn.grid(row=0, column=3, padx=10)

    close_btn = tk.Button(btn_frame, text="Close", command=flights.destroy, width=15, height=2, fg="white", bg="#ADD8E6", borderwidth=0)
    close_btn.grid(row=0, column=4, padx=10)

# Call the show_flights_menu function to display the window
if __name__ == "__main__":
    show_trip_menu()
