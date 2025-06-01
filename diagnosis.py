import pandas as pd
import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt

# Function to generate treatment recommendation
def generate_treatment():
    try:
        tumor_size = float(entry_tumor_size.get())  # Convert to float
        metastasis = var_metastasis.get()

        if metastasis == "Select":
            messagebox.showerror("Error", "Please select Metastasis Involvement (Yes or No).")
            return

        # Assign radiation & chemotherapy based on metastasis involvement
        if metastasis == "No":
            radiation = random.randint(25, 30)
            chemotherapy = "Not Required"
        else:  # Metastasis is Yes
            radiation = random.randint(20, 25)
            chemotherapy = random.randint(20, 30)

        # Display results
        treatment_message = f"Recommended Radiation Therapy: {radiation} units"
        if chemotherapy != "Not Required":
            treatment_message += f"\nRecommended Chemotherapy: {chemotherapy} units"

        messagebox.showinfo("Treatment Plan", treatment_message)

        # Save to CSV
        df = pd.DataFrame([[tumor_size, metastasis, radiation, chemotherapy]],
                          columns=["Tumor Size (cm)", "Metastasis", "Radiation (Units)", "Chemotherapy (Units)"])
        df.to_csv("treatment_plan.csv", mode='a', header=False, index=False)

        # Generate graph
        generate_graph(tumor_size, metastasis)

        # Clear input fields
        entry_tumor_size.delete(0, tk.END)
        var_metastasis.set("Select")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric value for Tumor Size.")

# Function to generate a tumor size vs. threshold graph
def generate_graph(tumor_size, metastasis):
    user_value = [tumor_size]
    threshold = [5]  # Example threshold for risk assessment

    labels = ["Tumor Size (cm)"]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, user_value, color='blue', label="Patient's Tumor Size")
    plt.bar(labels, threshold, color='red', alpha=0.5, label="Risk Threshold")

    plt.xlabel("Attributes")
    plt.ylabel("Size (cm)")
    plt.title(f"Tumor Size Analysis ({'Metastasis' if metastasis == 'Yes' else 'No Metastasis'})")
    plt.legend()
    plt.show()

# Initialize Tkinter window
root = tk.Tk()
root.title("Cancer Treatment Diagnosis")
root.geometry("400x350")
root.configure(bg="#f5f5f5")  # Light Gray Background

# UI Labels and Inputs
tk.Label(root, text="Enter Tumor Size (cm)", bg="#f5f5f5").pack()
entry_tumor_size = tk.Entry(root)
entry_tumor_size.pack()

# Metastasis Dropdown
tk.Label(root, text="Metastasis Involvement", bg="#f5f5f5").pack()
var_metastasis = tk.StringVar(value="Select")
dropdown_metastasis = tk.OptionMenu(root, var_metastasis, "Yes", "No")
dropdown_metastasis.pack()

# Submit Button
submit_btn = tk.Button(root, text="Get Treatment Plan", command=generate_treatment, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
submit_btn.pack(pady=20)

# Run the application
root.mainloop()