import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image

def view_flights_filtered():
    flights = tk.Toplevel()
    flights.title("Display Flights Filtered")
    
    # Set the icon photo for the Toplevel window
    image = Image.open('flights/flights_icon.png')
    icon = ImageTk.PhotoImage(image)
    flights.iconphoto(False, icon)
    
    flights.geometry('1640x600')
    flights.configure(bg='white')
    

      # Load the top image
    top_image = Image.open('flights/flight.png')
    top_image = top_image.resize((900, 300), Image.ANTIALIAS)  # Resize the image to fit the label
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(flights, image=top_image, bg='white')
    header_label.image = top_image  # Keep a reference to the image to prevent it from being garbage collected
    header_label.pack()
   
    # Section Line
    canvas = tk.Canvas(flights, width=1640, height=2, bg='#ADD8E6', highlightthickness=0)
    canvas.pack()

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")
    
    welcome_label = tk.Label(flights, text="Filtered Flights", bg="white", font=custom_font, fg="#ADD8E6")
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
    view_flights_filtered()
