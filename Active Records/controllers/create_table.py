from utils import *

if __name__ == '__main__':

    cnx = DatabaseUtils.connect_to_database('workshop_users')
    cursor = cnx.cursor()
    try:
        DatabaseUtils.create_table(cursor, 'Users (id serial not null, name varchar(25), email varchar(25) unique, hashed_password text, PRIMARY KEY (id))')
        DatabaseUtils.create_table(cursor, 'Messages (id SERIAL NOT NULL, form_id INT UNIQUE, to_id INT UNIQUE, message_content TEXT, message_timestamp TIMESTAMP, PRIMARY KEY(id))')
    finally:
        DatabaseUtils.close_cursor(cursor)
        DatabaseUtils.close_connection('workshop_users')
