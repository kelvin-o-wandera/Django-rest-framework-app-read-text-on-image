import os
import dj_database_url
from django.conf import settings
from datetime import date, timedelta
from django.utils.translation import ugettext_lazy as _
from django.contrib.messages import constants as messages
# from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# with open('/secret_key.txt') as f:
#     SECRET_KEY = f.read().strip()

# SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = 'rro^$^1n+t3zbnb)1*m=#0y+pi+sf@h440&&5m!g=qcjanpni1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SENDGRID_API_KEY = "*"

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'storages',
    'clone',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:8000',
    }
}

USER_AGENTS_CACHE = 'default'

SESSION_COOKIE_AGE = 3600

SESSION_SAVE_EVERY_REQUEST = True

PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ROOT_URLCONF = 'main.urls'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `nopassword`
    'django.contrib.auth.backends.ModelBackend',
)


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

if not DEBUG:
    # if os.environ.get('DATABASE_URL'):
    #     DATABASES['default'] = dj_database_url.config(default=os.environ['DATABASE_URL'])
    # DATABASES = {'default': dj_database_url.config(default='postgres://user:pass@localhost/dbname')}
    DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}
else:
    DATABASES = {
        'default': {
                    'ENGINE': 'django.db.backends.postgresql_psycopg2',
                    'NAME': 'dbname',
                    'USER': 'postgres',
                    'PASSWORD': 'dbpassword',
                    'PORT': '5432',
                    'HOST': 'localhost'
                },
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "assets", "static_cdn")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "assets", "our_static"),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "assets", "media_cdn")


if not DEBUG:
    DEFAULT_FILE_STORAGE = 'main.storage.CustomS3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_DEFAULT_ACL = 'public-read'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', 'change me')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', 'change me')
    AWS_AUTO_CREATE_BUCKET = True
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', 'change me')
    AWS_QUERYSTRING_AUTH = False

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
      'rest_framework.renderers.JSONRenderer',
      'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    "SEARCH_PARAM": "q",
    'DEFAULT_PAGINATION_CLASS': 'main.pagination.PageNumberPaginationDataOnly',
    'PAGE_SIZE': 10,
}

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'rest_auth.serializers.LoginSerializer',
    'TOKEN_SERIALIZER': 'rest_auth.serializers.TokenSerializer',
    'REST_USE_JWT': True,
    'JWT_SERIALIZER': 'rest_auth.serializers.JWTSerializer',
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.UserSerializer',
    # 'USER_DETAILS_SERIALIZER': 'rest_auth.serializers.UserDetailsSerializer',
    'PASSWORD_RESET_SERIALIZER': 'rest_auth.serializers.PasswordResetSerializer',
    'PASSWORD_RESET_CONFIRM_SERIALIZER': 'rest_auth.serializers.PasswordResetConfirmSerializer',
    'PASSWORD_CHANGE_SERIALIZER': 'rest_auth.serializers.PasswordChangeSerializer',
}


API_KEY = os.environ.get('API_KEY', 'change me')
