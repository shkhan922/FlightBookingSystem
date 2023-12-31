import tkinter as tk
from tkinter import PhotoImage, font
from PIL import Image, ImageTk
from flights.flights_menu import show_flights_menu
from destinations.destinations_menu import show_destinations_menu
from trip.trip_menu import show_trip_menu




def show_agency_menu(admin_name):
    agency = tk.Tk()
    agency.title("Prog2 Travel Agency")
    image = Image.open("agency/agency_icon.png")
    icon = ImageTk.PhotoImage(image)
    agency.geometry('1640x600')
    agency.configure(bg='white')
    agency.call('wm', 'iconphoto', agency._w, icon)
   

    # Load the top image
    header_image = PhotoImage(file="agency/agency.png")
    header_label = tk.Label(agency, image=header_image)
    header_label.pack(pady=20)

    # Section Line
    canvas = tk.Canvas(agency, width=1640, height=2, highlightthickness=0)
    canvas.pack()

    # Custom font for the welcome message
    custom_font = font.Font(family="Helvetica", size=14, weight="bold")
    
    welcome_label = tk.Label(agency, text=f"Hi {admin_name}, welcome to the Prog2 Travel Agency", bg="white", font=custom_font, fg="#00B2EE")
    welcome_label.pack(pady=20)

    # Section Line
    canvas = tk.Canvas(agency, width=1640, height=2, highlightthickness=0)
    canvas.pack()

    def open_flights_menu():
        show_flights_menu(admin_name)

    def open_destinations_menu():
        show_destinations_menu(admin_name)

    def open_trip_menu():
        show_trip_menu(admin_name)

    # Buttons for the Agency Menu
    btn_frame = tk.Frame(agency, bg='#00B2EE')
    btn_frame.pack(pady=20,fill="x",side="bottom")

    explore_flights_btn = tk.Button(btn_frame, text="Explore Flights", width=40, height=2, bg="#00B2EE", activebackground="#009ACD",fg="white", borderwidth=0, command=open_flights_menu)
    explore_flights_btn.grid(row=0, column=0, padx=10)

    explore_destinations_btn = tk.Button(btn_frame, text="Explore Destinations", width=40, height=2, bg="#00B2EE", activebackground="#009ACD", fg="white", borderwidth=0, command=open_destinations_menu)
    explore_destinations_btn.grid(row=0, column=1, padx=10)

    book_a_trip_btn = tk.Button(btn_frame, text="Book a Trip", width=40, height=2, bg="#00B2EE", activebackground="#009ACD", fg="white", borderwidth=0, command=open_trip_menu)
    book_a_trip_btn.grid(row=0, column=2, padx=10)

    exit_btn = tk.Button(btn_frame, text="Exit", command=agency.destroy, width=40, height=2, bg="#00B2EE", activebackground="#009ACD", fg="white", borderwidth=0)
    exit_btn.grid(row=0, column=3, padx=10)

    agency.mainloop()



if __name__ == "__main__":
   
    show_agency_menu()
