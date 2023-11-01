import tkinter as tk
from tkinter import PhotoImage, font, Listbox, END, messagebox
from PIL import ImageTk, Image
import csv
from functools import partial  # Import functools.partial

def load_destinations(trip_list):
    with open('trip/destinations.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        destinations = [row[0] for row in reader]

    trip_list.delete(0, END)
    for destination in destinations:
        trip_list.insert(END, destination)

def add_connecting_flights(trip_list):
    selected_indices = trip_list.curselection()
    added_flights = []

    for index in selected_indices:
        selected_destination = trip_list.get(index)

        # Read the selected destination information
        destination_info = read_destination_info(selected_destination)

        if not destination_info:
            error_message = f"Could not find information for '{selected_destination}'."
            messagebox.showerror("Error", error_message)
            continue

        destination_country = destination_info["Country"]

        # Find a corresponding flight based on the destination country
        corresponding_flight = find_corresponding_flight(destination_country)

        if corresponding_flight:
            added_flights.append(corresponding_flight)

    if added_flights:
        save_connecting_flights(added_flights)

        success_message = "Connecting flights added successfully."
        messagebox.showinfo("Success", success_message)
    else:
        no_flights_message = "No matching flights found for the selected destinations."
        messagebox.showinfo("Information", no_flights_message)

def read_destination_info(selected_destination):
    destination_info = {}
    
    # Implement code to read destination information from trip/destinations.csv
    # The file format should include columns like 'Destination', 'Country', and so on
    # Use the csv module to read the data from the CSV file
    with open('trip/destinations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Destination'] == selected_destination:
                destination_info['Destination'] = row['Destination']
                destination_info['Country'] = row['Country']
                # Add more fields as needed

    return destination_info

def find_corresponding_flight(destination_country):
    corresponding_flight = None
    
    # Implement code to search for a corresponding flight in flights/flights.csv
    # The file format should include columns like 'Country', 'FlightNumber', 'Details', etc.
    # Use the csv module to read the data from the CSV file
    with open('flights/flights.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Country'] == destination_country:
                corresponding_flight = row
                # Optionally, you can return a specific field, e.g., row['FlightNumber']

    return corresponding_flight

def save_connecting_flights(added_flights):
    # Implement code to save the added flights to trip/connecting_flights.csv
    # The file format should include columns like 'FlightNumber', 'Destination', and so on
    # Use the csv module to write the data to the CSV file
    with open('trip/connecting_flights.csv', 'a', newline='') as csvfile:
        fieldnames = ['FlightNumber', 'Destination']  # Update with actual field names
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for flight in added_flights:
            writer.writerow(flight)
