#First thing is to create an empty list, which will be used to append to later.
tasks = []
#Organize codes into functions
#Start with a main menu that welocmes users and displays a main menu with all options.
def main_menu():
    print("\n --Hello, welcome to the Task Menu--")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
    #Begin working option by option
    #Add task will be simplified with just try, except, finally
def add_task():
    try: 
        task = input("Enter new task: ")
        tasks.append(task)
    except:
        print("Error while adding task.")
    finally:
        print("Task added!")
    #view task will take on more by adding if , else, for
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
       #delete task will also require more work with if else, along with try,except, finally 
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
        """majority of time most errors result from 
        deleting something so 'try' and 'finally' ideal here!"""
        
# While True so we can begin to execute the commands 
#Adding in if elif else in between true, except, finally to ensure program runs smoothly
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