from pathlib import Path
import pandas as pd

file_path = Path(__file__).with_name("messy_students.csv")
students = pd.read_csv(file_path)
print(students)
students["score"] = pd.to_numeric(students["score"], errors="coerce")
print(students.dtypes)
print(students)
print(students.isna().sum())
print(students.duplicated().sum())
students = students.drop_duplicates()
students = students.reset_index(drop=True)
students = students.dropna(subset=["score"]).reset_index(drop=True)
print(students)
clean_file_path = Path(__file__).with_name("clean_students.csv")
students.to_csv(clean_file_path, index=False)
print("Clean data saved")
print(f"Average score: {students['score'].mean()}")