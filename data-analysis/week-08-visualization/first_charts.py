from pathlib import Path
import matplotlib.pyplot as plt
courses = ["COMP9001", "COMP9120", "COMP5310"]
average_scores = [85, 92, 78]
plt.title("Average scores by course")
plt.xlabel("Course")
plt.ylabel("Average score")
bars = plt.bar(courses, average_scores)
plt.bar_label(bars)
plt.ylim(0,100)
image_path = Path(__file__).with_name("course_scores.png")
plt.savefig(image_path)
plt.show()