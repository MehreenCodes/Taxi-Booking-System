import tkinter as tk
from tkinter import messagebox

# Temporary user data storage for drivers
driver_data = {}

# Log-in window definition
def log_in_window(parent):
    log_in_window = tk.Toplevel(parent)
    log_in_window.title("Driver Log In")
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

        if username in driver_data and driver_data[username] == password:
            messagebox.showinfo("Success", "You have logged in successfully!")
            log_in_window.destroy()  # Close login window
            booking_page(parent)  # Open booking page
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    tk.Button(
        log_in_window,
        text="Log In",
        command=validate_login,
        font=("Times", 15),
        bg="light green",
        width=15
    ).pack(pady=20)

# Sign-up window definition
def sign_up_window(parent):
    sign_up_window = tk.Toplevel(parent)
    sign_up_window.title("Driver Create an Account")
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
            messagebox.showerror("Error", "All fields must be filled.")
        elif username == password:
            messagebox.showerror("Error", "Password cannot be the same as Username.")
        elif username in driver_data:
            messagebox.showerror("Error", "Username already exists.")
        else:
            driver_data[username] = password
            messagebox.showinfo("Success", "Account created successfully!")
            sign_up_window.destroy()

    tk.Button(
        sign_up_window,
        text="Sign Up",
        command=register_user,
        font=("Times", 15),
        bg="light blue",
        width=15
    ).pack(pady=20)

# Driver window definition
def driver_window(parent):
    driver_window = tk.Toplevel(parent)
    driver_window.title("Driver Page")
    driver_window.configure(bg="light grey")

    tk.Label(driver_window, text="Driver Login and Sign Up", font=("Times", 30), bg="light grey").pack(pady=20)
    tk.Label(driver_window, text="Please register and create an account or login if you have an existing account", font=("Times", 15), bg="light grey").pack(pady=20)

    button1 = tk.Button(
        driver_window,
        text="Log In",
        command=lambda: log_in_window(driver_window),  # Open log-in window
        width=15,
        bg="white",
        fg="black",
        font=("Times", 15)
    )
    button1.pack(pady=20)

    button2 = tk.Button(
        driver_window,
        text="Create an Account",
        command=lambda: sign_up_window(driver_window),  # Open sign-up window
        width=15,
        bg="white",
        fg="black",
        font=("Times", 15)
    )
    button2.pack(pady=20)

# Booking page definition
def booking_page(parent):
    booking_window = tk.Toplevel(parent)
    booking_window.title("Driver Booking Page")
    booking_window.configure(bg="light grey")

    tk.Label(booking_window, text="Welcome to the Driver Booking Page", font=("Times", 30), bg="light grey").pack(pady=20)
    tk.Label(booking_window, text="Here you can manage your bookings services by accepting customer bookings", font=("Times", 15), bg="light grey").pack(pady=20)

    tk.Button(
        booking_window,
        text="Manage Bookings",
        font=("Times", 15),
        bg="light blue",
        command=lambda: messagebox.showinfo("Manage Bookings", "Booking management is coming soon!"),
        width=15
    ).pack(pady=20)
