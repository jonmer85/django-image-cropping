import os
import sys
import logging
import django.template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
SECRET_KEY = '0pfuvtvasdlkjasd76723"b)lna4*f_-xxkszs4##!+wpo'

ROOT_URLCONF = 'example.urls'

IMAGE_CROPPING_JQUERY_URL = 'js/jquery.min.js'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

if django.VERSION[:2] >= (1, 7):
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'easy_thumbnails',
    'image_cropping',
    'example',
]


if django.VERSION[:2] < (1, 6):
    TEST_RUNNER = 'discover_runner.DiscoverRunner'
else:
    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

from easy_thumbnails.conf import settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

try:
    import django_extensions
except ImportError:
    pass
else:
    INSTALLED_APPS += ['django_extensions']

# disable logging while testing
if len(sys.argv) > 1 and sys.argv[1] == 'test':
    logging.disable(logging.CRITICAL)

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        },
    }

IMAGE_CROPPING_THUMB_SIZE = (300, 300)
