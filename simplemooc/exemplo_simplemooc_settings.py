SECRET_KEY = 'lahflahfhlkahfalfalfkhff'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dadasdad',
        'USER': 'sasasa',
        'PASSWORD': 'sasasa',
        'HOST': 'x.x.x.x',
        'PORT': '5432',
    }
}

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'Nome <xxxx@gmail.com>'
#EMAIL_USE_TLS = False
#EMAIL_USE_SSL = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'xxxx@gmail.com'
#EMAIL_HOST_PASSWORD = 'xxxx'
#EMAIL_PORT = 587

CONTACT_EMAIL = 'gilcimar.dallo@gmail.com'
