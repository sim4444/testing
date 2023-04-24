from viewAllTasks import view_all_tasks
from viewPendingTasks import view_pending_tasks
from createTask import create_new_task
def main():
    go = True
    while go:
        print("\nMini Todo List App\n")
        print("Enter 1 - View all tasks")
        print("Enter 2 - View pending tasks")
        print("Enter 3 - Create a new task")
        print("Enter 0 - Quit\n")
        answer = input("Please enter your choice: ")
        if answer == "1":
            view_all_tasks()
        elif answer == "2":
            view_pending_tasks()
        elif answer == "3":
            create_new_task()
        elif answer == "0":
            print("Good-Bye!!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 3: ")
if __name__ == "__main__":
    main()
