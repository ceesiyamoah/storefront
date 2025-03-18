from storefront.settings.common import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!b4+dy=ry#wazguo6_x#p0d*!cb*-qz7fqoxpsty!m+n5v2i&0'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'P@ssword'

    }
}
