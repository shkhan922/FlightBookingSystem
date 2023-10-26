import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Create a dictionary to store user credentials (username: password)
user_credentials = {"admin": "admin123"}

# Function to verify user credentials
def verify_credentials():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in user_credentials and user_credentials[username] == password:
        show_admin_page()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to display the admin page
def show_admin_page():
    login_frame.pack_forget()  # Hide the login frame
    admin_frame.pack()  # Show the admin frame
    welcome_label.config(text=f"Welcome, {username_entry.get()}!")

# Create the main window
root = tk.Tk()
root.title("Flight Booking System")

# Style configuration
style = ttk.Style()
style.configure("TButton", foreground="black", background="lightblue")

# Login Frame
login_frame = ttk.Frame(root)
login_frame.pack()

login_label = ttk.Label(login_frame, text="Login")
login_label.grid(row=0, column=1, padx=10, pady=10)

username_label = ttk.Label(login_frame, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=10)
username_entry = ttk.Entry(login_frame)
username_entry.grid(row=1, column=1, padx=10, pady=10)

password_label = ttk.Label(login_frame, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=10)
password_entry = ttk.Entry(login_frame, show="*")  # Hide the password
password_entry.grid(row=2, column=1, padx=10, pady=10)

login_button = ttk.Button(login_frame, text="Login", command=verify_credentials)
login_button.grid(row=3, column=1, padx=10, pady=10)

# Admin Frame
admin_frame = ttk.Frame(root)
admin_frame.pack_forget()

# Load and display an image on the admin screen
image = Image.open("agency.png")  # Replace "agency.png" with the path to your image
photo = ImageTk.PhotoImage(image)
canvas = tk.Canvas(admin_frame, width=image.width, height=image.height)
canvas.create_image(0, 0, anchor=tk.NW, image=photo)
canvas.pack()

welcome_label = ttk.Label(admin_frame, text="", font=("Arial", 16))
welcome_label.pack()

# Buttons aligned horizontally at the bottom of the canvas
button_frame = ttk.Frame(admin_frame)
button_frame.pack(side=tk.BOTTOM)

explore_flights_button = ttk.Button(button_frame, text="Explore Flights")
explore_flights_button.pack(side=tk.LEFT, padx=10, pady=10)

explore_destinations_button = ttk.Button(button_frame, text="Explore Destinations")
explore_destinations_button.pack(side=tk.LEFT, padx=10, pady=10)

book_trip_button = ttk.Button(button_frame, text="Book a Trip")
book_trip_button.pack(side=tk.LEFT, padx=10, pady=10)

exit_button = ttk.Button(button_frame, text="Exit", command=root.destroy)
exit_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
