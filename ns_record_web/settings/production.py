from .base import *

DATABASES = {
    'default': {
        'NAME': 'NSDB',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': '128.1.99.151',
        'USER': 'admin_NS',
        'PASSWORD': 'NSDB2018!@'
    }
}
