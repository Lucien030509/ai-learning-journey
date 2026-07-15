def calculate_average(numbers):
    return sum(numbers) / len(numbers)
scores = [80, 90, 100]
scores.append(int(input("Enter a score:")))
average = calculate_average(scores)
print(average)
print(min(scores))
print(max(scores))