from datetime import datetime

def write_task(tasks):
    func = lambda x: datetime.strptime(x['deadline'], '%d %B %Y')
    the_tasks = sorted(tasks, key = func)

    with open('task.txt', 'w') as file:
        for task in the_tasks:
            file.write(task['title'] + '\n')
            if 'description' in task:
                file.write(task['description'] + '\n')
            file.write(task['deadline'] + '\n'+'\n')
            
