from datetime import datetime
from readList import read_list
from writeTask import write_task
def create_new_task():
    title = input('Enter the title of the task:')
    description_lines = []
    print('Enter the task description and add . when adding is done')
    while True:
        try:
            description_line = input("Enter description now:")
            if "." in description_line:
                break
        except EOFError:
            print("This is a multi line description.")
        finally:
            description_lines.append(description_line)
    if len(description_lines) == 0:
        print('no description is added')
    else:
        description='\n'.join(description_lines)
    while True:
        try:
            deadline= datetime.strptime(input('Enter the deadline date in format : DD MM YYYY :'), '%d %m %Y')
            deadline_format = deadline.strftime('%d %B %Y')
            break
        except ValueError:
            print("Invalid format of deadline date. Please enter the deadline in the format : DD MM YYYY.")
    a_task = {'title': title, 'description': description,'deadline': deadline_format}
    list_of_tasks = read_list()
    list_of_tasks.append(a_task)
    write_task(list_of_tasks)
    print('\n',"This task has been created ! ")





   



