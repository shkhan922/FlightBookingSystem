import tkinter as tk
from tkinter import ttk, font
from PIL import ImageTk, Image
import csv

def view_flights_filtered():
    flights = tk.Toplevel()
    flights.title("Filtered Flights")

    # Set the icon photo for the Toplevel window
    image = Image.open('flights/flights_icon.png')
    icon = ImageTk.PhotoImage(image)
    flights.iconphoto(False, icon)

    flights.geometry('1640x800')
    flights.configure(bg='white')

    # Load the top image
    top_image = Image.open('flights/flight.png')
    top_image = top_image.resize((1640, 300), Image.ANTIALIAS)
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(flights, image=top_image, bg='white')
    header_label.image = top_image
    header_label.pack()

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")

    welcome_label = tk.Label(flights, text="Filtered Flight", bg="white", font=custom_font, fg="#00B2EE")
    welcome_label.pack(pady=20)

    # Create a Treeview widget for displaying the table
    tree = ttk.Treeview(flights, columns=("Airline", "Flight Number", "Takeoff Country", "Landing Country", "Cost"))

    # Define column names
    tree.heading("#1", text="Airline")
    tree.heading("#2", text="Flight Number")
    tree.heading("#3", text="Takeoff Country")
    tree.heading("#4", text="Landing Country")
    tree.heading("#5", text="Cost")

    # Set column text color to light blue
    style = ttk.Style()
    style.configure("Treeview.Heading", foreground="#00B2EE")

    # Load data from the CSV file and insert it into the table
    data = []
    with open("flights/flights.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            tree.insert("", "end", values=row)
            data.append(row)
    
    # Create a search box to filter flights by country name
    search_frame = tk.Frame(flights, bg="white")
    search_frame.pack(pady=10, padx=30, fill="x")

    search_entry = tk.Entry(search_frame)
    search_entry.pack(fill="x")

    def search_flights(event):
        search_text = search_entry.get().lower()
        tree.delete(*tree.get_children())  # Clear the treeview
        for row in data:
            values = [value.lower() for value in row]
            if search_text in values:
                tree.insert("", "end", values=row)

    search_entry.bind("<KeyRelease>", search_flights)

    # Create a vertical scrollbar on the right side
    vsb = ttk.Scrollbar(flights, orient="vertical", command=tree.yview)

    # Pack the Treeview and scrollbar
    tree.pack(expand=True)
    vsb.pack(fill="y", side="right")

    # Configure the tree widget's yscrollcommand to work with the scrollbar
    tree.configure(yscrollcommand=vsb.set)

    # Create a ttk Style to set the background color
    style = ttk.Style()
    style.configure("Background.TFrame", background="#00B2EE")

    btn_frame = ttk.Frame(flights, style="Background.TFrame")
    btn_frame.pack(pady=20, fill="x", side="bottom")

    close_btn = tk.Button(btn_frame, text="Close", command=flights.destroy, width=100, foreground="white", border=0, background="#00B2EE", activebackground="#009ACD")
    close_btn.pack(side="bottom")  # Place the close button at the bottom of btn_frame

    # Call the view_flights_filtered function to display the window
    if __name__ == "__main__":
        view_flights_filtered()
