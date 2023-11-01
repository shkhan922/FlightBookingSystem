import tkinter as tk
from tkinter import PhotoImage, font, Listbox, END, messagebox
from PIL import ImageTk, Image
import csv
from trip.add_trip_destination import add_trip_destination
from trip.remove_destination_trip import remove_destination_trip
from destinations.view_destinations import view_destinations
from trip.add_connecting_flight import add_connecting_flights  # Import the add_connecting_flights function
from functools import partial

def load_destinations(trip_list):
    with open('trip/destinations.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        destinations = [row[0] for row in reader]

    trip_list.delete(0, END)
    for destination in destinations:
        trip_list.insert(END, destination)

def view_trip():
    trip_window = tk.Toplevel()
    trip_window.title("Display Trip")

    image = Image.open("trip/trip_icon.png")
    icon = ImageTk.PhotoImage(image)
    trip_window.iconphoto(False, icon)

    trip_window.geometry('1640x800')
    trip_window.configure(bg='white')

    top_image = Image.open('trip/trip.png')
    top_image = top_image.resize((1640, 300), Image.ANTIALIAS)
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

    trip_list = Listbox(trip_window, width=60, height=15, bg="white", selectbackground="#00B2EE", selectmode=tk.MULTIPLE)

    load_destinations(trip_list)

    trip_list.pack(pady=20)

    def view_individual_destinations():
        selected_indices = trip_list.curselection()
        for index in selected_indices:
            destination = trip_list.get(index)
            view_destinations(destination)
            # Handle the destination here (e.g., open view_destination)

    button_frame = tk.Frame(trip_window, bg="#00B2EE")
    button_frame.pack(pady=10, fill="x")

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

    btn_frame = tk.Frame(flights, bg='#00B2EE')
    btn_frame.pack(pady=20, fill="x", side="bottom")

    add_destination_btn = tk.Button(btn_frame, text="Add Destination", width=30, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD", command=add_trip_destination)
    add_destination_btn.grid(row=0, column=0, padx=10)

    remove_destination_btn = tk.Button(btn_frame, text="Remove Destination", width=35, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD", command=remove_destination_trip)
    remove_destination_btn.grid(row=0, column=1, padx=10)

    add_connecting_btn = tk.Button(btn_frame, text="Add Connecting Flights", width=35, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD", command=lambda: add_connecting_flights(trip_list))
    add_connecting_btn.grid(row=0, column=2, padx=10)

    view_trip_btn = tk.Button(btn_frame, text="View Trip", width=30, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD", command=view_trip)
    view_trip_btn.grid(row=0, column=3, padx=10)

    close_btn = tk.Button(btn_frame, text="Close", command=flights.destroy, width=30, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD")
    close_btn.grid(row=0, column=4, padx=10)

if __name__ == "__main__":
    show_trip_menu("Admin Name")
