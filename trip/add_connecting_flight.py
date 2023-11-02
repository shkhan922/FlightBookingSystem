import tkinter as tk
from tkinter import PhotoImage, font, Listbox, END, messagebox
from PIL import ImageTk, Image
import csv
from functools import partial  # Import functools.partial
from error_window import show_error_window



def find_and_save_connecting_flights():
    # Read destinations from trip/destinations.csv
    destinations = read_destinations()

    # Find and save corresponding flights based on destinations
    saved_flights = find_and_save_corresponding_flights(destinations)

    if saved_flights:
        success_message = "Connecting flights added successfully."
        messagebox.showinfo("Success", success_message)
    else:
        no_flights_message = "No matching flights found for the selected destinations."
        show_error_window("Item not found exception", no_flights_message)

def read_destinations():
    destinations = []
    with open('trip/destinations.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                destination, country = row[0], row[1]
                destinations.append((destination, country))
    return destinations

def find_and_save_corresponding_flights(destinations):
    corresponding_flights = []

    with open('flights/flights.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for destination, country in destinations:
                # Check if the last field contains a valid price (assuming it's a numeric value)
                if len(row) >= 5 and row[2] == country and row[4].isdigit():
                    corresponding_flights.append(row)

    save_connecting_flights(corresponding_flights)
    return corresponding_flights

def save_connecting_flights(added_flights):
    with open('trip/connecting_flights.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(added_flights)
