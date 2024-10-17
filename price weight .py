import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

# Function to perform the calculations
def calculate():
    try:
        price_per_kg = float(price_per_kg_entry.get())  # Price per kilogram
        input_value = float(input_entry.get())  # The user input (price or weight)
        price_per_gram = price_per_kg / 1000  # Price per gram

        # Display variables
        result_text = ""
        item_name = item_name_entry.get()

        # Case 1: Input interpreted as weight in grams
        cost_for_grams = input_value * price_per_gram
        result_text += f"{input_value:.2f} grams = {cost_for_grams:.2f} ₨.\n"

        # Case 2: Input interpreted as price in rupees (what it can buy in grams)
        if input_value >= price_per_gram:
            grams_can_buy = input_value / price_per_gram
            result_text += f"{input_value:.2f} ₨ = {grams_can_buy:.2f} grams.\n"

        # Case 3: Input interpreted as weight in kilograms
        kilograms = input_value / 1000
        kilogram_cost = input_value * price_per_kg
        result_text += f"{input_value:.2f} kilograms = {kilogram_cost:.2f} ₨."

        # Add item name if provided
        if item_name:
            result_text = f"Item: {item_name}\n" + result_text

        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for price and weight.")

import datetime  # Import datetime module for current date

# Function to save purchase details to a .txt file
def save_purchase_details():
    item_name = item_name_entry.get() or "Purchase_Details"  # Default to "Purchase_Details" if no item name is provided
    details = result_label.cget("text")
    
    if not details:
        messagebox.showerror("Error", "No details to save. Please calculate first.")
        return
    
    # Get the current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Create a default file name using the item name and current date
    default_file_name = f"{item_name}_{current_date}.txt"
    
    # Ask the user where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             initialfile=default_file_name,
                                             filetypes=[("Text files", "*.txt")], 
                                             title="Save Purchase Details")
    if file_path:
        try:
            # Append a footer to the details
            footer = "\n\nSoftware developed by imsubhu."
            details_with_footer = details + footer
            
            # Save file with UTF-8 encoding to support special characters
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(details_with_footer)
            
            messagebox.showinfo("Saved", f"Details saved at {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save the file: {e}")


# Function to clear inputs and results
def clear():
    price_per_kg_entry.delete(0, tk.END)
    input_entry.delete(0, tk.END)
    item_name_entry.delete(0, tk.END)
    result_label.config(text="")

# Function to show about info
def show_about():
    messagebox.showinfo("About", "Weight Price Calculator\nDeveloped by: imsubhu")

# Create the main application window
root = tk.Tk()
root.title("Weight Price Calculator")
root.geometry("400x550")
root.config(bg="#2c3e50")

# Create a menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add "About" to the menu
menu_bar.add_command(label="About", command=show_about)

# Title label with modern font and design
title_label = tk.Label(root, text="Weight Price Calculator", font=("Arial", 18, "bold"), bg="#e67e22", fg="white", pady=10)
title_label.pack(fill=tk.X)

# Input for price per KG with modern styling
tk.Label(root, text="Enter Price per KG (₨):", bg="#2c3e50", fg="white", font=("Arial", 12)).pack(pady=5)
price_per_kg_entry = ttk.Entry(root, font=("Arial", 12))
price_per_kg_entry.pack(pady=5, padx=20, fill=tk.X)

# Input for price or weight
tk.Label(root, text="Enter Price or Weight:", bg="#2c3e50", fg="white", font=("Arial", 12)).pack(pady=5)
input_entry = ttk.Entry(root, font=("Arial", 12))
input_entry.pack(pady=5, padx=20, fill=tk.X)

# Input for optional item name
tk.Label(root, text="Item Name (Optional):", bg="#2c3e50", fg="white", font=("Arial", 12)).pack(pady=5)
item_name_entry = ttk.Entry(root, font=("Arial", 12))
item_name_entry.pack(pady=5, padx=20, fill=tk.X)

# Buttons with a modern style
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=10)

calculate_button = ttk.Button(button_frame, text="CALCULATE", command=calculate)
calculate_button.grid(row=0, column=0, padx=10, ipadx=10)

clear_button = ttk.Button(button_frame, text="CLEAR", command=clear)
clear_button.grid(row=0, column=1, padx=10, ipadx=10)

# Result label with modern design
result_label = tk.Label(root, text="", justify=tk.LEFT, bg="#34495e", fg="white", font=("Arial", 12), padx=10, pady=10)
result_label.pack(pady=10, padx=20, fill=tk.X)

# Purchase detail button with a modern look
purchase_button = ttk.Button(root, text="SAVE PURCHASE DETAIL", command=save_purchase_details)
purchase_button.pack(pady=20, ipadx=20, ipady=5)

# Start the application
root.mainloop()
