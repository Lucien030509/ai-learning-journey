log_message = input("Enter a learning note:")
with open("python-basics/week-03-files-errors/learning_log.txt", "a") as file:
    file.write(log_message + "\n")
print("Note saved")