from pathlib import Path
import pandas as pd

file_path = Path(__file__).with_name("course_results.csv")
results = pd.read_csv(file_path)
print(results["score"].describe())

results["score"]
print(results.isna().sum())
print(results["score"].mean())
print(results["score"])