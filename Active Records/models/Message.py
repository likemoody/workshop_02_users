from validator import *
from utils import *

class Message:
    def __init__(self, id, form_id, to_id, text, creation_date):
        self.id = Validator.validate_is_int(self, id)
        self.form_id = Validator.validate_is_int(self, form_id)
        self.to_id = Validator.validate_is_int(self, to_id)
        self.text = Validator.validate_is_str(self, text)
        self.creation_date = creation_date  # date validity check needed considering table's column data type it is used in



if __name__ == '__main__':
    cnx = DatabaseUtils.connect_to_database('workshop_users')
    cursor = cnx.cursor()

    cursor.close()
    print('Cursor closed')
    cnx.close()
    print('Connection closed')