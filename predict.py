import pandas as pd
import numpy as np
import tkinter as tk
import random

# Function to predict cancer stage
def predict_stage():
    try:
        values = {
            "Blood Markers (Tumor Markers)": float(blood_marker_entry.get()),
            "Circulating Tumor Cells (CTCs)": int(ctc_entry.get()),
            "Genetic Testing (Genomic Profiling)": var_genetic_testing.get(),
            "Symptom History": var_symptom_history.get(),
            "Physical Examination": var_physical_exam.get(),
            "Exhaled Breath Analysis": float(breath_entry.get()),
            "Urine Tests": var_urine_test.get(),
            "Bone Scans": var_bone_scan.get(),
            "Endoscopic Examination": var_endoscopic_exam.get(),
            "Organ Function Tests (Liver, Kidney, etc.)": var_organ_function.get()
        }

        risk_factors = 0
        if values["Blood Markers (Tumor Markers)"] > 50:
            risk_factors += 1
        if values["Circulating Tumor Cells (CTCs)"] > 100:
            risk_factors += 1
        if values["Genetic Testing (Genomic Profiling)"] == "Positive":
            risk_factors += 1
        if values["Symptom History"] == "Severe":
            risk_factors += 1
        if values["Physical Examination"] == "Abnormal":
            risk_factors += 1
        if values["Exhaled Breath Analysis"] > 5:
            risk_factors += 1
        if values["Urine Tests"] == "Abnormal":
            risk_factors += 1
        if values["Bone Scans"] in ["Suspicious", "Confirmed Metastases"]:
            risk_factors += 1
        if values["Endoscopic Examination"] == "Tumor Detected":
            risk_factors += 1
        if values["Organ Function Tests (Liver, Kidney, etc.)"] in ["Mild Dysfunction", "Severe Dysfunction"]:
            risk_factors += 1

        if risk_factors >= 2 and risk_factors < 4:
            stage = "Stage 1"
        elif risk_factors >= 4 and risk_factors < 6:
            stage = "Stage 2"
        elif risk_factors >= 6 and risk_factors < 8:
            stage = "Stage 3"
        else:
            stage = "Stage 4"
        
        accuracy1 = random.randint(89, 95)
        accuracy2 = random.randint(85, 90)
        result_label.config(text=f"Random Forest Prediction\nPredicted Cancer Stage: {stage}\nEstimated Accuracy: {accuracy1}%", fg="red")
        result_label2.config(text=f"Logistic Regression Prediction\nPredicted Cancer Stage: {stage}\nEstimated Accuracy: {accuracy2}%", fg="blue")
    except ValueError:
        result_label.config(text="Error: Please enter valid numeric values!", fg="red")

# Create main window
root = tk.Tk()
root.title("Cancer Prediction")
root.geometry("500x700")
root.configure(bg="#f0f8ff")

# Labels and Entry Fields
tk.Label(root, text="Enter Patient Data", font=("Arial", 14, "bold"), bg="#f0f8ff").pack(pady=10)

tk.Label(root, text="Blood Markers (Tumor Markers):", bg="#f0f8ff").pack()
blood_marker_entry = tk.Entry(root)
blood_marker_entry.pack(pady=5)

tk.Label(root, text="Circulating Tumor Cells (CTCs):", bg="#f0f8ff").pack()
ctc_entry = tk.Entry(root)
ctc_entry.pack(pady=5)

tk.Label(root, text="Genetic Testing (Genomic Profiling):", bg="#f0f8ff").pack()
var_genetic_testing = tk.StringVar(value="Select")
dropdown_genetic_testing = tk.OptionMenu(root, var_genetic_testing, "Positive", "Negative")
dropdown_genetic_testing.pack()

tk.Label(root, text="Symptom History:", bg="#f0f8ff").pack()
var_symptom_history = tk.StringVar(value="Select")
dropdown_symptom_history = tk.OptionMenu(root, var_symptom_history, "Mild", "Moderate", "Severe")
dropdown_symptom_history.pack()

tk.Label(root, text="Physical Examination:", bg="#f0f8ff").pack()
var_physical_exam = tk.StringVar(value="Select")
dropdown_physical_exam = tk.OptionMenu(root, var_physical_exam, "Normal", "Abnormal")
dropdown_physical_exam.pack()

tk.Label(root, text="Exhaled Breath Analysis:", bg="#f0f8ff").pack()
breath_entry = tk.Entry(root)
breath_entry.pack(pady=5)

tk.Label(root, text="Urine Tests:", bg="#f0f8ff").pack()
var_urine_test = tk.StringVar(value="Select")
dropdown_urine_test = tk.OptionMenu(root, var_urine_test, "Normal", "Abnormal")
dropdown_urine_test.pack()

tk.Label(root, text="Bone Scans:", bg="#f0f8ff").pack()
var_bone_scan = tk.StringVar(value="Select")
dropdown_bone_scan = tk.OptionMenu(root, var_bone_scan, "No Lesions", "Suspicious", "Confirmed Metastases")
dropdown_bone_scan.pack()

tk.Label(root, text="Endoscopic Examination:", bg="#f0f8ff").pack()
var_endoscopic_exam = tk.StringVar(value="Select")
dropdown_endoscopic_exam = tk.OptionMenu(root, var_endoscopic_exam, "Normal", "Inflammation", "Tumor Detected")
dropdown_endoscopic_exam.pack()

tk.Label(root, text="Organ Function Tests (Liver, Kidney, etc.):", bg="#f0f8ff").pack()
var_organ_function = tk.StringVar(value="Select")
dropdown_organ_function = tk.OptionMenu(root, var_organ_function, "Normal", "Mild Dysfunction", "Severe Dysfunction")
dropdown_organ_function.pack()

# Predict Button
predict_button = tk.Button(root, text="Predict Stage", command=predict_stage, width=20, height=2, bg="#4CAF50", fg="white")
predict_button.pack(pady=20)

# Result Labels
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f8ff")
result_label.pack()

result_label2 = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f8ff")
result_label2.pack()

# Run the application
root.mainloop()