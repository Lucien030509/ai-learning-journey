class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def describe(self):
        print(f"Course: {self.name}, Code: {self.code}")
course1 = Course("Programming Fundamentals", "COMP9001")
course1.describe()