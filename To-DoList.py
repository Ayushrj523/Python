tasks = []

try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View all tasks")
    print("2. Add new task")
    print("3. Mark task as done")
    print("4. Save and Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\nTasks:")
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
    
    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print("Task added.")

    elif choice == "3":
        if not tasks:
            print("No tasks to mark as done.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
            done = int(input("Enter task number to mark as done: "))
            if 1 <= done <= len(tasks):
                tasks[done - 1] += " [Done]"
                print("Task marked as done.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Tasks saved. Exiting...")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")
