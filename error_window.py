import tkinter as tk
from tkinter import font, ttk
from PIL import ImageTk, Image



def show_error_window(error_message):
    flights = tk.Toplevel()
    flights.title("Error")
    
    # Set the icon photo for the Toplevel window
    image = Image.open("error_icon.png")
    icon = ImageTk.PhotoImage(image)
    flights.iconphoto(False, icon)
    
    flights.geometry('800x600')
    flights.configure(bg='white')

    # Load the top image
    top_image = Image.open('error.png')
    top_image = top_image.resize((800, 300), Image.ANTIALIAS)  # Resize the image to fit the label
    top_image = ImageTk.PhotoImage(top_image)

    header_label = tk.Label(flights, image=top_image, bg='white')
    header_label.image = top_image  # Keep a reference to the image to prevent it from being garbage collected
    header_label.pack()


    # Section Line
    canvas = tk.Canvas(flights, width=1640, height=2, bg='#00B2EE', highlightthickness=0)
    canvas.pack()

    # Custom font for welcome message
    custom_font = font.Font(family="Helvetica", size=18, weight="bold")
    
    welcome_label = tk.Label(flights, text="Error", bg="white", font=custom_font, fg="#00B2EE")
    welcome_label.pack(pady=20)

    # Section Line
    canvas = tk.Canvas(flights, width=1640, height=2, highlightthickness=0)
    canvas.pack()

    error_label = tk.Label(flights, text=error_message, bg="#E0E0E0", fg="red")
    error_label.pack(pady=20)

    # Buttons for Flights Menu
    btn_frame = tk.Frame(flights, bg='#00B2EE')
    btn_frame.pack(pady=20, fill="x",side="bottom")

    
    close_btn = tk.Button(btn_frame, text="Close", command=flights.destroy, width=100, height=2, fg="white", bg="#00B2EE", activebackground="#009ACD", borderwidth=0)
    close_btn.grid(row=0, column=4, padx=10)

# Call the show_flights_menu function to display the window
if __name__ == "__main__":
    show_error_window()
