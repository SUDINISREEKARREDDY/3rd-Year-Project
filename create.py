import pandas as pd
import numpy as np

def generate_stage_data(stage, num_samples):
    # Define value ranges for each stage
    blood_marker_range = [(0, 20), (10, 40), (30, 70), (50, 100)]
    ctc_range = [(0, 50), (20, 150), (100, 300), (200, 500)]
    exhaled_breath_range = [(0, 2), (1, 4), (3, 7), (5, 10)]
    
    symptom_history_levels = ["Mild", "Moderate", "Severe", "Severe"]
    physical_exam_levels = ["Normal", "Normal", "Abnormal", "Abnormal"]
    urine_test_levels = ["Normal", "Normal", "Abnormal", "Abnormal"]
    bone_scan_levels = ["No Lesions", "Suspicious", "Suspicious", "Confirmed Metastases"]
    endoscopic_levels = ["Normal", "Inflammation", "Tumor Detected", "Tumor Detected"]
    organ_function_levels = ["Normal", "Mild Dysfunction", "Mild Dysfunction", "Severe Dysfunction"]
    
    # Create data dictionary
    data = {
        "Blood Markers (Tumor Markers)": np.random.uniform(*blood_marker_range[stage-1], num_samples),
        "Circulating Tumor Cells (CTCs)": np.random.randint(*ctc_range[stage-1], num_samples),
        "Genetic Testing (Genomic Profiling)": np.random.choice(["Positive", "Negative"], num_samples),
        "Symptom History": np.random.choice([symptom_history_levels[stage-1]], num_samples),
        "Physical Examination": np.random.choice([physical_exam_levels[stage-1]], num_samples),
        "Exhaled Breath Analysis": np.random.uniform(*exhaled_breath_range[stage-1], num_samples),
        "Urine Tests": np.random.choice([urine_test_levels[stage-1]], num_samples),
        "Bone Scans": np.random.choice([bone_scan_levels[stage-1]], num_samples),
        "Endoscopic Examination": np.random.choice([endoscopic_levels[stage-1]], num_samples),
        "Organ Function Tests (Liver, Kidney, etc.)": np.random.choice([organ_function_levels[stage-1]], num_samples),
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    filename = f"stage{stage}.csv"
    df.to_csv(filename, index=False)
    print(f"Dataset '{filename}' has been created successfully!")

# Generate datasets for each stage
for stage in range(1, 5):
    generate_stage_data(stage, num_samples=100)
