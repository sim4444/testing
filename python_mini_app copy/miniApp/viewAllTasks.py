from datetime import datetime
from view import view_task
from deleteTask import delete_task
from readList import read_list

def view_all_tasks():
    tasks = read_list()
    func=lambda x: datetime.strptime(x['deadline'], '%d %B %Y')
    the_tasks = sorted(tasks, key = func)
    m = 0
    # print('\n',the_tasks,'\n')
    for task in the_tasks:
        print(m+1, ' Title is:', task['title'])
        m = m+ 1
    if m>0: 
        go=True
        while go:
            try:
                choose_task = input('Choose the task number OR press 0 to go to main menu: ')
                if not choose_task.isdigit():
                    raise ValueError('Invalid input. Please enter a number.')
                elif int(choose_task) == 0:
                    return
                elif int(choose_task) < 1 or int(choose_task) > len(tasks):
                    raise IndexError('Invalid task number. Please try again.')
                else:
                    chosen_task = tasks[int(choose_task)-1]
                    print('Chosen task is:', chosen_task['title'])
                    while True:
                        try:
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
                                print('Invalid entry. try again.')
                        except IndexError as IE:
                            print("Enter valid number")
                        except Exception as E:
                            print(f'An error occurred: {str(E)}. Please try again.')
                        
            except ValueError as E:
                print(str(E))
            except IndexError as IE:
                print(str(IE))
    else:
        print("You have no tasks yet.")

