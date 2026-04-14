def display_menu():
    print("\nTo-Do List Application")
    print("1. View Task")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_task(tasks):
    if not tasks:
        print("your To-Do List is empty.")
    else:
        print("\n Your To-Do List:")

    index = 1
    for task in tasks:
        print(f"{index}. {task}")
        index += 1

def add_task(tasks):
    task = input("enter the task to add:")
    tasks.append(task)
    print(f"Task added succesfully")

def delete_task(tasks):
    view_task(tasks)
    try:
        task_number=int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number -1)
            print(f"Task '{removed_task}' Deleted successfully.")
        else:
            print("Invalid task number. Please try again")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def todo_list():
    tasks = []
    while True:
        display_menu()
        choice =input("enter your choice (1-4):")
        if choice == '1':
            view_task(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice =='3':
            delete_task(tasks)
        elif choice =='4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")
todo_list()

