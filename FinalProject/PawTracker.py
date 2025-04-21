from datetime import datetime, timedelta

def add_task(schedule):
    # Add a new task to the pet's schedule.
    print("\n--- Add a New Task ---")
    pet_name = input("Enter the pet's name: ")
    task_type = input("Enter the type of task (e.g., Vet Visit, Grooming): ")
    date = input("Enter the date for the task (YYYY-MM-DD): ")
    time = input("Enter the time for the task (HH:MM in 24-hour format): ")

    task = {
        "pet_name": pet_name,
        "task_type": task_type,
        "date": date,
        "time": time
    }
    schedule.append(task)
    print(f"\nTask added| [Pet Name: {pet_name}] [Task type: {task_type}] [Date: {date}] [Time: {time}]")
    return schedule

def view_schedule(schedule):
    # Display all tasks in the schedule.
    print("\n--- View Schedule ---")
    if not schedule:
        print("No tasks scheduled.")
    else:
        for idx, task in enumerate(schedule, start=1):
            print(f"{idx}. {task['pet_name']} - {task['task_type']} on {task['date']} at {task['time']}")

def delete_task(schedule):
    # Remove a task from the schedule.
    print("\n--- Delete a Task ---")
    pet_name = input("Enter the pet's name for the task to delete: ")
    task_type = input("Enter the type of task to delete: ")

    updated_schedule = []
    task_found = False
    for task in schedule:
        if task['pet_name'].lower() == pet_name.lower() and task['task_type'].lower() == task_type.lower():
            task_found = True
        else:
            updated_schedule.append(task)

    if task_found:
        print(f"Task '{task_type}' for {pet_name} removed.")
    else:
        print(f"No matching task found for '{task_type}' of {pet_name}.")
    return updated_schedule

def update_task(schedule):
    # Update a specific task in the schedule.
    print("\n--- Update a Task ---")
    pet_name = input("Enter the pet's name for the task to update: ")
    old_task_type = input("Enter the current type of task: ")

    updated = False
    for i, task in enumerate(schedule):
        if task['pet_name'].lower() == pet_name.lower() and task['task_type'].lower() == old_task_type.lower():
            print("Begin updating task below...")
            new_task_type = input("Enter the new task type: ")
            new_date = input("Enter the new date (YYYY-MM-DD): ")
            new_time = input("Enter the new time (HH:MM in 24-hour format): ")

            schedule[i] = {
                "pet_name": pet_name,
                "task_type": new_task_type,
                "date": new_date,
                "time": new_time
            }
            updated = True
            print(f"\nTask updated| [Pet Name: {pet_name}] [Task type: {new_task_type}] [Date: {new_date}] [Time: {new_time}]")
            break

    if not updated:
        print(f"No task found for '{old_task_type}' of {pet_name}.")
    return schedule

def check_reminders(schedule):
    # Print reminders for tasks happening within the next hour.
    print("\n--- Check Reminders ---")
    now = datetime.now()
    for task in schedule:
        try:
            task_time_str = f"{task['date']} {task['time']}"
            task_datetime = datetime.strptime(task_time_str, "%Y-%m-%d %H:%M")
            if now <= task_datetime <= now + timedelta(hours=1):
                print(f"Reminder: {task['task_type']} for {task['pet_name']} at {task['time']} today.")
        except ValueError:
            print(f"Skipping invalid task date/time: {task}")

def main():
    # Main function to run the Pet Care Scheduler.
    schedule = []
    while True:
        print("\n--- Pet Care Scheduler ---")
        print("1. Add Task")
        print("2. View Schedule")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Check Reminders")
        print("6. Exit")
