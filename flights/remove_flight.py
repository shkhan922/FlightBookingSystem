import tkinter as tk
from tkinter import PhotoImage, font, messagebox
from PIL import ImageTk, Image
import csv
from error_window import show_error_window

def remove_flight():
    def validate_entries(*args):
        takeoff = takeoff_country_entry.get()
        landing = landing_country_entry.get()
        if takeoff and landing:
            remove_button.config(state="normal")
        else:
            remove_button.config(state="disabled")

    flights = tk.Toplevel()
    flights.title("Remove Flight")

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

    welcome_label = tk.Label(flights, text="Remove a Flight", font=custom_font, bg="white", fg="#00B2EE")
    welcome_label.grid(row=1, column=0, columnspan=2, pady=20)

    # Create labels and entry widgets for flight information
    takeoff_country_label = tk.Label(flights, text="Takeoff Country", fg="#00B2EE", bg="white")
    takeoff_country_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')

    takeoff_country_entry = tk.Entry(flights, bg='white')
    takeoff_country_entry.grid(row=2, column=1, padx=10, pady=5)
    takeoff_country_entry.insert(0, "")  # Initialize entry with an empty string
    takeoff_country_entry.bind("<KeyRelease>", validate_entries)  # Bind validation function to entry

    landing_country_label = tk.Label(flights, text="Landing Country", fg="#00B2EE", bg="white")
    landing_country_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')

    landing_country_entry = tk.Entry(flights, bg='white')
    landing_country_entry.grid(row=3, column=1, padx=10, pady=5)
    landing_country_entry.insert(0, "")  # Initialize entry with an empty string
    landing_country_entry.bind("<KeyRelease>", validate_entries)  # Bind validation function to entry

    # Frame for buttons
    button_frame = tk.Frame(flights, bg="#00B2EE")
    button_frame.grid(row=4, column=0, columnspan=2, sticky='s')

    def remove_from_csv():
        takeoff = takeoff_country_entry.get()
        landing = landing_country_entry.get()

        # Read the existing data from the CSV file
        with open("flights/flights.csv", "r") as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)

        # Search for flights and remove the matching entries
        new_data = [entry for entry in data if entry[2] != takeoff or entry[3] != landing]

        if data == new_data:
            # Entry not found, show an error message
            # messagebox.showerror("Entry Not Found", "Flight not found. Please check the takeoff and landing countries.")
            show_error_window("Item not found exception","Please enter the correct take off or landing country")
        else:
            # Write the updated data back to the CSV file
            with open("flights/flights.csv", "w", newline="") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(new_data)

            # Clear the entry widgets after removing
            takeoff_country_entry.delete(0, tk.END)
            landing_country_entry.delete(0, tk.END)
            remove_button.config(state="disabled")  # Disable "Remove" button

    remove_button = tk.Button(button_frame, text="Remove", command=remove_from_csv, activebackground="#009ACD", width=50, foreground="white", border=0, background="#00B2EE", state="disabled")
    remove_button.grid(row=0, column=0, padx=10)

    close_btn = tk.Button(button_frame, text="Close", command=flights.destroy, foreground="white", border=0, width=50, background="#00B2EE", activebackground="#009ACD")
    close_btn.grid(row=0, column=1)

    flights.columnconfigure(1, weight=1)
    flights.rowconfigure(4, weight=1)

# Call the remove_flight function to display the window
if __name__ == "__main__":
    remove_flight()
