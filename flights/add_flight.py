import tkinter as tk
from tkinter import PhotoImage, font
from PIL import ImageTk, Image
import csv

def add_flight():
    def validate_entries(*args):
        all_filled = all(entry.get() for entry in entries)
        if all_filled:
            add_button.config(state="normal")
        else:
            add_button.config(state="disabled")

    flights = tk.Toplevel()
    flights.title("Add Flight")

    # Set the icon photo for the Toplevel window
    image = Image.open("flights/flights_icon.png")
    icon = ImageTk.PhotoImage(image)
    flights.iconphoto(False, icon)

    flights.geometry('800x600')
    flights.configure(bg='white')

    # Load the top image
    top_image = Image.open('flights/flight.png')
    top_image = top_image.resize((1400, 300), Image.ANTIALIAS)
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(flights, image=top_image, bg='white')
    header_label.image = top_image
    header_label.grid(row=0, column=0, columnspan=2)

    

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")

    welcome_label = tk.Label(flights, text="Add a Flight", font=custom_font, bg="white", fg="#00B2EE")
    welcome_label.grid(row=1, column=0, columnspan=2, pady=20)

   


    # Create labels and entry widgets for flight information
    labels = ["Airline", "Flight Number", "Takeoff Country", "Landing Country", "Cost"]
    entries = []

    for i, label_text in enumerate(labels):
        label = tk.Label(flights, text=label_text, fg="#00B2EE", bg="white")
        label.grid(row=i + 2, column=0, padx=10, pady=5, sticky='w')

        entry = tk.Entry(flights, bg='white')
        entry.grid(row=i + 2, column=1, padx=10, pady=5)
        entry.insert(0, "")  # Initialize entries with empty strings
        entries.append(entry)
        entry.bind("<KeyRelease>", validate_entries)  # Bind validation function to entry

    # Frame for buttons
    button_frame = tk.Frame(flights, bg="#00B2EE")
    button_frame.grid(row=7, column=0, columnspan=2, sticky='s')

    def add_to_csv():
        # Get the data from entry widgets
        data = [entry.get() for entry in entries]

        # Append the data to the CSV file
        with open("flights/flights.csv", "a", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(data)

        # Clear the entry widgets after adding
        for entry in entries:
            entry.delete(0, tk.END)
            add_button.config(state="disabled")  # Disable "Add" button

    add_button = tk.Button(button_frame, text="Add", command=add_to_csv, activebackground="#009ACD", width=50, foreground="white", border=0, background="#00B2EE", state="disabled")
    add_button.grid(row=0, column=0)

    close_btn = tk.Button(button_frame, text="Close", command=flights.destroy, foreground="white", border=0, width=50, background="#00B2EE", activebackground="#009ACD")
    close_btn.grid(row=0, column=1)

    flights.columnconfigure(1, weight=1)
    flights.rowconfigure(7, weight=1)

# Call the add_flight function to display the window
if __name__ == "__main__":
    add_flight()
