weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]

day_count = len(weekdays)

employee_count = 14

for employee_number in range(0, employee_count):
    day_index = employee_number % day_count
    weekday = weekdays[day_index]

    print(f"Scheduling employee #{employee_number} on {weekday}")