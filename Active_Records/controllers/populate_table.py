from utils import *
from models.User import User

if __name__ == '__main__':

    cnx = DatabaseUtils.connect_to_database('workshop_users_db')
    cursor = cnx.cursor()
    try:
        # adding a new user to the db >> Users table
        user_1 = User()  # create an object (empty)
        user_1.username = 'Іван Яблучко' # fill an object with data
        user_1.email = 'i.ja@mail.com'  # fill an object with data
        user_1.set_password('somepass', 'saltie')  # fill an object with data
        user_1.save_to_db(cursor)  # "save" object (transfer data from object to DB)

    finally:
        DatabaseUtils.close_cursor(cursor)
        cnx.close()
