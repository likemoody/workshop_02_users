import argparse
from models.User import User
from utils import DatabaseUtils

description = '''Communication app. Please see help: -h'''

def app(description):
    parser = argparse.ArgumentParser(description=description)
    # adding values' containers to parser (global app container)
    parser.add_argument('-u', '--username',
                        metavar='U',
                        type=str,
                        help='username')
    parser.add_argument('-p', '--password',
                        metavar='P',
                        type=str,
                        help='current password (min 8 symbols)')
    parser.add_argument('-n', '--new_password',
                        metavar='N',
                        type=str,
                        help='new password')
    # flags
    parser.add_argument('-l', '--list',
                        help='list of all users',
                        action='store_true')
    parser.add_argument('-d', '--delete',
                        help='delete user',
                        action='store_true')
    parser.add_argument('-e', '--edit',
                        help='edit username',
                        action='store_true')

    args = parser.parse_args()

    u = args.username
    p = args.password
    n = args.new_password
    l = args.list
    d = args.delete
    e = args.edit

    #connect to database
    cnx = DatabaseUtils.connect_to_database('workshop_users_db')
    crs = cnx.cursor()

    # get all users
    users_raw = User.load_all_users(crs)

    crs.close()
    cnx.close()

    l = True # uncomment to use "-l" flag

    # appropriate code ahs to be writen instead of print functions
    if u and p and e == False and d == False:
        print(':: Check credentials >> add user or raise error')
        # if username not in db AND password not in DB
            # create account
                # if password length > 8 symbols:
                    # username = args.username
                    # password = args.password
                    # save_to_db()
                    # print('Account created')
                # else:
                    # print('Password must be 8 or more symbols long.')
        # else:
            # print('Account with such username is already registered. Please try another credentials.')
    elif u and p and e and n:
        print(':: Check credentials >> change user password to {} or show message'.format(n))
        # if password and username match:
            # if new pass length > 8
                # password = args.new_password
                # save_to_db()
                # print('Password changed')
            # else:
                # print('Password must be 8 or more symbols long.')
        # else:
            # print('Wrong credentials')
    elif u and p and d:
        print(':: Check credentials >> delete user or show message')
        # if password and username match:
            # delete account
            # print('Account has been deleted')
        # else:
            # print('Wrong credentials')
    elif l:
        print(':: User list ::')
        for user in users_raw:
            print(user.username)
    else:
        parser.print_help()
    return None

if __name__ == "__main__":
    app(description)