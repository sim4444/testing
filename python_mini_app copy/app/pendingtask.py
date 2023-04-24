from datetime import datetime
from process import process_task
from view import view_task
from delete import delete_task
from viewlist import view_list

def view_pending_task(): 

    tasks = process_task()
    all_tasks = sorted(tasks, key=lambda element: datetime.strptime(element['deadline'], '%d %B %Y'))
    deadline_tasks=[]
    today = datetime.now()
    i=0
    for task in all_tasks:
        
        deadline= task['deadline']
        date_deadline= datetime.strptime(deadline, '%d %B %Y')
        if date_deadline > today:
             print(i+1, ' Title:', task['title'])
             i += 1
             deadline_tasks.append(task)
    if i>0:    
            select_task = int(input('Enter the number of the task you want to select or press 0 to go back to main menu : '))
            if select_task == 0:
                return
            
            selected_task = deadline_tasks[select_task-1]
            print('Selected task:', selected_task['title'])
            action = input('What would you like to do with this task? (view/delete/back) ')
            if action == 'view':
                view_task(selected_task)
                ask= input('Press b to go back to task list')
                if ask=='b':
                    view_pending_task()
                else:
                    print('invalid entry')
            elif action == 'delete':
                delete_task(selected_task)
                ask= input('Press b to go back to task list')

                if ask=='b':
                    view_pending_task()
                else:
                    print('invalid entry')
            elif action == 'back':
                view_list()
            else:
                print('Invalid action')
                return
    else:
        print("Sorry you dont have have any tasks right now")
    











