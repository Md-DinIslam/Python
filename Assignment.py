import pandas as pd

# ---------------------------
# 1. Load & Clean Data
# ---------------------------
file_path = "Class_Attendance_CSE 315-CSE(201)(221_D1)-Artificial Intelligence.xlsx"
data = pd.read_excel(file_path)

# Remove 'Unnamed' columns
clean_cols = [c for c in data.columns if not c.startswith("Unnamed")]
data = data[clean_cols]

# Attendance columns start after first three columns
att_cols = clean_cols[3:]

# ---------------------------
# 2. Count Present / Absent
# ---------------------------
data["Total_Present"] = data[att_cols].apply(lambda row: (row == "P").sum(), axis=1)
data["Total_Absent"]  = data[att_cols].apply(lambda row: (row == "A").sum(), axis=1)

# Total class count is same for everyone
data["Classes_Taken"] = len(att_cols)

# Remove header mis-read row
data = data.iloc[1:].copy()

# ---------------------------
# 3. Percentage & Marks
# ---------------------------
data["Attendance_Percent"] = (data["Total_Present"] / data["Classes_Taken"]) * 100
data["Attendance_Percent"] = data["Attendance_Percent"].astype(int)

# Convert ID columns to proper integer type
data["SL"] = data["SL"].astype(int)
data["Student's ID"] = data["Student's ID"].astype(int)

# Marks calculation function
def assign_marks(percent):
    if percent >= 70:
        return 5
    if percent >= 60:
        return 4
    if percent >= 45:
        return 3
    return 2

data["Marks"] = data["Attendance_Percent"].apply(assign_marks)

# ---------------------------
# 4. Summary Report
# ---------------------------
range_70 = (data["Attendance_Percent"] >= 70).sum()
range_60 = data["Attendance_Percent"].between(60, 69).sum()
range_45 = data["Attendance_Percent"].between(45, 59).sum()
range_30 = data["Attendance_Percent"].between(30, 44).sum()

summary = pd.DataFrame({
    "SL": [1, 2, 3, 4],
    "Range": ["70% & above", "60% - 69%", "45% - 59%", "30% - 44%"],
    "Total_Students": [range_70, range_60, range_45, range_30]
})

# ---------------------------
# 5. Output
# ---------------------------
print(data[["SL", "Student's Name", "Student's ID", "Attendance_Percent", "Marks"]])
print(summary)
