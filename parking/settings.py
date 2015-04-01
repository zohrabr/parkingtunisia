"""
Django settings for parking project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2k_ic-t@-s9d_at*^fgr3e0_g&0ykb)%19ajvrk$ni+lmnz$^x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
SETTINGS_DIR=os.path.dirname(__file__)
PROJECT_PATH=os.path.join(SETTINGS_DIR,os.pardir)
PROJECT_PATH=os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH=os.path.join(PROJECT_PATH,'template')
ALLOWED_HOSTS = ['parkingtunisie.olympe.in']
TEMPLATE_DIRS=(
	TEMPLATE_PATH, 
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',                              #new ligne
    'django.contrib.staticfiles',
    'car',
    'geoposition',
    'allauth',                      #new ligne
    'widget_tweaks',
)

SITE_ID = 1 #new ligne auth
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'parking.urls'

WSGI_APPLICATION = 'parking.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES_PATH=os.path.join(PROJECT_PATH,'parking.db')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASES_PATH ,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL='/car/login/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_PATH=os.path.join(PROJECT_PATH,'static')
STATIC_URL = '/static/'
STATICFILES_DIRS=(
	STATIC_PATH ,
)
