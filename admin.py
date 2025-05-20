import tkinter as tk
from tkinter import messagebox

# Temporary user data storage
admin_data = {}
driver_data = {}

# Log-in window definition
def log_in_window(parent, user_type):
    log_in_window = tk.Toplevel(parent)
    log_in_window.title(f"{user_type.capitalize()} Log In")
    log_in_window.configure(bg="light grey")

    tk.Label(log_in_window, text="Welcome, please log in to get started", font=("Times", 20), bg="light grey").pack(pady=20)

    tk.Label(log_in_window, text="Username:", font=("Times", 15), bg="light grey").pack(pady=5)
    username_entry = tk.Entry(log_in_window, font=("Times", 15), width=30)
    username_entry.pack(pady=10)

    tk.Label(log_in_window, text="Password:", font=("Times", 15), bg="light grey").pack(pady=5)
    password_entry = tk.Entry(log_in_window, font=("Times", 15), width=30, show="*")
    password_entry.pack(pady=10)

    def validate_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        data = admin_data if user_type == "admin" else driver_data

        if username in data and data[username] == password:
            messagebox.showinfo("Success", f"{user_type.capitalize()} logged in successfully!")
            log_in_window.destroy()  # Close login window
            booking_page(parent, user_type)  # Open the booking page
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
def sign_up_window(parent, user_type):
    sign_up_window = tk.Toplevel(parent)
    sign_up_window.title(f"{user_type.capitalize()} Create an Account")
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
        data = admin_data if user_type == "admin" else driver_data

        if not username or not password:
            messagebox.showerror("All fields must be completed")
        elif username == password:
            messagebox.showerror("Error", "Password cannot be the same as Username.")
        elif username in data:
            messagebox.showerror("Error", "Username already exists.")
        else:
            data[username] = password
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

# Booking page definition
def booking_page(parent, user_type):
    booking_window = tk.Toplevel(parent)
    booking_window.title(f"{user_type.capitalize()} Booking Page")
    booking_window.configure(bg="light grey")

    tk.Label(booking_window, text=f"Welcome to the {user_type.capitalize()} Booking Page", font=("Times", 30), bg="light grey").pack(pady=20)

    if user_type == "admin":
        tk.Label(booking_window, text="Manage users bookings and assign driver bookings.", font=("Times", 15), bg="light grey").pack(pady=20)
        tk.Button(
            booking_window,
            text="Manage Users",
            font=("Times", 15),
            bg="light blue",
            command=lambda: messagebox.showinfo("Manage bookings", "manage bookings coming soon!"),
            width=15
        ).pack(pady=20)
    elif user_type == "driver":

        tk.Label(booking_window, text="Manage your bookings or services.", font=("Times", 15), bg="light grey").pack(pady=20)
        tk.Button(
            booking_window,
            text="Manage Bookings",
            font=("Times", 15),
            bg="light blue",
            command=lambda: messagebox.showinfo("Manage Bookings", "Booking management functionality coming soon!"),
            width=15
        ).pack(pady=20)

# Admin window definition
def admin_window(parent):
    admin_window = tk.Toplevel(parent)
    admin_window.title("Admin Page")
    admin_window.configure(bg="light grey")

    tk.Label(admin_window, text="Admin Login and Sign Up", font=("Times", 30), bg="light grey").pack(pady=20)
    tk.Label(admin_window, text="Register or log in to get access.", font=("Times", 15), bg="light grey").pack(pady=20)

    tk.Button(
        admin_window,
        text="Log In",
        command=lambda: log_in_window(admin_window, "admin"),
        width=15,
        bg="white",
        fg="black",
        font=("Times", 15)
    ).pack(pady=20)

    tk.Button(
        admin_window,
        text="Create an Account",
        command=lambda: sign_up_window(admin_window, "admin"),
        width=15,
        bg="white",
        fg="black",
        font=("Times", 15)
    ).pack(pady=20)

# Driver window definition
def driver_window(parent):
    driver_window = tk.Toplevel(parent)
    driver_window.title("Driver Page")
    driver_window.configure(bg="light grey")

    tk.Label(driver_window, text="Driver Login and Sign Up", font=("Times", 30), bg="light grey").pack(pady=20)
    tk.Label(driver_window, text="Register or log in to manage your bookings.", font=("Times", 15), bg="light grey").pack(pady=20)

    tk.Button(
        driver_window,
        text="Log In",
        command=lambda: log_in_window(driver_window, "driver"),
        width=15,
        bg="white",
        fg="black",
        font=("Times", 15)
    ).pack(pady=20)

    tk.Button(
        driver_window,
        text="Create an Account",
        command=lambda: sign_up_window(driver_window, "driver"),
        width=15,
        bg="white",
        fg="black",
        font=("Times", 15)
    ).pack(pady=20)

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Admin and Driver System")

    tk.Label(root, text="Welcome to the System", font=("Times", 30), bg="light grey").pack(pady=20)
    tk.Button(root, text="Admin", command=lambda: admin_window(root), width=20, font=("Times", 15)).pack(pady=10)
    tk.Button(root, text="Driver", command=lambda: driver_window(root), width=20, font=("Times", 15)).pack(pady=10)

    root.mainloop()
