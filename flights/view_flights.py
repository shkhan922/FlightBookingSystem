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

    flights.geometry('1400x800')
    flights.configure(bg='white')

    # Load the top image
    top_image = Image.open('flights/flight.png')
    top_image = top_image.resize((900, 300), Image.ANTIALIAS)
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(flights, image=top_image, bg='white')
    header_label.image = top_image
    header_label.pack()

    # Section Line
    canvas = tk.Canvas(flights, width=1400, height=2, bg='#ADD8E6', highlightthickness=0)
    canvas.pack()

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")

    welcome_label = tk.Label(flights, text="Flights", font=custom_font, bg="white", fg="#ADD8E6")
    welcome_label.pack(pady=20)

    # Create a Treeview widget for displaying the table
    tree = ttk.Treeview(flights, columns=("Airline", "Flight Number", "Takeoff Country", "Landing Country", "Cost"))

    # Define column names
    tree.heading("#1", text="Airline")
    tree.heading("#2", text="Flight Number")
    tree.heading("#3", text="Takeoff Country")
    tree.heading("#4", text="Landing Country")
    tree.heading("#5", text="Cost")

    # Add a vertical scrollbar
    vsb = ttk.Scrollbar(flights, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    # Read data from a CSV file and insert it into the table
    with open("flights/flights.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            tree.insert("", "end", values=row)

    # Pack the Treeview and scrollbar
    tree.pack(expand=True, fill="both")
    vsb.pack(side="right", fill="y")

    # Create a ttk Style to set the background color
    style = ttk.Style()
    style.configure("Background.TFrame", background="#ADD8E6")

    # Section Line
    canvas = tk.Canvas(flights, width=1400, height=2, bg='#ADD8E6', highlightthickness=0)
    canvas.pack()

    btn_frame = ttk.Frame(flights, style="Background.TFrame")
    btn_frame.pack(pady=20)

    close_btn = tk.Button(btn_frame, text="Close", command=flights.destroy, foreground="white", border=0, background="#ADD8E6")
    close_btn.grid(row=0, column=4, padx=10)

# Call the view_flights function to display the window
if __name__ == "__main__":
    view_flights()
