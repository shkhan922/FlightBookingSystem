import tkinter as tk

from tkinter import PhotoImage, font, Listbox, END, messagebox, ttk
from PIL import ImageTk, Image
import csv
from trip.add_trip_destination import add_trip_destination
from trip.remove_destination_trip import remove_destination_trip
# from destinations.view_destinations import view_destinations
from trip.add_connecting_flight import find_and_save_connecting_flights  # Import the add_connecting_flights function
from functools import partial
from error_window import show_error_window
from trip.add_connecting_flight import read_destinations

def load_destinations(trip_list):
    with open('trip/destinations.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        destinations = [row for row in reader]

    trip_list.delete(0, END)
    for destination in destinations:
        trip_list.insert(END, destination)

def load_connecting_flights(trip_list):
    try:
        with open('trip/connecting_flights.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            connecting_flights = [row for row in reader]
            

        for flight in connecting_flights:
            trip_list.insert(END, flight)
    except FileNotFoundError:
        # Handle the case where the connecting flights file doesn't exist
        pass
def get_connecting_flights():
    # Implement code to read and return a list of connecting flights from your data source (e.g., connecting_flights.csv)
    connecting_flights = []
    try:
        with open('trip/connecting_flights.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            connecting_flights = [row for row in reader]
    except FileNotFoundError:
        pass
    return connecting_flights

def view_trip():
    trip_window = tk.Toplevel()
    trip_window.title("Display Trip")

    image = Image.open("trip/trip_icon.png")
    icon = ImageTk.PhotoImage(image)
    trip_window.iconphoto(False, icon)

    trip_window.geometry('1200x900')
    trip_window.configure(bg='white')

    top_image = Image.open('trip/trip.png')
    top_image = top_image.resize((1200, 200), Image.ANTIALIAS)
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(trip_window, image=top_image, bg='white')
    header_label.image = top_image
    header_label.pack()

    canvas = tk.Canvas(trip_window, width=1640, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

    custom_font = font.Font(family="Helvetica", size=18, weight="bold")

    welcome_label = tk.Label(trip_window, text="Your Trip", bg="white", font=custom_font, fg="#00B2EE")
    welcome_label.pack(pady=20)

    canvas = tk.Canvas(trip_window, width=1640, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

    trip_list = Listbox(trip_window, width=80, height=15, bg="white", selectbackground="#00B2EE", selectmode=tk.MULTIPLE)

    load_destinations(trip_list)
    load_connecting_flights(trip_list)

    trip_list.pack(pady=20)

    def view_individual_destinations():
        # selected_indices = trip_list.curselection()

        # for index in selected_indices:
        #     selected_indices = trip_list.curselection()
        #     selected_item = trip_list.get(selected_indices[0]) if selected_indices else None

        #     destinations = read_destinations()
        #     connecting_flights = get_connecting_flights()
        #     print(selected_item)
        #     print(destinations)
        #     print(connecting_flights)

        # if selected_item in destinations:
        #     # Open the destination details window
        #     open_destination_window(selected_item)
        # elif selected_item in connecting_flights:
        #     # Open the connecting flight details window
        #     open_connecting_flight_window(selected_item)
        # else:
        #     # Show an error message for an incorrect selection
        #     show_error_window("Invalid Selection exception", "Invalid selection. Please select a destination or connecting flight.")
    #     selected_indices = trip_list.curselection()
    
    #     if not selected_indices:
    #     # Show an error message if nothing is selected
    #         show_error_window("Invalid Selection exception", "No item selected. Please select a destination or connecting flight.")
    #         return

    #     selected_item = trip_list.get(selected_indices[0])
    
    # # Split the selected item to determine its type
    #     parts = selected_item.split(', ')
    
    #     if len(parts) == 5:
    #     # This is a connecting flight
    #         open_connecting_flight_window(parts)
    #     else:
    #     # This is a destination
    #         open_destination_window(parts)
        selected_indices = trip_list.curselection()

        if not selected_indices:
        # Show an error message if nothing is selected
                show_error_window("Invalid Selection Exception", "No item selected. Please select a destination or connecting flight.")
                return

        if len(selected_indices) > 2:
        # Show an error message if multiple items are selected
            show_error_window("Invalid Selection Exception", "Multiple items selected. Please select a single destination or connecting flight.")
            return

        selected_indices = trip_list.curselection()

        if not selected_indices:
        # Show an error message if nothing is selected
            show_error_window("Invalid Selection exception", "No item selected. Please select a destination or connecting flight.")
            return

        selected_item = trip_list.get(selected_indices[0])

        if isinstance(selected_item, tuple) and len(selected_item) == 5:
        # This is a flight
            open_connecting_flight_window(selected_item)
        elif isinstance(selected_item, tuple) and len(selected_item) == 2:
        # This is a destination
         open_destination_window(selected_item)
        else:
        # Show an error message for an incorrect selection
         show_error_window("Invalid Selection exception", "Invalid selection. Please select a destination or connecting flight.")

    
    def open_destination_window(destination):
    # Create a new window for destination details
        destination_window = tk.Toplevel()
        destination_window.title("Destination Details")

    # Set the icon photo for the Toplevel window
        image = Image.open("destinations/destinations_icon.png")
        icon = ImageTk.PhotoImage(image)
        destination_window.iconphoto(False, icon)

        destination_window.geometry('1400x800')
        destination_window.configure(bg='white')

    # Load the top image
        top_image = Image.open('destinations/destination.png')
        top_image = top_image.resize((1400, 300), Image.ANTIALIAS)
        top_image = ImageTk.PhotoImage(top_image)

        header_label = tk.Label(destination_window, image=top_image, bg='white')
        header_label.image = top_image
        header_label.pack()

    # Section Line
        canvas = tk.Canvas(destination_window, width=1400, height=2, bg='#00B2EE', highlightthickness=0)
        canvas.pack()

    # Custom font for welcome message
        custom_font = font.Font(family="Helvetica", size=18, weight="bold")

        welcome_label = tk.Label(destination_window, text="Destination", font=custom_font, bg="white", fg="#00B2EE")
        welcome_label.pack(pady=20)

    # Create a Treeview widget for displaying the destination details
        tree = ttk.Treeview(destination_window, columns=("Name", "Country"))

    # Define column names
        tree.heading("#1", text="Name")
        tree.heading("#2", text="Country")
    
    # Set column text color to light blue
        style = ttk.Style()
        style.configure("Treeview.Heading", foreground="#00B2EE")

    # Insert the destination data into the table
        tree.insert("", "end", values=destination)

    # Pack the Treeview
        tree.pack(expand=True, fill="both")

    # Section Line
        canvas = tk.Canvas(destination_window, width=1400, height=2, bg='#00B2EE', highlightthickness=0)
        canvas.pack()

        close_btn = tk.Button(destination_window, text="Close", command=destination_window.destroy, width=100, foreground="white", border=0, background="#00B2EE")
        close_btn.pack(pady=20)

    
    def open_connecting_flight_window(connecting_flight):
        connecting_flight_window = tk.Toplevel()
        connecting_flight_window.title("Connecting Flight Details")

    # Set the icon photo for the Toplevel window
        image = Image.open("flights/flights_icon.png")
        icon = ImageTk.PhotoImage(image)
        connecting_flight_window.iconphoto(False, icon)

        connecting_flight_window.geometry('1200x800')
        connecting_flight_window.configure(bg='white')

    # Load the top image
        top_image = Image.open('flights/flight.png')
        top_image = top_image.resize((1400, 300), Image.ANTIALIAS)
        top_image = ImageTk.PhotoImage(top_image)

        header_label = tk.Label(connecting_flight_window, image=top_image, bg='white')
        header_label.image = top_image
        header_label.grid(row=0, column=0, columnspan=2)

    # Section Line
        canvas = tk.Canvas(connecting_flight_window, width=1400, height=2, highlightthickness=0)
        canvas.grid(row=1, column=0, columnspan=2)

    # Custom font for welcome message
        custom_font = font.Font(family="Helvetica", size=18, weight="bold")

        welcome_label = tk.Label(connecting_flight_window, text="Connecting Flights", font=custom_font, bg="white", fg="#00B2EE")
        welcome_label.grid(row=2, column=0, columnspan=2, pady=20)

    # Create a Treeview widget for displaying the table
        tree = ttk.Treeview(connecting_flight_window, columns=("Airline", "Flight Number", "Takeoff Country", "Landing Country", "Cost"))

    # Define column names
        tree.heading("#1", text="Airline", anchor="w")
        tree.heading("#2", text="Flight Number", anchor="w")
        tree.heading("#3", text="Takeoff Country", anchor="w")
        tree.heading("#4", text="Landing Country", anchor="w")
        tree.heading("#5", text="Cost", anchor="w")

    # Set column text color to light blue
        style = ttk.Style()
        style.configure("Treeview.Heading", foreground="#00B2EE")

    # Read data from a CSV file and insert it into the table
        tree.insert("", "end", values=connecting_flight)

    # Create a vertical scrollbar
        vsb = ttk.Scrollbar(connecting_flight_window, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)

    # Grid layout for the treeview and scrollbar
        tree.grid(row=3, column=0, columnspan=2, sticky="nsew")
        vsb.grid(row=3, column=2, sticky="ns")

    # Make the rows and columns expand with window resizing
        connecting_flight_window.grid_rowconfigure(3, weight=1)
        connecting_flight_window.grid_columnconfigure(0, weight=1)

    # Create a ttk Style to set the background color
        style = ttk.Style()
        style.configure("Background.TFrame", background="#00B2EE")

        btn_frame = ttk.Frame(connecting_flight_window, style="Background.TFrame")
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20)

        close_btn = tk.Button(btn_frame, text="Close", command=connecting_flight_window.destroy, width=100, foreground="white", border=0, background="#00B2EE", activebackground="#009ACD")
        close_btn.grid(row=0, column=4)

    button_frame = tk.Frame(trip_window, bg="#00B2EE")
    button_frame.pack(pady=5, fill="x")

    view_individual_btn = tk.Button(button_frame, text="View Individual", command=view_individual_destinations, width=50, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD")
    view_individual_btn.pack(side="left", padx=10)

    close_trip_btn = tk.Button(button_frame, text="Close", command=trip_window.destroy, width=50, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD")
    close_trip_btn.pack(side="right", padx=10)

def show_trip_menu(admin_name):
    flights = tk.Toplevel()
    flights.title("Book A Trip")

    image = Image.open("trip/trip_icon.png")
    icon = ImageTk.PhotoImage(image)
    flights.iconphoto(False, icon)

    flights.geometry('1640x600')
    flights.configure(bg='white')

    top_image = Image.open('trip/trip.png')
    top_image = top_image.resize((1640, 300), Image.ANTIALIAS)
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(flights, image=top_image, bg='white')
    header_label.image = top_image
    header_label.pack()

    canvas = tk.Canvas(flights, width=1640, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

    custom_font = font.Font(family="Helvetica", size=18, weight="bold")

    welcome_label = tk.Label(flights, text=f"Hi {admin_name}, welcome to the Trip section", bg="white", font=custom_font, fg="#00B2EE")
    welcome_label.pack(pady=20)

    canvas = tk.Canvas(flights, width=1640, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

    trip_list = Listbox(flights, width=60, height=15, bg="white", selectbackground="#00B2EE", selectmode=tk.MULTIPLE)
    load_destinations(trip_list)

    btn_frame = tk.Frame(flights, bg='#00B2EE')
    btn_frame.pack(pady=20, fill="x", side="bottom")

    add_destination_btn = tk.Button(btn_frame, text="Add Destination", width=30, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD", command=add_trip_destination)
    add_destination_btn.grid(row=0, column=0, padx=10)

    remove_destination_btn = tk.Button(btn_frame, text="Remove Destination", width=35, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD", command=remove_destination_trip)
    remove_destination_btn.grid(row=0, column=1, padx=10)

    add_connecting_btn = tk.Button(btn_frame, text="Add Connecting Flights", width=35, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD", command=find_and_save_connecting_flights)
    add_connecting_btn.grid(row=0, column=2, padx=10)

    view_trip_btn = tk.Button(btn_frame, text="View Trip", width=30, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD", command=view_trip)
    view_trip_btn.grid(row=0, column=3, padx=10)

    close_btn = tk.Button(btn_frame, text="Close", command=flights.destroy, width=30, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD")
    close_btn.grid(row=0, column=4, padx=10)

if __name__ == "__main__":
    show_trip_menu("Admin Name")
