import tkinter as tk
from tkinter import messagebox

# Logic for Calculation
def calculate_expense():
    try:
        # Get inputs from text boxes and convert them to floats
        appliance_name = appliance_entry.get().strip()
        watts = float(watts_entry.get())
        hours = float(hours_entry.get())
        rate = float(rate_entry.get())
        
        # Validation checks
        if not appliance_name:
            messagebox.showerror("Input Error", "Please enter an appliance name.")
            return
        if hours > 24 or hours < 0:
            messagebox.showerror("Input Error", "Hours used per day must be between 0 and 24.")
            return
        if watts < 0 or rate < 0:
            messagebox.showerror("Input Error", "Watts and Rate must be positive numbers.")
            return

        # Math calculations
        daily_kwh = (watts / 1000) * hours
        monthly_kwh = daily_kwh * 30
        monthly_cost = monthly_kwh * rate

        # Update the results on the UI
        result_label.config(
            text=f"Results for '{appliance_name}':\n\n"
                 f"Daily Consumption: {daily_kwh:.2f} kWh\n"
                 f"Monthly Consumption: {monthly_kwh:.2f} kWh\n"
                 f"Estimated Monthly Cost: ₹{monthly_cost:.2f}",
            fg="#10B981"  # Changes text color to green on success
        )
        
    except ValueError:
        # Catches cases where user types letters instead of numbers
        messagebox.showerror("Input Error", "Please enter valid numbers for Watts, Hours, and Rate.")

# User Interface
root = tk.Tk()
root.title("Home Energy & Expense Simulator")
root.geometry("500x600")
root.configure(bg="#00BFFF") 

# Banner Title
title_label = tk.Label(root, text="⚡ Energy & Expense Simulator", font=("Helvetica", 16, "bold"), bg="#1F2937", fg="white", pady=10)
title_label.pack(fill=tk.X)

# Form Container Frame
frame = tk.Frame(root, bg="#C3EB0D", padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

# Grid Layout configuration 
labels = ["Appliance Name (e.g., AC, Fridge):", "Power Rating (Watts):", "Hours Used Per Day:", "Electricity Rate (per kWh/Unit):"]
entries = []

for i, text in enumerate(labels):
    lbl = tk.Label(frame, text=text, font=("Helvetica", 10, "bold"), bg="#F3F4F6", fg="#374151")
    lbl.grid(row=i*2, column=0, sticky="w", pady=(10, 2))
    
    entry = tk.Entry(frame, font=("Helvetica", 11), bd=2, relief="groove")
    entry.grid(row=i*2+1, column=0, sticky="we", pady=(0, 10))
    entries.append(entry)

# I have assigned entry variables for easy access in logic
appliance_entry, watts_entry, hours_entry, rate_entry = entries

# I have set a default value for electricity rate to make it user-friendly
rate_entry.insert(0, "7.0")

# Calculate Button
calculate_btn = tk.Button(frame, text="Calculate Cost", font=("Helvetica", 12, "bold"), bg="#3B82F6", fg="white", bd=0, cursor="hand2", command=calculate_expense, pady=5)
calculate_btn.grid(row=8, column=0, pady=15)

# Results Display Area
result_label = tk.Label(frame, text="Enter appliance details above\nto calculate estimated monthly costs.", font=("Helvetica", 11, "italic"), bg="#E5E7EB", fg="#4B5563", borderwidth=1, relief="solid", padx=15, pady=15, justify="left")
result_label.grid(row=9, column=0,pady=10)

root.mainloop()