profile = {"name": "Lucien", "university": "USYD", "program": "Master of AI"}
print(profile["program"])
profile["current_focus"]= "SQL"
print(profile["current_focus"])
for key in profile:
    print(f"{key}: {profile[key]}")