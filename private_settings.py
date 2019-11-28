
import os

from transfer.settings import BASE_DIR

# DEBUG = True
# THUMBNAIL_DEBUG = True

PUBLIC_FILES_DIR = os.path.dirname(__file__)

STATIC_ROOT = os.path.join(PUBLIC_FILES_DIR, 'static-collection')
MEDIA_ROOT = os.path.join(PUBLIC_FILES_DIR, 'media')
STATICFILES_DIRS = [os.path.join(PUBLIC_FILES_DIR, 'static')]

# ADMINS = MANAGERS = (('Andry', 'o.bogature@gmail.com'), )

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_PORT = 1025
# EMAIL_HOST = 'localhost'
# EMAIL_HOST_USER = 'pmaigutyak@gmail.com'
# EMAIL_HOST_PASSWORD = ''

#
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'serg',
#         'USER': 'root',
#         'PASSWORD': '1',
#         'HOST': '',
#         'PORT': ''
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'bogature$rating2',
#         'USER': 'bogature',
#         'PASSWORD': 'andreandre1',
#         'HOST': 'bogature.mysql.pythonanywhere-services.com',
#     }
# }