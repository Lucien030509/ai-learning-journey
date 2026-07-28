import pandas as pd
data = {
    "name": ["Estella", "Alex", "Mia"],
    "course": ["COMP9001", "COMP9120", "COMP5310"],
    "scores": [85, 92, 78]
}
students = pd.DataFrame(data)
print(students)
print(students["scores"])
print(students["scores"].mean())
high_score_students = students[students["scores"] >= 85]
print(high_score_students)
students["passed"] = students["scores"] >= 80
print(students)