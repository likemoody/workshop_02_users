from models.User import User
from utils import *

if __name__ == "__main__":
    cnx = DatabaseUtils.connect_to_database('workshop_users_db')
    crs = cnx.cursor()
    print('Connection opened')
    try:
        # retrieve data of user with id of {}
        user = User.load_user_by_id(crs, 5)

        # modify record (row in DB / object in app)
        user.username = 'Bob'
        user.save_to_db(crs)

        # check if changes happened
        user_check = User.load_user_by_id(crs, 5)
        print(user_check.username)

    finally:
        DatabaseUtils.close_cursor(crs)
        cnx.close()
        print('Connection closed')
