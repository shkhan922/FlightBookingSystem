import tkinter as tk
from tkinter import PhotoImage, font
from PIL import ImageTk, Image

def add_flight():
    flights = tk.Toplevel()
    flights.title("Add Flight")
    
    # Set the icon photo for the Toplevel window
    image = Image.open("flights/flights_icon.png")
    icon = ImageTk.PhotoImage(image)
    flights.iconphoto(False, icon)
    
    flights.geometry('1640x600')
    flights.configure(bg='white')

    # Load the top image
    myimg = ImageTk.PhotoImage(Image.open('flights/flight.png'))
    header_label = tk.Label(flights, image=myimg)
    header_label.pack(pady=10)

    # Section Line
    canvas = tk.Canvas(flights, width=1640, height=2, bg='#ADD8E6', highlightthickness=0)
    canvas.pack()

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")
    
    welcome_label = tk.Label(flights, text="Add a Flight", bg="white", font=custom_font, fg="#ADD8E6")
    welcome_label.pack(pady=20)

    # Section Line
    canvas = tk.Canvas(flights, width=1640, height=2, bg='#ADD8E6', highlightthickness=0)
    canvas.pack()

    # Buttons for Flights Menu
    btn_frame = tk.Frame(flights, bg='#ADD8E6')
    btn_frame.pack(pady=20)

    

    close_btn = tk.Button(btn_frame, text="Close", command=flights.destroy, width=15, height=2, fg="white", bg="#ADD8E6", borderwidth=0)
    close_btn.grid(row=0, column=4, padx=10)

# Call the show_flights_menu function to display the window
if __name__ == "__main__":
    add_flight()
