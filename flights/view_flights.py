import tkinter as tk
from tkinter import PhotoImage, font
from PIL import ImageTk, Image
from tkinter import ttk
import csv

def view_flights():
    flights = tk.Toplevel()
    flights.title("View Flights")

    # Set the icon photo for the Toplevel window
    image = Image.open("flights/flights_icon.png")
    icon = ImageTk.PhotoImage(image)
    flights.iconphoto(False, icon)

    flights.geometry('1200x800')
    flights.configure(bg='white')

    # Load the top image
    top_image = Image.open('flights/flight.png')
    top_image = top_image.resize((1400, 300), Image.ANTIALIAS)
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(flights, image=top_image, bg='white')
    header_label.image = top_image
    header_label.grid(row=0, column=0, columnspan=2)

    # Section Line
    canvas = tk.Canvas(flights, width=1400, height=2, highlightthickness=0)
    canvas.grid(row=1, column=0, columnspan=2)

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")

    welcome_label = tk.Label(flights, text="Flights", font=custom_font, bg="white", fg="#00B2EE")
    welcome_label.grid(row=2, column=0, columnspan=2, pady=20)

    # Create a Treeview widget for displaying the table
    tree = ttk.Treeview(flights, columns=("Airline", "Flight Number", "Takeoff Country", "Landing Country", "Cost"))

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
    with open("flights/flights.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            tree.insert("", "end", values=row)

    # Create a vertical scrollbar
    vsb = ttk.Scrollbar(flights, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    # Grid layout for the treeview and scrollbar
    tree.grid(row=3, column=0, columnspan=2, sticky="nsew")
    vsb.grid(row=3, column=2, sticky="ns")

    # Make the rows and columns expand with window resizing
    flights.grid_rowconfigure(3, weight=1)
    flights.grid_columnconfigure(0, weight=1)

    # Create a ttk Style to set the background color
    style = ttk.Style()
    style.configure("Background.TFrame", background="#00B2EE")

    btn_frame = ttk.Frame(flights, style="Background.TFrame")
    btn_frame.grid(row=4, column=0, columnspan=2, pady=20)

    close_btn = tk.Button(btn_frame, text="Close", command=flights.destroy, width=100, foreground="white", border=0, background="#00B2EE", activebackground="#009ACD")
    close_btn.grid(row=0, column=4)

# Call the view_flights function to display the window
if __name__ == "__main__":
    view_flights()
