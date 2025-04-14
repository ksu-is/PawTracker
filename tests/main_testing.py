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
