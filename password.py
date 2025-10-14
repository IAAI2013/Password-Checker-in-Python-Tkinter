import tkinter as tk
from tkinter import StringVar

def check_strength(password):
    length = len(password)
    if length == 0:
        return "Enter a password"
    elif length < 6:
        return "Weak"
    elif length < 10:
        return "Moderate"
    else:
        return "Strong"

def on_key_release(event=None):
    pwd = password_var.get()
    strength = check_strength(pwd)
    strength_var.set(f"Strength: {strength}")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x150")

password_var = StringVar()
strength_var = StringVar(value="Strength: ")

tk.Label(root, text="Enter Password:").pack(pady=10)
pwd_entry = tk.Entry(root, textvariable=password_var, show="*")
pwd_entry.pack()
pwd_entry.bind("<KeyRelease>", on_key_release)

tk.Label(root, textvariable=strength_var, font=("Arial", 12)).pack(pady=20)

root.mainloop()