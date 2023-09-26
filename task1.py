import json
import os
from datetime import datetime

# Define the data file path for storing tasks
data = "tasks.json"

# Load tasks from the data file if it exists
def fill_tasks_here():
    tasks = []
    if os.path.exists(data):
        with open(data, "r") as file:
            tasks = json.load(file)
    return tasks

# Save tasks to the data file
def save_tasks(tasks):
    with open(data, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_new_task(tasks):
    task = {}
    task["title"] = input("Enter task title: ")
    task["priority"] = input("Enter task priority (high/medium/low): ").lower()
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    try:
        task["due_date"] = datetime.strptime(due_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Task not added.")
        return
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# Remove a task
def remove_a_task(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['title']} (Priority: {task['priority']}, Due Date: {task['due_date']})")
    try:
        index = int(input("Enter the number of the task to remove (or 0 to cancel): ")) - 1
        if index == -1:
            return
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed_task['title']}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Mark a task as completed
def mark_task_completed(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks):
        status = "Completed" if task.get("completed") else "Not Completed"
        print(f"{i + 1}. {task['title']} (Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status})")
    try:
        index = int(input("Enter the number of the completed task (or 0 to cancel): ")) - 1
        if index == -1:
            return
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[index]['title']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# List tasks
def list_of_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            status = "Completed" if task.get("completed") else "Not Completed"
            print(f"{i + 1}. {task['title']} (Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status})")

# Main function
def main():
    tasks = fill_tasks_here()
    while True:
        print("\nTASKI - To-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_task(tasks)
        elif choice == "2":
            remove_a_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            list_of_tasks(tasks)
        elif choice == "5":
            print("Exiting TASKI. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
