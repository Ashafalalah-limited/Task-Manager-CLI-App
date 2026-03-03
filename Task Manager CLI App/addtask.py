from userregistration import tasks

def add_task(uname):
    tsk = input('Enter New Task: ').strip()
    if tsk:
        if uname not in tasks:
            tasks[uname] = []
        tasks[uname].append(tsk)
        print('Task Added Successfully!')
    else:
        print('Task Cannot be Empty.')
