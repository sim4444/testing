from datetime import datetime
from readList import read_list
from view import view_task
from deleteTask import delete_task
from viewAllTasks import view_all_tasks


def view_pending_tasks(): 
    tasks = read_list()
    func=lambda x: datetime.strptime(x['deadline'], '%d %B %Y')
    the_tasks = sorted(tasks, key=func)
    deadline_tasks=[]
    today = datetime.now()
    n=0
    for task in the_tasks:
        deadline= task['deadline']
        date_deadline= datetime.strptime(deadline, '%d %B %Y')
        if date_deadline > today:
             print(n+1, ' Title:', task['title'])
             n = n + 1
             deadline_tasks.append(task)
    if n>0:    
        while True:
            try:
                choose_task = int(input('Choose the task number OR press 0 to go to main menu: '))
                if choose_task == 0:
                    return
                chosen_task = deadline_tasks[choose_task-1]
                while True:
                    print('Chosen task is:', chosen_task['title'])
                    print('Enter v to view ')
                    print('Enter d to delete ')
                    print('Enter g to go back ')
                    ans = input('Enter v / d / g :')
                    if ans == 'v':
                        view_task(chosen_task)
                        break
                    elif ans == 'd':
                        delete_task(chosen_task)
                        break
                    elif ans == 'g':
                        break
                    else:
                        print('Invalid action')
                        return
            except Exception as E:
                print(f'Error: {str(E)}.Try again.')
    else:
        print("Sorry you dont have have any tasks right now")
    











