import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip
def generate_password(length=12, include_uppercase=True, include_digits=True, include_special_chars=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Ensure that at least one character type is included
    if not all_chars:
        raise ValueError("Password must include at least one character type.")

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password
def main():
    print("Password Generator App")
    length = int(input("Enter the length of the password: "))

    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, include_uppercase, include_digits, include_special_chars)
        print("Generated Password:", password)
    except ValueError as ve:
        print("Error:", ve)
def generate_password_button_clicked():
    length = int(length_entry.get())
    include_uppercase = include_uppercase_var.get()
    include_digits = include_digits_var.get()
    include_special_chars = include_special_chars_var.get()

    try:
        password = generate_password(length, include_uppercase, include_digits, include_special_chars)
        password_output.config(text="Generated Password: " + password)

        # Save the generated password to the clipboard
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

# Create the main application window
app = tk.Tk()
app.title("Password Generator App")

# Create and arrange GUI elements
length_label = tk.Label(app, text="Enter the length of the password:")
length_label.pack()

length_entry = tk.Entry(app)
length_entry.pack()

include_uppercase_var = tk.BooleanVar()
include_uppercase_checkbutton = tk.Checkbutton(app, text="Include Uppercase Letters", variable=include_uppercase_var)
include_uppercase_checkbutton.pack()

include_digits_var = tk.BooleanVar()
include_digits_checkbutton = tk.Checkbutton(app, text="Include Digits", variable=include_digits_var)
include_digits_checkbutton.pack()

include_special_chars_var = tk.BooleanVar()
include_special_chars_checkbutton = tk.Checkbutton(app, text="Include Special Characters", variable=include_special_chars_var)
include_special_chars_checkbutton.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_password_button_clicked)
generate_button.pack()

password_output = tk.Label(app, text="")
password_output.pack()

# Start the main event loop
app.mainloop()