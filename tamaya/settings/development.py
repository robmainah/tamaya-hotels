from .base import *
from django.conf import settings

DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tamaya',
        'USER': 'root',
        'PASSWORD': 'HelloWorld',
        'PORT': '5432',
        'HOST': '127.0.0.1'
    }
}

INTERNAL_IPS = ('127.0.0.1',)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

def show_toolbar(request):
    return True
SHOW_TOOLBAR_CALLBACK = show_toolbar