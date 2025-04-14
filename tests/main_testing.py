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
