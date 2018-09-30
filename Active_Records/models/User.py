from validator import *
from utils import *
import random

# Kew will commit his implementation

class User:
    def __init__(self):
        self.__id = -1
        self.username = ""
        self.email = ""
        self.__hashed_password = ""

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password):
        salt = ''.join([random.choice('Sluchajciesiemamyiumywajcierecezmydlem') for i in range(10)])
        self.__hashed_password = str(password) + salt

    def save_to_db(self, cursor):
        if self.__id == -1:
            # saving new instance using prepared statements
            sql = """INSERT INTO Users(name, email, hashed_password)
                     VALUES(%s, %s, %s) RETURNING id"""
            values = (self.username, self.email, self.hashed_password)
            cursor.execute(sql, values)
            self.__id = cursor.fetchone()[0]  # or cursor.fetchone()['id']
            return True
        else:
            sql = """UPDATE Users SET name=%s, email=%s, hashed_password=%s WHERE id=%s"""
            values = (self.username, self.email, self.hashed_password, self.id)
            cursor.execute(sql, values)
            return True

    @staticmethod
    def load_user_by_id(cursor, user_id):
        sql = "SELECT id, name, email, hashed_password FROM users WHERE id=%s"
        cursor.execute(sql, (user_id,))  # (user_id, ) - creating a tuple
        data = cursor.fetchone()
        if data:
            loaded_user = User()
            loaded_user.__id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user.__hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_user_by_name(cursor, user_name):
        sql = "SELECT id, name, email, hashed_password FROM users WHERE name=%s"
        cursor.execute(sql, (user_name,))  # (user_id, ) - creating a tuple
        data = cursor.fetchone()
        if data:
            loaded_user = User()
            loaded_user.__id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user.__hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor):
        sql = "SELECT id, name, email, hashed_password FROM Users"
        ret = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            loaded_user = User()
            loaded_user.__id = row[0]
            loaded_user.username = row[1]
            loaded_user.email = row[2]
            loaded_user.__hashed_password = row[3]
            ret.append(loaded_user)
        return ret

    def delete(self, cursor):
        sql = "DELETE FROM Users WHERE id=%s"
        cursor.execute(sql, (self.__id,))
        self.__id = -1
        return True

if __name__ == '__main__':
    cnx = DatabaseUtils.connect_to_database('workshop_users_db')
    crs = cnx.cursor()


    crs.close()
    print('Cursor closed')
    cnx.close()
    print('Connection closed')