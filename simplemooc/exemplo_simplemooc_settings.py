SECRET_KEY = 'f_vum-+l9gvj3q*7ubr4d2dvsu+qw@z)msj#7o8*a8sv_cm)-x'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'simplemooc',
        'USER': 'root',
        'PASSWORD': 'cacaverde',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'Gilcimar dalló <dallo.gilcimar@gmail.com>'
#EMAIL_USE_TLS = False
#EMAIL_USE_SSL = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'dallo.gilcimar@gmail.com'
#EMAIL_HOST_PASSWORD = 'xxxx'
#EMAIL_PORT = 587

CONTACT_EMAIL = 'gilcimar.dallo@gmail.com'
