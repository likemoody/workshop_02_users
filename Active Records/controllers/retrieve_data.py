from models.User import User
from utils import *

if __name__ == "__main__":
    cnx = DatabaseUtils.connect_to_database('workshop_users_db')
    crs = cnx.cursor()
    print('Connection opened')
    try:
        # retrieve data of user with id of {}
        user_no_6 = User.load_user_by_id(crs, 6)

        # retrieve data of all users in table Users
        users = User.load_all_users(crs)

        # check data
        print(len(users))
        for user in users:
            print(user.username)

    finally:
        DatabaseUtils.close_cursor(crs)
        cnx.close()
        print('Connection closed')
