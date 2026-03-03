from userregistration import users, tasks
from viewtasks import view_tasks
from addtask import add_task
from removetask import remove_task
# from userlogin import login

def task_menu(uname):
    while True:
        print('\n--- Task Menu For', uname, '---')
        print('1. View Tasks.','\n2. Add Task.','\n3. Remove Task.','\n4. Return Back.')
        try:
            choice = int(input('Choose an Option From The Menu: '))
            if choice == 1:
                view_tasks(uname)
            elif choice == 2:
                add_task(uname)
            elif choice == 3:
                remove_task(uname)
            elif choice == 4:
                print('Returning.......')
                # login()
                break
            else:
                print('Invalid, Try Again...')
        except ValueError:
            print('Invalid Input. Please Enter Only Digit Number.')
