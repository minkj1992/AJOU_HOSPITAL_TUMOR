from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ('128.1.99.43', '127.0.0.1', '192.168.130.166')
STATIC_URL = 'http://128.1.99.43:5555/'

DATABASES = {
    'default': {
        'NAME': 'NSDB_backup',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': '128.1.99.151',
        'USER': 'admin_NS',
        'PASSWORD': 'NSDB2018!@'
    }
}
