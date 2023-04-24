from readList import read_list
from writeTask import write_task

def delete_task(task):
    ans = input('Should we delete?(yes/no)')
    try:
        if ans == 'yes':
          tasks_list = read_list()
          tasks_list.remove(task)
          write_task(tasks_list)
          print('\n','Task is deleted')
        else:
            print('Task is not deleted')
    except ValueError:
        ('Invalid entry. Enter a valid answer!')
  

