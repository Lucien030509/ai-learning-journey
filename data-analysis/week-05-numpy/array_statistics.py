import numpy as np
student_scores = np.array([
    [80,90,100],
    [70,85,95]])
print(student_scores)
print(student_scores.shape)
print(student_scores[0])
print(student_scores[0, 1])
print(student_scores.mean(axis=1))
print(student_scores.mean(axis=0))
