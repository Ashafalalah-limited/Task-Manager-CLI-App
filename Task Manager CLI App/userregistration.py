
users = {
    'Asha6':'1234An',
    '3John':'23JH44',
    'Be45n':'44bE76',
    'Jeff!':'Fj2234',
    'Musa5':'M8485U',
    'Abba7':'6584Bb',
    'Mod67':'MD7383'
}
tasks = {
    'Asha6':['Buy Food','Buy Gas'],
    '3John':['Go to the Market','Buy Casava','Go Home'],
    'Be45n':['Go and Dance','Stay at home'],
    'Jeff!':['Do your Assignments','Buy Data and do the Assignments'],
    'Musa5':['Buy Casava'],
    'Abba7':['Go and Pray','Stay at home'],
    'Mod67':['Go and collect my Money']
}

def register_user():
    print('=== Welcome To Task Manager CLI App ===')

    while True:
        print('\n--- Enter Your Details For Registration ---')

        uname = input('Enter Your Username: ').strip()
        if not uname:
            print('Username Cannot Be Empty. Please Try Again.\n')
            continue
        elif len(uname) != 5:
            print('Username Must Be Exactly 5 Characters. Try Again.\n')
            continue
        elif uname in users:
            print('Username Already Exists. Redirecting to Login...\n')
            from userlogin import login
            login()
            return

        while True:
            upass = input('Enter Your Password (Max 6 Characters): ').strip()

            if not upass:
                print('Password Cannot Be Empty. Please Try Again.')
            elif ' ' in upass:
                print('Spaces Are Not Allowed In Password. Please Try Again.\n')
            elif len(upass) > 6:
                print('Password Cannot Be More Than 6 Characters. Please Try Again.\n')
            elif len(upass) < 6:
                print('Password Is Too Short. Please Try Again.\n')
            else:
                break

        users[uname] = upass
        tasks[uname] = []
        print('Registration Successful For:', uname)

        choice = input('Press (1) To Login (2) To Return: ').strip()
        if choice == '1':
            from userlogin import login
            login()
        break
