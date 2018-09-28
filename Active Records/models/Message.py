from utils import *

class Message:
    def __init__(self):
        self.__id = -1
        self.from_id = ""
        self.to_id = ""
        self.message_content = ""
        self.creation_date = ""

    @property
    def id(self):
        return self.__id

    def save_to_db(self, cursor):
        if self.__id == -1:
            sql = """INSERT INTO Messages(from_id, to_id, message_content, creation_date) VALUES(%s, %s, %s) RETURNING id"""
            values = (self.from_id, self.to_id, self.message_content, self.creation_date)
            cursor.execute(sql, values)
            self.__id = cursor.fetchone()[0]  # or cursor.fetchone()['id']
            return True
        else:
            sql = """UPDATE Messages SET from_id=%s, to_id=%s, message_content=%s WHERE id=%s"""
            values = (self.from_id, self.to_id, self.message_content, self.creation_date, self.id)
            cursor.execute(sql, values)
            return True

    @staticmethod
    def load_sent_message(cursor, to_id):
        sql = "SELECT message_content FROM Messages WHERE to_id={};".format(to_id)
        cursor.execute(sql, (to_id,))
        data = cursor.fetchone()
        if data:
            loaded_message = Message()
            loaded_message.__id = data[0]
            loaded_message.from_id = data[1]
            loaded_message.to_id = data[2]
            loaded_message.message_content = data[3]
            loaded_message.creation_date = data[4]
            return loaded_message
        else:
            return None

    @staticmethod
    def load_all_sent_messages(cursor, to_id):
        sql = "SELECT message_content FROM Messages WHERE to_id={};".format(to_id)
        ret = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            loaded_message = Message()
            loaded_message.__id = row[0]
            loaded_message.from_id = row[1]
            loaded_message.to_id = row[2]
            loaded_message.text = row[3]
            loaded_message.creation_date = row[4]
            ret.append(loaded_message)
        return ret

    def delete(self, cursor):
        sql = "DELETE FROM Messages WHERE id=%s"
        cursor.execute(sql, (self.__id,))
        self.__id = -1


if __name__ == '__main__':
    cnx = DatabaseUtils.connect_to_database('workshop_users_db')
    crs = cnx.cursor()


    crs.close()
    print('Cursor closed')
    cnx.close()
    print('Connection closed')