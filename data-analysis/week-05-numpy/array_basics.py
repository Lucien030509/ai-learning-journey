import numpy as np
scores = np.array([80, 90, 100])
print(scores)
print(type(scores))
print(scores + 5)
print(scores.mean())
print(scores.min())
print(scores.max())
print(scores >= 90)
high_scores = scores[scores >= 95]
print(high_scores)