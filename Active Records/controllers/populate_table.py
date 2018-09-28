from utils import *

if __name__ == '__main__':

    cnx = DatabaseUtils.connect_to_database('workshop_users')
    cursor = cnx.cursor()
    try:
        data = [
            {'form_id': "1", 'to_id': "1", 'message_content': "Hello, world", 'message_timestamp': "2018-09-21"},
            {'form_id': "2", 'to_id': "2", 'message_content': "Hello, world. Again.", 'message_timestamp': "2018-09-21"},
            {'form_id': "3", 'to_id': "3", 'message_content': "Message here!!", 'message_timestamp': "2018-09-11"}
        ]

        DatabaseUtils.insert_data(cursor, 'Messages', data)

    finally:
        DatabaseUtils.close_cursor(cursor)
        DatabaseUtils.close_connection('workshop_users')
