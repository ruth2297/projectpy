import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

# Function to load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = json.load(file)
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task():
    print("\n--- Add New Task ---")
    title = input("Enter task title: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")

    try:
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    tasks = load_tasks()
    new_task = {
        "title": title,
        "deadline": deadline,
        "done": False
    }
    tasks.append(new_task)
    save_tasks(tasks)

    print("Task added successfully.")

# Function to display all tasks
def show_all_tasks():
    print("\n--- All Tasks ---")
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(f"{index + 1}. {task['title']} | Due: {task['deadline']} | Status: {status}")

# Function to display only pending tasks
def show_pending_tasks():
    print("\n--- Pending Tasks ---")
    tasks = load_tasks()
    found = False

    for index, task in enumerate(tasks):
        if not task["done"]:
            found = True
            print(f"{index + 1}. {task['title']} | Due: {task['deadline']}")

    if not found:
        print("All tasks are completed!")

# Function to mark a task as done
def mark_task_as_done():
    print("\n--- Mark Task as Done ---")
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No tasks to update.")
        return

    show_pending_tasks()
    task_number = input("Enter task number to mark as done: ")

    if not task_number.isdigit():
        print("Invalid input. Enter a number.")
        return

    task_index = int(task_number) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Task number out of range.")
        return

    tasks[task_index]["done"] = True
    save_tasks(tasks)

    print("Task marked as completed.")

# Function to delete a task
def delete_task():
    print("\n--- Delete Task ---")
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    show_all_tasks()
    task_number = input("Enter task number to delete: ")

    if not task_number.isdigit():
        print("Invalid input. Enter a number.")
        return

    task_index = int(task_number) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Task number out of range.")
        return

    deleted_task = tasks.pop(task_index)
    save_tasks(tasks)

    print(f"Task '{deleted_task['title']}' deleted.")

# Main menu loop
def main():
    while True:
        print("\n=== TO-DO LIST MANAGER ===")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. View Pending Tasks")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_all_tasks()
        elif choice == "3":
            show_pending_tasks()
        elif choice == "4":
            mark_task_as_done()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()
