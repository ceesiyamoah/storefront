import os
from storefront.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = []
