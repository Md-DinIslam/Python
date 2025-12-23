import pandas as pd

df = pd.read_excel("Class_Attendance_CSE 315-CSE(201)(221_D1)-Artificial Intelligence.xlsx")

# print(df)
df = df.drop(columns=[col for col in df.columns if 'Unnamed' in col])

attendance_columns = df.columns[3:]

df['Present'] = (df[attendance_columns] == 'P').sum(axis = 1)
df['Absence'] = (df[attendance_columns] == 'A').sum(axis = 1)

total_days = attendance_columns.size
df["Total_Classes"] = total_days

df = df.drop(df.index[0])

# print(df[['SL' ,'Student\'s ID', 'Student\'s Name', 'Present', 'Absence', 'Total_Classes']])

df['Percentage'] = (df['Present'] / df['Total_Classes']) * 100
df['Percentage'] = df['Percentage'].astype('int64')
df["Student's ID"] = df["Student's ID"].astype('int64')
df["SL"] = df["SL"].astype('int64')

def getMark(p):
        if p >= 70:
                return 5
        elif p >= 60:
                return 4
        elif p >= 45:
                return 3
        else:
                return 2
        
df['Marks'] = df['Percentage'].apply(getMark)

c_70 = (df['Percentage'] >= 70).sum()
c_60 = ((df['Percentage'] >= 60) & (df['Percentage'] < 70)).sum()
c_45 = ((df['Percentage'] >= 45) & (df['Percentage'] < 60)).sum()
c_30 = ((df['Percentage'] >= 30) & (df['Percentage'] < 45)).sum()

report = pd.DataFrame ({
        "SL" : [1, 2, 3, 4],
        'Percentage' : ['70%', '60%', '45%', '30%'],
        'Count' : [c_70, c_60, c_45, c_30]
})

df['Percentage'] = df['Percentage'].astype('int64').astype(str) + "%"

print("\n       ---- Calculate Attendance Percentage ----\n")
print(df[['SL' ,"Student's Name", "Student's ID", 'Percentage', 'Marks']])

print("\n       ---- Attendance Percentage (Student Count) ----\n")

print(report)

