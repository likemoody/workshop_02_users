from utils import *

if __name__ == '__main__':
    cnx = DatabaseUtils.connect_to_database('workshop_users')
    cursor = cnx.cursor()

    # DatabaseUtils.create_database(cursor, 'workshop_users')
    # DatabaseUtils.create_table(cursor, 'Users (id serial not null, name varchar(25), email varchar(25) unique, hashed_password text, PRIMARY KEY (id))')
    # DatabaseUtils.create_table(cursor, 'Messages (id SERIAL NOT NULL, form_id INT UNIQUE, to_id INT UNIQUE, message_content TEXT, message_timestamp TIMESTAMP, PRIMARY KEY(id))')
    data = {
        {'form_id': "1", 'to_id': "1", 'message_content': "Hello, world", 'message_timestamp': "2018-09-21"},
        {'form_id': "2", 'to_id': "2", 'message_content': "Hello, world. Again.", 'message_timestamp': "2018-09-21"},
    }

    DatabaseUtils.insert_data(cursor, 'Messages', data)

    cursor.close()
    cnx.close()
