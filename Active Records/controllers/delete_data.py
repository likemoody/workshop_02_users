from models.User import User
from utils import *

if __name__ == "__main__":
    cnx = DatabaseUtils.connect_to_database('workshop_users_db')
    crs = cnx.cursor()
    print('Connection opened')
    try:

        users = User.load_all_users(crs)        # load all users (rows >> objects)
        for user in users:                      # check usernames and id
            print(user.id, ':', user.username)
        user_to_delete = users[1]               # << {} has been removed
        res = user_to_delete.delete(crs)        # delete user with id = {}
        print(res)                              # check if user in DB

    finally:
        DatabaseUtils.close_cursor(crs)
        cnx.close()
        print('Connection closed')
