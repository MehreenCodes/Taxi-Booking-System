import tkinter
import tkinter as tk
from customer import customer_window  # Import the customer function
from driver import driver_window      # Import the driver function
from admin import admin_window        # Import the admin function

# Main Window
root = tk.Tk()
root.title("Taxi Booking System")
root.configure(bg="beige")
 
#  Welcome Message
label = tk.Label(
    root,
    text="Welcome to the EasyRide Taxi Booking Service",
    fg="black",
    bg="beige",
    font=("Times", 30, "bold"),
    padx=60,
    pady=60
)
label.pack()

# Create buttons for different user
# Each button will open a different window (customer, driver, admin)
customerbutton = tk.Button(root, text="Customer", command=lambda: customer_window(root), width=15, bg="light blue", fg="black", font=("Times", 15))
customerbutton.pack(pady=20)

driverbutton= tk.Button(root, text="Driver", command=lambda: driver_window(root), width=15, bg="thistle", fg="black", font=("Times", 15))
driverbutton.pack(pady=20)

adminbutton = tk.Button(root, text="Administrator", command=lambda: admin_window(root), width=15, bg="light pink", fg="black", font=("Times", 15))
adminbutton.pack(pady=20)

# Main Loop
root.mainloop()