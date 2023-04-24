from datetime import datetime
from process import process_task
from write import write_tasks
def create_new_task():
    title = input('What is the title of the task?')

    # read multiple lines of input from the console
    input_lines = []
    print('Please enter the task description. Write END when you are finished.')
    while True:
        try:
            line = input()
            if "END" in line:
                break
        except EOFError:
            break
        input_lines.append(line)
    if len(input_lines) == 0:
        description = "no description"
    else:
        description = '\n'.join(input_lines)
   
    while True:
        try:
            deadline= datetime.strptime(input('Write the deadline date in DD MM YYYY format ' ), '%d %m %Y')
            str_deadline = deadline.strftime('%d %B %Y')
            break
        except ValueError:
            print("Invalid deadline format. Please enter the deadline in the format YYYY-MM-DD HH:MM.")

    task = {
        'title': title,
        'description': description,
        'deadline': str_deadline
    }

    tasks = process_task()
    tasks.append(task)
    write_tasks(tasks)
    print("task created successfully")





   



