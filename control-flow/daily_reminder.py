task = input("Enter your task: ")
Priority = input ("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no):")

match property:
    case "high":
         reminder = f"'{task}' is a high priority task"
    case " medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"
if time == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print("\nReminder:", reminder)             
