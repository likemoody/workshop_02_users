import argparse
from ..models.User import *
from utils import *

description = '''Communication app. Please see help: -h'''

def users_app(description, db_name):
    # RETRIEVING DATA
    #connect to database
    cnx = DatabaseUtils.connect_to_database(db_name)
    crs = cnx.cursor()
    # get all users
    users_raw = User.load_all_users(crs)
    crs.close()
    cnx.close()

    # PREPARING DATA
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
    # TODO add email field

    args = parser.parse_args()
    u = args.username
    p = args.password
    n = args.new_password
    l = args.list
    d = args.delete
    e = args.edit

    user_pass_list = []
    for user in users_raw:
        user_pass_list.append({user.username: user.hashed_password})

    user_list = [user.username for user in users_raw]


    # PROCESSING DATA
    try:

        if u and p and e == False and d == False:  # scenario 1 - registration
            cnx = DatabaseUtils.connect_to_database(db_name)
            crs = cnx.cursor()
            if u not in user_list:
                if len(p) >= 8:
                    new_user = User()
                    new_user.username = u
                    new_user.set_password(p)
                    new_user.save_to_db(crs)
                    # TODO add email
                    print('Account created')
                else:
                    print('Password must be 8 or more symbols long.')
            else:
                print('Account with such username is already registered. Please try another credentials.')
            crs.close()
            cnx.close()
        elif u and p and e and n:  # scenario 2 - password change
            cnx = DatabaseUtils.connect_to_database(db_name)
            crs = cnx.cursor()

            # RETRIEVING DATA
            user = User.load_user_by_name(crs, u)

            # PREPARING DATA
            password_given = p
            password_in_db = user.hashed_password
            password_new = n

            # PROCESSING DATA
            if password_in_db.startswith(password_given):
                if len(password_new) >= 8:
                    user.set_password(password_new)
                    user.save_to_db(crs)
                    print('Password changed')
                else:
                    print('Password must be 8 or more symbols long.')
            else:
                print('Wrong credentials')

            DatabaseUtils.close_cursor(crs)
            cnx.close()

        elif u and p and d:  # scenario 3 - account deletion
            cnx = DatabaseUtils.connect_to_database(db_name)
            crs = cnx.cursor()

            # RETRIEVING DATA
            user = User.load_user_by_name(crs, u)

            # PREPARING DATA
            password_given = p
            password_in_db = user.hashed_password

            # PROCESSING DATA
            if password_in_db.startswith(password_given):
                user.delete(crs)
                print('Account for {} has been deleted.'.format(u))
            else:
                print('Wrong credentials')

            DatabaseUtils.close_cursor(crs)
            cnx.close()

        elif l:  # scenario 4 - get the list of users
            print(':: User list ::')
            for user in users_raw:
                print(user.username)
        else:  # scenario 5 - app ran without flags: show help
            parser.print_help()
        return None

    except Exception as e:
        print(e)
    finally:
        if cnx is not None:
            cnx.close()


if __name__ == "__main__":
    app(description, 'workshop_users')