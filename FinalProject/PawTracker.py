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
