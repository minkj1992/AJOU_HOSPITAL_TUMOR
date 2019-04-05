from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'NAME': 'NS_DEV',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'localhost'

    }
}

# CommandError: You appear not to have the 'sqlite3' program installed or on your path.
# DATABASES = {
#     'default': {
#         'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
#         'ENGINE': 'django.db.backends.sqlite3',
#         # 'HOST': 'localhost'
#     }
# }