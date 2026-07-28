from pathlib import Path
missing_students = []
file_path = Path(__file__).with_name("students.csv")
with open(file_path) as file:
    next(file)
    for line in file:
        fields = line.strip().split(",")
        name = fields[0]
        score = fields[2]
        if score == "":
            print(f"Missing score: {name}")
            missing_students.append(name)
print(missing_students)
print(f"Students with missing scores: {len(missing_students)}")