# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added:", task)

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed:", task)
    else:
        print("Task not found:", task)

# Function to display the current tasks
def display_tasks():
    if tasks:
        print("Current tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")

# Main loop
while True:
    print("\nTo-Do List Manager")
    print("1. Add task")
    print("2. Remove task")
    print("3. Display tasks")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        display_tasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
