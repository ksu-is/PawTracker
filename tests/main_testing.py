from datetime import datetime, timedelta

def add_task(pet_name, task_type, date, time):
    """
    Add a new task to the pet's schedule.
    Returns a dictionary representing the task.
    """
    task = {
        "pet_name": pet_name,
        "task_type": task_type,
        "date": date,
        "time": time
    }
    print(f"Task added: {task}")
    return task


def view_schedule(schedule):
    """
    Display all tasks in the schedule.
    """
    if not schedule:
        print("No tasks scheduled.")
    else:
        for task in schedule:
            print(f"{task['pet_name']} - {task['task_type']} on {task['date']} at {task['time']}")

def delete_task(schedule, pet_name, task_type):
    updated_schedule = []
    task_found = False
    for task in schedule:
        if task["pet_name"] == pet_name and task["task_type"] == task_type:
            task_found = True
        else:
            updated_schedule.append(task)
    if task_found:
        print(f"Task '{task_type}' for {pet_name} removed.")
    else:
        print(f"No matching task found for {pet_name}.")
    return updated_schedule

def update_task(schedule, pet_name, old_task_type, new_task_type, new_date, new_time):
    updated = False
    for i, task in enumerate(schedule):
        if task["pet_name"] == pet_name and task["task_type"] == old_task_type:
            schedule[i] = {
                "pet_name": pet_name,
                "task_type": new_task_type,
                "date": new_date,
                "time": new_time
            }
            updated = True
            print(f"Task updated: {schedule[i]}")
            break
    if not updated:
        print(f"Task '{old_task_type}' for {pet_name} not found.")
    return schedule
def check_reminders(schedule):
    """
    Print reminders for tasks happening within the next hour.
    """
    now = datetime.now()
    for task in schedule:
        task_time_str = f"{task['date']} {task['time']}"
        try:
            task_datetime = datetime.strptime(task_time_str, "%Y-%m-%d %H:%M")
            if now <= task_datetime <= now + timedelta(hours=1):
                print(f" Reminder: {task['task_type']} for {task['pet_name']} at {task['time']} today.")
        except ValueError:
            print(f"Skipping invalid task date/time: {task}")


# ------------------ Demo (Optional for Playing Around) ------------------

if __name__ == "__main__":
    run_tests()

    # Sample usage
    schedule = []
    schedule.append(add_task("Milo", "vet appointment", "2025-04-14", "16:00"))
    schedule.append(add_task("Luna", "walk", "2025-04-14", "14:30"))

    view_schedule(schedule)

    check_reminders(schedule)  # This will alert if a task is due soon
