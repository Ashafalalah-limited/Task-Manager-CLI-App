from userregistration import tasks

def view_tasks(uname):
    print('\n-- Available Tasks ---')
    user_tasks = tasks.get(uname, [])
    if not user_tasks:
        print('You Don\'t Have Tasks Available')
        return
    for idx, task in enumerate(user_tasks, 1):
        print(f"{idx}. {task}")
