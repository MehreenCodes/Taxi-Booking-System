import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Temporary user data storage
user_data = {}
customer_bookings = []  # Store bookings

# Sign-up window definition
def sign_up_window(parent):
    sign_up_window = tk.Toplevel(parent)
    sign_up_window.title("Create an Account")
    sign_up_window.configure(bg="light grey")

    tk.Label(sign_up_window, text="Create an Account", font=("Times", 20), bg="light grey").pack(pady=20)

    tk.Label(sign_up_window, text="Username:", font=("Times", 15), bg="light grey").pack(pady=5)
    username_entry = tk.Entry(sign_up_window, font=("Times", 15), width=30)
    username_entry.pack(pady=10)

    tk.Label(sign_up_window, text="Password:", font=("Times", 15), bg="light grey").pack(pady=5)
    password_entry = tk.Entry(sign_up_window, font=("Times", 15), width=30, show="*")
    password_entry.pack(pady=10)

    tk.Label(sign_up_window, text="Email:", font=("Times", 15), bg="light grey").pack(pady=5)
    email_entry = tk.Entry(sign_up_window, font=("Times", 15), width=30)
    email_entry.pack(pady=10)

    tk.Label(sign_up_window, text="Phone Number:", font=("Times", 15), bg="light grey").pack(pady=5)
    phonenumber_entry = tk.Entry(sign_up_window, font=("Times", 15), width=30)
    phonenumber_entry.pack(pady=10)

    tk.Label(sign_up_window, text="Address:", font=("Times", 15), bg="light grey").pack(pady=5)
    address_entry = tk.Entry(sign_up_window, font=("Times", 15), width=30)
    address_entry.pack(pady=10)

    def register_user():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "all fields need to be filled")
        elif username == password:
            messagebox.showerror("Error", "Password cannot be the same as Username.")
        elif username in user_data:
            messagebox.showerror("Error", "Username already exists.")
        else:
            user_data[username] = password
            messagebox.showinfo("Success", "Account has been created successfully!")
            sign_up_window.destroy()

    tk.Button(
        sign_up_window,
        text="Sign Up",
        command=register_user,
        font=("Times", 15),
        bg="light blue",
        width=15
    ).pack(pady=20)

# Log-in window definition
def log_in_window(parent):
    log_in_window = tk.Toplevel(parent)
    log_in_window.title("Log In")
    log_in_window.configure(bg="light grey")

    tk.Label(log_in_window, text="Welcome, please log In to get started", font=("Times", 20), bg="light grey").pack(pady=20)

    tk.Label(log_in_window, text="Username:", font=("Times", 15), bg="light grey").pack(pady=5)
    username_entry = tk.Entry(log_in_window, font=("Times", 15), width=30)
    username_entry.pack(pady=10)

    tk.Label(log_in_window, text="Password:", font=("Times", 15), bg="light grey").pack(pady=5)
    password_entry = tk.Entry(log_in_window, font=("Times", 15), width=30, show="*")
    password_entry.pack(pady=10)

    def validate_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if username in user_data and user_data[username] == password:
            messagebox.showinfo("Success", "You have logged in successfully!")
            log_in_window.destroy()  # Close login window
            booking_page(parent, username)  # Open booking page
        else:
            messagebox.showerror("Error", "Please enter a valid username and password")

    tk.Button(
        log_in_window,
        text="Log In",
        command=validate_login,
        font=("Times", 15),
        bg="light green",
        width=15
    ).pack(pady=20)

# Customer window definition
def customer_window(parent):
    customer_window = tk.Toplevel(parent)
    customer_window.title("Customer Page")
    customer_window.configure(bg="light grey")

    tk.Label(customer_window, text="Customer Login and Sign Up", font=("Times", 30), bg="light grey").pack(pady=20)
    tk.Label(customer_window, text="Please register and create an account or log in if you have an existing account", font=("Times", 15), bg="light grey").pack(pady=20)

    button1 = tk.Button(
        customer_window,
        text="Log In",
        command=lambda: log_in_window(customer_window),
        width=15,
        bg="white",
        fg="black",
        font=("Times", 15)
    )
    button1.pack(pady=20)

    button2 = tk.Button(
        customer_window,
        text="Create an Account",
        command=lambda: sign_up_window(customer_window),  # sign_up_window function call here
        width=15,
        bg="white",
        fg="black",
        font=("Times", 15)
    )
    button2.pack(pady=20)

# Booking page definition
def booking_page(parent, username):
    customer_bookings_window = tk.Toplevel(parent)
    customer_bookings_window.title("Customer Bookings")
    customer_bookings_window.configure(bg="light grey")

    tk.Label(customer_bookings_window, text="Welcome to the Customer Booking Page", font=("Times", 30), bg="light grey").pack(pady=20)
    tk.Label(customer_bookings_window, text="Here you can self-book trips", font=("Times", 15), bg="light grey").pack(pady=20)

    tk.Label(customer_bookings_window, text="Pick up location:", font=("Times", 15), bg="light grey").pack(pady=5)
    pickup_location = tk.Entry(customer_bookings_window, font=("Times", 15), width=30, )
    pickup_location.pack(pady=10)

    tk.Label(customer_bookings_window, text="Post code for pick up location:", font=("Times", 15), bg="light grey").pack(pady=5)
    postcode_pickup_location = tk.Entry(customer_bookings_window, font=("Times", 15), width=30, )
    postcode_pickup_location.pack(pady=10)

    tk.Label(customer_bookings_window, text="Drop off location:", font=("Times", 15), bg="light grey").pack(pady=5)
    dropoff_location = tk.Entry(customer_bookings_window, font=("Times", 15), width=30, )
    dropoff_location.pack(pady=10)

    tk.Label(customer_bookings_window, text="Post code for drop off location:", font=("Times", 15), bg="light grey").pack(pady=5)
    postcode_dropoff_location = tk.Entry(customer_bookings_window, font=("Times", 15), width=30, )
    postcode_dropoff_location.pack(pady=10)

    tk.Label(customer_bookings_window, text="Date and time for booking", font=("Times", 15), bg="light grey").pack(pady=5)
    date_and_time = tk.Entry(customer_bookings_window, font=("Times", 15), width=30, )
    date_and_time.pack(pady=10)

    # Add a button to accept data and save the booking
    def save_booking():
        pickup = pickup_location.get().strip()
        pickup_postcode = postcode_pickup_location.get().strip()
        dropoff = dropoff_location.get().strip()
        dropoff_postcode = postcode_dropoff_location.get().strip()
        date_time = date_and_time.get().strip()

        if not pickup or not pickup_postcode or not dropoff or not dropoff_postcode or not date_time:
            messagebox.showerror("Error", "All fields must be filled.")
        else:
            # Store the booking in the customer_bookings list
            customer_id = len(customer_bookings) + 1  # Incremental customer ID
            booking = {
                "ID": customer_id,
                "Pickup": pickup,
                "Pickup Postcode": pickup_postcode,
                "Dropoff": dropoff,
                "Dropoff Postcode": dropoff_postcode,
                "Date & Time": date_time
            }
            customer_bookings.append(booking)
            messagebox.showinfo("Success", "Booking successfully saved!")

            # Clear the form
            pickup_location.delete(0, tk.END)
            postcode_pickup_location.delete(0, tk.END)
            dropoff_location.delete(0, tk.END)
            postcode_dropoff_location.delete(0, tk.END)
            date_and_time.delete(0, tk.END)

            display_bookings()

    tk.Button(
        customer_bookings_window,
        text="Save Booking",
        command=save_booking,
        font=("Times", 15),
        bg="light green",
        width=15
    ).pack(pady=20)

    def display_bookings():
        table_window = tk.Toplevel(customer_bookings_window)
        table_window.title("Booking list for customers")
        table_window.configure(bg="light grey")

        columns = ("ID", "Pickup", "Pickup Postcode", "Dropoff", "Dropoff Postcode", "Date & Time")

        tree = ttk.Treeview(table_window, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor="center")

        # Insert bookings into the table
        for booking in customer_bookings:
            tree.insert("", "end", values=(booking["ID"], booking["Pickup"], booking["Pickup Postcode"], 
                                          booking["Dropoff"], booking["Dropoff Postcode"], booking["Date & Time"]))

        tree.pack(pady=20)

