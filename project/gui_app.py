import tkinter as tk
from tkinter import messagebox
from models import *

users_list = []

# Create a test user and add to users_list
new_user = Customer(
    username="johncustomer", 
    name="John Customer", 
    password="password123", 
    email="john@gmail.com", 
    physical_address="123 Main St"
)
users_list.append(new_user)

# Define basic Tkinter window
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("User Login")
        
        # Create the login frame
        self.login_frame = tk.Frame(root)
        self.login_frame.pack(padx=20, pady=20)

        # Create and place the welcome label
        label = tk.Label(self.login_frame, text="Welcome to Kinsey's Store!")
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        # Creating
        # a label for username
        tk.Label(self.login_frame, text="Username:").grid(row=1, column=0, padx=10, pady=5)
        # Create a label for password
        tk.Label(self.login_frame, text="Password:").grid(row=2, column=0, padx=10, pady=5)

        # Create entry fields for username and password
        self.username_entry = tk.Entry(self.login_frame)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        # Create a login button
        login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Print entered username and password for debugging
        print(f"Entered Username: {username}")
        print(f"Entered Password: {password}")

        # Check if the user exists in users_list
        user = next((u for u in users_list if u.username == username), None)
        if user:
            # Print stored hashed password for debugging
            print(f"Stored Hashed Password: {user.password}")
            # Print hashed entered password for comparison
            print(f"Hashed Entered Password: {user._hash_password(password)}")

        if user and user.login(password):
            messagebox.showinfo("Login Successful", f"Welcome, {user.name}!")
            self.show_new_screen()  # Call the function to show the new screen
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!")

    def show_new_screen(self):
        # Remove the login frame
        self.login_frame.pack_forget()

        # Create a new frame for the new screen
        new_frame = tk.Frame(self.root)
        new_frame.pack(padx=20, pady=20)

        # Add content to the new screen
        tk.Label(new_frame, text="Welcome to the dashboard!").pack(pady=10)
        tk.Button(new_frame, text="Logout", command=lambda: self.logout(new_frame)).pack(pady=10)

    def logout(self, frame):
        # Remove the current frame
        frame.pack_forget()

        # Show the login frame again
        self.login_frame.pack(padx=20, pady=20)

# Initialize Tkinter and run the GUI
root = tk.Tk()
app = App(root)
root.mainloop()
