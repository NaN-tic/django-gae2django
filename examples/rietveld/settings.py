# Django settings for django_gae2django project.

# NOTE: Keep the settings.py in examples directories in sync with this one!

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev.db',                       # Or path to database file if using sqlite3.
        'USER': '',                             # Not used with sqlite3.
        'PASSWORD': '',                         # Not used with sqlite3.
        'HOST': '',                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
        }
    }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# Absolute path to the directory that holds django static files.
# Example: "/home/media/media.lawrence.com/"
STATIC_ROOT = ''

# URL prefix for django static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'el@4s$*(idwm5-87teftxlksckmy8$tyo7(tm!n-5x)zeuheex'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'gae2django.middleware.FixRequestUserMiddleware',
    # Keep in mind, that CSRF protection is DISABLED in this example!
    'rietveld_helper.middleware.DisableCSRFMiddleware',
    'rietveld_helper.middleware.AddUserToRequestMiddleware',
    'codereview.middleware.AddHSTSHeaderMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',    # required by admin panel
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'rietveld_helper.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'gae2django',
    'rietveld_helper',
    'codereview',
)

AUTH_PROFILE_MODULE = 'codereview.Account'
LOGIN_REDIRECT_URL = '/'

# This won't work with gae2django.
RIETVELD_INCOMING_MAIL_ADDRESS = None

RIETVELD_REVISION = 'a2d5c409a0ee'

# Default values for patch rendering
DEFAULT_CONTEXT = 10
DEFAULT_COLUMN_WIDTH = 80
MIN_COLUMN_WIDTH = 3
MAX_COLUMN_WIDTH = 2000
HSTS_MAX_AGE = 60*60*24*365  # 1 year in seconds.

UPLOAD_PY_SOURCE = os.path.join(os.path.dirname(__file__), 'upload.py')
