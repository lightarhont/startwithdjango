"""
Django settings for startwithdjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'filters': {
'require_debug_false': {
'()': 'django.utils.log.RequireDebugFalse'
},
'require_debug_true': {
'()': 'django.utils.log.RequireDebugTrue'
}
},
'formatters': {
'main_formatter': {
'format': '%(levelname)s:%(name)s: %(message)s '
'(%(asctime)s; %(filename)s:%(lineno)d)',
'datefmt': "%Y-%m-%d %H:%M:%S",
},
},
'handlers': {
'mail_admins': {
'level': 'ERROR',
'filters': ['require_debug_false'],
'class': 'django.utils.log.AdminEmailHandler'
},
'console':{
'level': 'DEBUG',
'filters': ['require_debug_true'],
'class': 'logging.StreamHandler',
'formatter': 'main_formatter',
},
'production_file':{
'level' : 'INFO',
'class' : 'logging.handlers.RotatingFileHandler',
'filename' : 'logs/main.log',
'maxBytes': 1024*1024*5, # 5 MB
'backupCount' : 7,
'formatter': 'main_formatter',
'filters': ['require_debug_false'],
},
'debug_file':{
'level' : 'DEBUG',
'class' : 'logging.handlers.RotatingFileHandler',
'filename' : 'logs/main_debug.log',
'maxBytes': 1024*1024*5, # 5 MB
'backupCount' : 7,
'formatter': 'main_formatter',
'filters': ['require_debug_true'],
},
'null': {
"class": 'django.utils.log.NullHandler',
}
},
'loggers': {
'django.request': {
'handlers': ['mail_admins', 'console'],
'level': 'ERROR',
'propagate': True,
},
'django': {
'handlers': ['null', ],
},
'py.warnings': {
'handlers': ['null', ],
},
'': {
'handlers': ['console', 'production_file', 'debug_file'],
'level': "DEBUG",
},
}
} 

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z3$p6yx3lis35q_)ieiwxa!z*c3mc#p1y8$!f8rfa@)%_lds4l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    '/mnt/webserver/pythonproject/startwithdjango/startwithdjango/tpls',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'profiles'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'startwithdjango.urls'

WSGI_APPLICATION = 'startwithdjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {'default': {'ENGINE': 'mysql.connector.django',
'NAME': 'swd',
'USER': 'swd',
'PASSWORD': 'speed1',
'HOST': 'localhost', }}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
STATIC_URL = '/assets/'
MEDIA_URL = '/assets/media/'

STATICFILES_DIRS = (
    ('css', os.path.join(STATIC_ROOT, 'css')),
    ('images', os.path.join(STATIC_ROOT, 'images')),
    ('js', os.path.join(STATIC_ROOT, 'js')),
    ('lib', os.path.join(STATIC_ROOT, 'lib')),
    ('media', MEDIA_ROOT),
)
