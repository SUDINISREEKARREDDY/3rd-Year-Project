import tkinter as tk
import subprocess

def cancer_prediction():
    subprocess.Popen(["python", "predict.py"])

def cancer_diagnosis():
    subprocess.Popen(["python", "diagnosis.py"])

# Create main window
root = tk.Tk()
root.title("Cancer Detection System")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Welcome to Cancer Detection System", font=("Arial", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

# Buttons
predict_button = tk.Button(root, text="Cancer Prediction", font=("Arial", 12), command=cancer_prediction, width=20, height=2, bg="#4CAF50", fg="white")
predict_button.pack(pady=10)

diagnosis_button = tk.Button(root, text="Cancer Diagnosis", font=("Arial", 12), command=cancer_diagnosis, width=20, height=2, bg="#2196F3", fg="white")
diagnosis_button.pack(pady=10)

# Run the application
root.mainloop()
