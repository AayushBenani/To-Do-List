# Simple To-Do List in Python

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet!\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!\n")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a number!\n")

def menu():
    while True:
        print("=== To-Do List Menu ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")

        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

menu()