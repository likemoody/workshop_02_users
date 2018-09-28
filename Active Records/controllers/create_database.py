from utils import *

if __name__ == '__main__':

    cnx = DatabaseUtils.connect_to_database('workshop_users')
    cursor = cnx.cursor()
    try:
        DatabaseUtils.create_database(cursor, 'workshop_users')
    finally:
        DatabaseUtils.close_cursor(cursor)
        DatabaseUtils.close_connection('workshop_users')
