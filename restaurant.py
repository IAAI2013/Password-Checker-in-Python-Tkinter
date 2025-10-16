import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantApp:
    def __init__ (self,root):
        self.root = root
        self.root.title("Restaurant Management System")

        self.menu_items = {
            "FRIES": 2,
            "LUNCH PACKAGE": 5,
            "BURGER PACKAGE": 5,
            "PIZZA PACKAGE": 8,
            "CHICKEN PACKAGE": 7,
            "DRINKS": 1
        }

        self.exchange_rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.75,
            "CNY": 6.5,
            "INR": 74.0,
            "LKR": 200.0
        }

        self.setup_bg(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame,
                  text="Restaurant Management System",
                  font=("Arial", 20, "bold")).grid(row=0, columnspan=2, pady=10)
        
        self.menu_labels = {}
        self.menu_quanties = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame,
                              text=f"{item} (${price})",
                              font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        self.currency_var = tk.StringVar()
        ttk.Label(frame, text="Select Currency:", font=("Arial", 12)).grid(row=len(self.menu_items) + 1, column=0, padx=10, pady=5)

        currency_dropdown = ttk.Combobox(frame, textvariable=self.currency_var, state="readonly", width=18, values=("USD", "EUR", "GBP", "CNY", "INR", "LKR"))
        currency_dropdown.current(0)

        self.currency_var.trace("w", self.update_menu_prices)

        order_button = ttk.Button(frame, text="Place Order", command=self.place_order)
        order_button.grid(row=len(self.menu_items) + 2, columnspan=3, padx=10, pady=10)

        def setup_bg(self, root):
            bg_width, bg_height = 800, 600
            canvas = tk.Canvas(root, width=bg_width, height=bg_height)
            canvas.pack()
            original_image = tk.PhotoImage(file="Background.webp")
            background_image = original_image.subsample(original_image.width() // bg_width, original_image.height() // bg_height)
            canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
            canvas.image= background_image

        def update_menu_prices(self, *args):
            currency = self.currency_var.get()
            symbol = {"USD": "$", "EUR": "€", "GBP": "£", "CNY": "¥", "INR": "₹", "LKR": "Rs."}
            rate = self.exchange_rates[currency]
            for item, price in self.menu_items.items():
                converted_price = price * rate
                self.menu_labels[item].config(text=f"{item} ({symbol[currency]}{converted_price:.2f})")

        def place_order(self):