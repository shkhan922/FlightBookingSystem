import tkinter as tk
from tkinter import PhotoImage, font
from PIL import ImageTk, Image
from destinations.add_destination import add_destination
from destinations.remove_destination import remove_destination

def add_destination():
    # You can redirect to the Add Destination window or function from here
    pass

def view_trip():
    trip_window = tk.Toplevel()
    trip_window.title("Display Trip")

    # Create a list to display destination information
    trip_list = tk.Listbox(trip_window, width=60, height=15, bg="white", selectbackground="#00B2EE")

    # Assuming you have a list of destinations, you can populate the list with them
    # For example, I'm adding some sample destinations
    destinations = ["Paris, France", "New York, USA", "Tokyo, Japan"]

    for destination in destinations:
        trip_list.insert(tk.END, destination)

    trip_list.pack(pady=20)

    # Buttons to view individual destination and close the trip window
    view_individual_btn = tk.Button(trip_window, text="View Individual", command=view_individual_destination, width=30, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD")
    view_individual_btn.pack(pady=10)

    close_trip_btn = tk.Button(trip_window, text="Close", command=trip_window.destroy, width=30, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD")
    close_trip_btn.pack()

def view_individual_destination():
    # You can implement the code to view individual destination details here
    pass

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
    top_image = Image.open('trip/trip.png')
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
    
    welcome_label = tk.Label(flights, text="Hi {admin_name}, welcome to the Trip section", bg="white", font=custom_font, fg="#00B2EE")
    welcome_label.pack(pady=20)

    # Section Line
    canvas = tk.Canvas(flights, width=1640, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

    # Buttons for Trip Menu
    btn_frame = tk.Frame(flights, bg='#00B2EE')
    btn_frame.pack(pady=20, fill="x", side="bottom")

    add_destination_btn = tk.Button(btn_frame, text="Add Destination", width=30, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD", command=add_destination)
    add_destination_btn.grid(row=0, column=0, padx=10)

    remove_destination_btn = tk.Button(btn_frame, text="Remove Destination", width=35, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD", command=remove_destination)
    remove_destination_btn.grid(row=0, column=1, padx=10)

    view_trip_btn = tk.Button(btn_frame, text="View Trip", width=30, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD", command=view_trip)
    view_trip_btn.grid(row=0, column=2, padx=10)

    close_btn = tk.Button(btn_frame, text="Close", command=flights.destroy, width=30, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD")
    close_btn.grid(row=0, column=3, padx=10)

if __name__ == "__main__":
    show_trip_menu()
