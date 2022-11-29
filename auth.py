users = {}

def add_user (user_name):
    if user_name in users.keys():
        print('Such user already exists. choose another name')
    else:
        password = input('Enter password: ')
        users[user_name] = password

def authorisation(user_name, password):
    if user_name in users.keys():
        if users[user_name] == password:
            print('Successful authorization')
        else:
            print('Wrong password')
    else:
        print('Wrong user name')



while input('Do you want to log into the system: \n if yes - press 1 \n if no - press 0') != '0':
    a = input('Do you want to add new user? (yes/no): ')
    if a == 'yes':
        name = input('Enter user name: ')
        add_user(name)




else:
    print('Good bye!')

