import csv
import os
from datetime import datetime

TASKS_FILE = "tasks.csv"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, mode='r', newline='') as f:
            reader = csv.DictReader(f)
            tasks = list(reader)
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, mode='w', newline='') as f:
        fieldnames = ["id", "task", "status", "created_at"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

def add_task(description, tasks):
    task_id = str(len(tasks) + 1)
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    tasks.append({
        "id": task_id,
        "task": description.strip(),
        "status": "pending",
        "created_at": created_at
    })
    save_tasks(tasks)

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        print(f"{t['id']}. {t['task']} [{t['status']}] (added on {t['created_at']})")

def mark_complete(task_id, tasks):
    for t in tasks:
        if t['id'] == task_id:
            t['status'] = "done"
            save_tasks(tasks)
            return True
    return False

def delete_task(task_id, tasks):
    new_tasks = [t for t in tasks if t['id'] != task_id]
    if len(new_tasks) < len(tasks):
        save_tasks(new_tasks)
        return new_tasks
    return tasks
