import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image

from destinations.view_destinations import view_destinations
from destinations.view_destinations_filtered import view_destinations_filtered
from destinations.add_destination import add_destination
from destinations.remove_destination import remove_destination

def show_destinations_menu(admin_name):
    destinations = tk.Toplevel()
    destinations.title("Explore Destinations")
    
    # Set the icon photo for the Toplevel window
    image = Image.open("destinations/destinations_icon.png")
    icon = ImageTk.PhotoImage(image)
    destinations.iconphoto(False, icon)
    
    destinations.geometry('1640x800')
    destinations.configure(bg='white')

    # Load the top image
    top_image = Image.open('destinations/destination.png')
    top_image = top_image.resize((1640, 300), Image.ANTIALIAS)  # Resize the image to fit the label
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(destinations, image=top_image, bg='white')
    header_label.image = top_image  # Keep a reference to the image to prevent it from being garbage collected
    header_label.pack()

    # Section Line
    canvas = tk.Canvas(destinations, width=1640, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")
    
    welcome_label = tk.Label(destinations, text=f"Hi {admin_name}, welcome to the Destinations section", bg="white", font=custom_font, fg="#00B2EE")
    welcome_label.pack(pady=20)

    # Section Line
    canvas = tk.Canvas(destinations, width=1640, height=2, highlightthickness=0)
    canvas.pack()

    # Buttons for Destinations Menu
    btn_frame = tk.Frame(destinations, bg='#00B2EE')
    btn_frame.pack(pady=20, fill="x", side="bottom")

    view_all_btn = tk.Button(btn_frame, text="View All Destinations", width=30, height=2, fg="white", bg="#00B2EE", activebackground="#009ACD", borderwidth=0, command=view_destinations)
    view_all_btn.grid(row=0, column=0, padx=10)

    view_by_country_btn = tk.Button(btn_frame, text="View Destinations by Country", width=35, height=2, fg="white", bg="#00B2EE", activebackground="#009ACD", borderwidth=0, command=view_destinations_filtered)
    view_by_country_btn.grid(row=0, column=1, padx=10)

    add_destination_btn = tk.Button(btn_frame, text="Add Destination", width=35, height=2, fg="white", bg="#00B2EE", borderwidth=0, activebackground="#009ACD", command=add_destination)
    add_destination_btn.grid(row=0, column=2, padx=10)

    remove_destination_btn = tk.Button(btn_frame, text="Remove Destination", width=30, height=2, fg="white", bg="#00B2EE", activebackground="#009ACD", borderwidth=0, command=remove_destination)
    remove_destination_btn.grid(row=0, column=3, padx=10)

    close_btn = tk.Button(btn_frame, text="Close", command=destinations.destroy, width=30, height=2, fg="white", bg="#00B2EE", activebackground="#009ACD", borderwidth=0)
    close_btn.grid(row=0, column=4, padx=10)

# Call the show_destinations_menu function to display the window
if __name__ == "__main__":
    show_destinations_menu()
