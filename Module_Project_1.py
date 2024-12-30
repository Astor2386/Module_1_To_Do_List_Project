#Create empty task dictionary
tasks = []
#Create initial main menu and options
def main_menu():
    print("\n --Hello, welcome to the Task Menu--")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
    
def add_task():
    try: 
        task = input("Enter new task: ")
        tasks.append(task)
    except:
        print("Error while adding task.")
    finally:
        print("Task added!")
    
def view_task():
    try:
        if not tasks:
            print("No tasks available")
        else:
            for task in tasks:
                print(task)
    except:
        print("An error occurred while viewing tasks.")
    finally:
        print("View tasks complete.")
        
def delete_task():
    try:
        if not tasks:
            print("No tasks to delete.")
        else:
            task_to_delete = input("Enter task to delete: ")
            if task_to_delete in tasks:
                tasks.remove(task_to_delete)
                print("Task deleted")
            else:
                print("Task not found")
    except:
        print("deleting task failed")
    finally:
        print("Delete task completed.")
        
while True:
    try:
        main_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Error, invalid option.")
    except:
        print("An Error occured.")
    finally:
        print("Operation completed.")