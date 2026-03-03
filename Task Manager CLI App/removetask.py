from userregistration import tasks
from viewtasks import view_tasks

def remove_task(uname):
    user_task = tasks.get(uname,[])
    if not user_task:
        print('You Have No Tasks To Remove.')
        return
    view_tasks(uname)

    try:
        ind = int(input('Enter Task Number To Remove: '))
        if 1 <= ind <= len(user_task):
            rmv = user_task.pop(ind - 1)
            print('Task Has Been Removed:', rmv)
        else:
            print('Invalid Task Number.')
    except ValueError:
        print('Please Enter a Valid Number.')
