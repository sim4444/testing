from process import process_task
from datetime import datetime
from view import view_task
from delete import delete_task

def view_list():
    tasks = process_task()
    all_tasks = sorted(tasks, key=lambda x: datetime.strptime(x['deadline'], '%d %B %Y'))

    i = 0
    for task in all_tasks:
        print(i+1, ' Title:', task['title'])
        i += 1
    if i>0: 
        while True:
            try:
                select_task = input('Enter the number of the task you want to select or press 0 to go back to main menu: ')
                if not select_task.isdigit():
                    raise ValueError('Invalid input. Please enter a number.')
                elif int(select_task) == 0:
                    return
                elif int(select_task) < 1 or int(select_task) > len(tasks):
                    raise IndexError('Invalid task number. Please try again.')
                else:
                    selected_task = tasks[int(select_task)-1]
                    print('Selected task:', selected_task['title'])
                    while True:
                        try:
                            action = input('What would you like to do with this task? (view/delete/back) ')
                            if action == 'view':
                                view_task(selected_task)
                                ask = input('Press b to go back to task list: ')
                                if ask == 'b':
                                    view_list()
                                    break
                                else:
                                    print('Invalid entry. Please try again.')
                            elif action == 'delete':
                                delete_task(selected_task)
                                ask = input('Press b to go back to task list: ')
                                if ask == 'b':
                                    view_list()
                                    break
                                else:
                                    print('Invalid entry. Please try again.')
                            elif action == 'back':
                                view_list()
                                break
                            else:
                                print('Invalid input. Please try again.')
                        except Exception as e:
                            print(f'An error occurred: {str(e)}. Please try again.')
            except ValueError as ve:
                print(str(ve))
            except IndexError as ie:
                print(str(ie))
    else:
        print("Sorry, you don't have any tasks right now.")

