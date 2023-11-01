import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
import csv

def remove_destination():
    def validate_entries(*args):
        country = country_entry.get()
        city = city_entry.get()
        if country and city:
            remove_button.config(state="normal")
        else:
            remove_button.config(state="disabled")

    destinations = tk.Toplevel()
    destinations.title("Remove Destination")

    # Set the icon photo for the Toplevel window
    image = Image.open("destinations/destinations_icon.png")
    icon = ImageTk.PhotoImage(image)
    destinations.iconphoto(False, icon)

    destinations.geometry('800x600')
    destinations.configure(bg='white')

    # Load the top image
    top_image = Image.open('destinations/destination.png')
    top_image = top_image.resize((1400, 300), Image.ANTIALIAS)
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(destinations, image=top_image, bg='white')
    header_label.image = top_image
    header_label.grid(row=0, column=0, columnspan=2)

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")

    welcome_label = tk.Label(destinations, text="Remove a Destination", font=custom_font, bg="white", fg="#00B2EE")
    welcome_label.grid(row=1, column=0, columnspan=2, pady=20)

    # Create labels and entry widgets for destination information
    country_label = tk.Label(destinations, text="Country", fg="#00B2EE", bg="white")
    country_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')

    country_entry = tk.Entry(destinations, bg='white')
    country_entry.grid(row=2, column=1, padx=10, pady=5)
    country_entry.insert(0, "")  # Initialize entry with an empty string
    country_entry.bind("<KeyRelease>", validate_entries)  # Bind validation function to entry

    city_label = tk.Label(destinations, text="City", fg="#00B2EE", bg="white")
    city_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')

    city_entry = tk.Entry(destinations, bg='white')
    city_entry.grid(row=3, column=1, padx=10, pady=5)
    city_entry.insert(0, "")  # Initialize entry with an empty string
    city_entry.bind("<KeyRelease>", validate_entries)  # Bind validation function to entry

    # Frame for buttons
    button_frame = tk.Frame(destinations, bg="#00B2EE")
    button_frame.grid(row=4, column=0, columnspan=2, sticky='s')

    def remove_from_csv():
        country = country_entry.get()
        city = city_entry.get()

        # Read the existing data from the CSV file
        with open("destinations/destinations.csv", "r") as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)

        # Search for destinations and remove the matching entries
        new_data = [entry for entry in data if entry[0] != country or entry[1] != city]

        # Write the updated data back to the CSV file
        with open("destinations/destinations.csv", "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(new_data)

        # Clear the entry widgets after removing
        country_entry.delete(0, tk.END)
        city_entry.delete(0, tk.END)
        remove_button.config(state="disabled")  # Disable "Remove" button

    remove_button = tk.Button(button_frame, text="Remove", command=remove_from_csv, activebackground="#009ACD", width=50, foreground="white", border=0, background="#00B2EE", state="disabled")
    remove_button.grid(row=0, column=0, padx=10)

    close_btn = tk.Button(button_frame, text="Close", command=destinations.destroy, foreground="white", border=0, width=50, background="#00B2EE", activebackground="#009ACD")
    close_btn.grid(row=0, column=1)

    destinations.columnconfigure(1, weight=1)
    destinations.rowconfigure(4, weight=1)

# Call the remove_destination function to display the window
if __name__ == "__main__":
    remove_destination()
