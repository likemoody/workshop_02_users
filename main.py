import logging
from Active_Records.controllers.mak_users_app import *

logger = logging.getLogger('kewiany_commons')
logging.basicConfig(level=logging.INFO)
description = '''Communication app. Please see help: -h'''

if __name__ == "__main__":
    users_app(description, 'workshop_users')  # users app
    # messages_app(description, 'workshop_users')  # messages app
