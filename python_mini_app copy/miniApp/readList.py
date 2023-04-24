def read_list():
    the_tasks = []
    try:
        with open('task.txt', 'r') as fp:
            reader = fp.read().strip().split('\n\n')
            for read in reader:
                data = read.strip().split('\n')                
                if len(data) == 2:
                    deadline = data[1]
                    task = {'title': data[0],'deadline': deadline}
                    the_tasks.append(task)
                elif len(data) > 2:
                    deadline = data[-1]
                    description = '\n'.join(data[1:-1])
                    task = {'title': data[0],'deadline': deadline,'description': description.strip()}
                    the_tasks.append(task)
    except FileNotFoundError:
        print('You have no tasks at this time')
    return the_tasks
