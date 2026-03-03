from userregistration import users
import sys
from taskmenu import task_menu

def login():
    print('\n=== User Login Details ===')
    atmpt = 0
    while atmpt < 5:
        uname = input('Enter Your Username: ').strip()
        upass = input('Enter Your Password: ').strip()
        if users.get(uname) == upass:
            print('Login Successful. Welcome,', uname)
            task_menu(uname)
            return
        else:
            atmpt += 1
            rmng = 5 - atmpt
            if rmng > 0:
                print(f'Incorrect Username or Password. You Have {rmng} Attempts Left.\n')
                print('Please Try Again!...')
                bk = input('Type 1 To Return or Press Enter To Try Again').strip()
                if bk == '1':
                    return None
            else:
                print('Too Many Failed Attempts! Closing App.')
                sys.exit()
    # return None