from app.settings.base import *

###ENV settings
# SECURITY WARNING: don't run with debug turned on in production!
ENVIRONMENT = 'production'
DEBUG = False

ALLOWED_HOSTS = ["*"]

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://bqdxyyfoegfspe:6c4ad4323fc2f96a0585887cbee265928959c5d7f37106b0f6e2c23942e03f54@ec2-54-204-46-236.compute-1.amazonaws.com:5432/ddbhlgsjjqrm79')}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
WHITENOISE_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'root')
