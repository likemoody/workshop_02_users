import logging

logger = logging.getLogger('kewiany_commons')
logging.basicConfig(level=logging.INFO)
description = '''Communication app. Please see help: -h'''

if __name__ == "__main__":
    # from Active_Records.controllers.mak_users_app import *
    # users_app(description, 'workshop_users')  # users app

    from Active_Records.controllers.mak_messages_app import *
    messages_app(description, 'workshop_users')  # messages app


