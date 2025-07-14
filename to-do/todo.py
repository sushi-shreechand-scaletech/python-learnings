from task_manager import (
    load_tasks, save_tasks,
    add_task, list_tasks,
    mark_complete, delete_task
)

def menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def main():
    tasks = load_tasks()

    while True:
        menu()
        try:
            choice = input("Enter your choice (1-5): ").strip()
            if choice == '1':
                list_tasks(tasks)

            elif choice == '2':
                desc = input("Enter task description: ")
                if not desc:
                    raise ValueError("Task description cannot be empty.")
                add_task(desc, tasks)
                tasks = load_tasks()
                print("Task added!")

            elif choice == '3':
                task_id = input("Enter task ID to mark as done: ")
                if mark_complete(task_id, tasks):
                    print("Marked as done.")
                else:
                    print("Invalid task ID.")

            elif choice == '4':
                task_id = input("Enter task ID to delete: ")
                tasks = delete_task(task_id, tasks)
                print("Task deleted if ID was valid.")

            elif choice == '5':
                print("Exiting To-Do App. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1 to 5.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
