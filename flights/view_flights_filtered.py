import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
from tkinter import ttk
import csv

def view_flights_filtered():
    flights = tk.Toplevel()
    flights.title("Display Flights Filtered")
    
    # Set the icon photo for the Toplevel window
    image = Image.open('flights/flights_icon.png')
    icon = ImageTk.PhotoImage(image)
    flights.iconphoto(False, icon)
    
    flights.geometry('1640x800')
    flights.configure(bg='white')

    # Load the top image
    top_image = Image.open('flights/flight.png')
    top_image = top_image.resize((900, 300), Image.ANTIALIAS)
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(flights, image=top_image, bg='white')
    header_label.image = top_image
    header_label.pack()

    # Section Line
    canvas = tk.Canvas(flights, width=1640, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")
    
    welcome_label = tk.Label(flights, text="Filtered Flights", bg="white", font=custom_font, fg="#00B2EE")
    welcome_label.pack(pady=20)

    # Section Line
    canvas = tk.Canvas(flights, width=1640, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

     # Create a search box to filter flights by country name
    search_frame = ttk.Frame(flights, style="Background.TFrame")
    search_frame.pack(pady=10)

    search_label = ttk.Label(search_frame, text="Search by Country Name:")
    search_label.grid(row=0, column=0, padx=5)

    search_entry = ttk.Entry(search_frame)
    search_entry.grid(row=0, column=1, padx=5)

    def search_flights(event):
        search_text = search_entry.get().lower()
        for item in tree.get_children():
            values = tree.item(item, "values")
            if search_text in [str(value).lower() for value in values]:
                tree.selection_set(item)
            else:
                tree.selection_remove(item)

    search_entry.bind("<KeyRelease>", search_flights)

    # Section Line
    canvas = tk.Canvas(flights, width=1640, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

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

    # Insert data from CSV into the table
    with open("flights/flights.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            tree.insert("", "end", values=row)

    # Pack the Treeview and scrollbar
    tree.pack(expand=True, fill="both")
    vsb.pack(side="left", fill="y")

    # Create a ttk Style to set the background color
    style = ttk.Style()
    style.configure("Background.TFrame", background="#00B2EE")

   

    # Buttons for Flights Menu
    btn_frame = ttk.Frame(flights, style="Background.TFrame")
    btn_frame.pack(pady=20, fill="x", side="bottom")

    close_btn = tk.Button(btn_frame, text="Close", border=0, background="#00B2EE",activebackground="#009ACD",command=flights.destroy)
    close_btn.grid(row=0, column=4, padx=10)

# Call the view_flights_filtered function to display the window
if __name__ == "__main__":
    view_flights_filtered()
