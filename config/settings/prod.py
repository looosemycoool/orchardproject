import environ

from .base import *

ALLOWED_HOSTS = ['43.200.128.160', 'gwasuwon.kr']
STATIC_ROOT = BASE_DIR / 'orchard/static/'
STATICFILES_DIRS = []
DEBUG = True

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }
}