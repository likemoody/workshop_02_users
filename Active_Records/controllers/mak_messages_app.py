import argparse
from datetime import datetime

from ..models.User import *
from ..models.Message import *
from utils import *

description = '''Messages app. Please see help: -h'''

def messages_app(description, db_name):
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
                        help='current password')


    parser.add_argument('-t', '--to',
                        metavar='T',
                        type=str,
                        help='send message to ...')
    parser.add_argument('-s', '--send',
                        metavar='S',
                        type=str,
                        help='send message of content ... (use "" or '' to send mulitple word message)')

    # flags
    parser.add_argument('-l', '--list',
                        help='list of all sent messages',
                        action='store_true')

    args = parser.parse_args()
    u = args.username
    p = args.password

    t = args.to
    s = args.send

    l = args.list

    user_pass_list = []
    for user in users_raw:
        user_pass_list.append({user.username: user.hashed_password})

    user_list = [user.username for user in users_raw]


    # PROCESSING DATA
    try:
        if u and p and t and s:  # scenario 1 - sending message
            cnx = DatabaseUtils.connect_to_database(db_name)
            crs = cnx.cursor()

            # RETRIEVING DATA
            user = User.load_user_by_name(crs, u)

            password_given = None
            password_in_db = None

            if user:
                # PREPARING DATA
                password_given = p
                password_in_db = user.hashed_password
            else:
                u = None

            # PROCESSING DATA
            if u and password_in_db.startswith(password_given):
                if t in user_list:
                    if s != '':
                        tid = 0
                        for user in users_raw:
                            if user.username == t: tid = user.id
                        message = Message()
                        message.from_id = user.id
                        message.to_id = tid
                        message.message_content = s
                        message.creation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        message.save_to_db(crs)
                        print('Message sent')
                    else:
                        print('Message field can\'t be empty')
                else:
                    print('No such addressee')
            else:
                print('Wrong credentials')

            DatabaseUtils.close_cursor(crs)
            cnx.close()

        elif u and p and l:  # scenario 2 - list all messages
            cnx = DatabaseUtils.connect_to_database(db_name)
            crs = cnx.cursor()

            # RETRIEVING DATA
            user = User.load_user_by_name(crs, u)

            password_given = None
            password_in_db = None

            if user:
                # PREPARING DATA
                password_given = p
                password_in_db = user.hashed_password
            else:
                u = None

            # PROCESSING DATA
            if u and password_in_db.startswith(password_given):
                messages = Message.load_all_messages(crs, 'desc', user.id)
                print('\n-------------------\nMessages received:', len(messages))
                for message in messages:
                    print(message.creation_date, message.message_content)
                print('-------------------\n')
            else:
                print('Wrong credentials')

            DatabaseUtils.close_cursor(crs)
            cnx.close()

        else:  # scenario 3 - app ran without flags: show help
            parser.print_help()
        return None



    except Exception as e:
        print(e)
    finally:
        if cnx is not None:
            cnx.close()


if __name__ == "__main__":
    messages_app(description, 'workshop_users')