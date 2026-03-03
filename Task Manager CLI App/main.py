from userlogin import login
from userregistration import register_user
from taskmenu import task_menu

def main_m():
    uname = None
    while True:
        print('\n=== Welcome To CLI App Menu ===')
        print('1. Register','\n2. Login','\n3. Task Menu','\n4. Logout','\n5. Exit App')
        op = input('Choose An Option To Continue: ').strip()
        if not op.isdigit():
            print('Invalid Entry....')
        if op == '1':
            register_user()
        elif op == '2':
            uname = login()
            if uname is None:
                continue
        elif op == '3':
            if uname:
                task_menu(uname)
            else:
                print('\nPlease Login First.')
        elif op == '4':
            print('\nLogging Out.... Goodbye!\n')
            uname = None
            register_user()
        elif op == '5':
            print('Exiting App... Goodbye')
            print('\n=== See You Soon ===')
            break
        else:
            print('Only Digit Numbers Are Allowed.\n')
            main_m()
if __name__ == '__main__':
    main_m()
