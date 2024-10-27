import os
from .settings import *
from .settings import BASE_DIR

print(f'Azure settings')

SECRET_KEY = os.environ['SECRET_KEY']
# ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME'],'.ajmvfr.xyz','.anthonymorgan.xyz']
# print(f"website host: {os.environ['WEBSITE_HOSTNAME']}")
# CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME'],'https://*.ajmvfr.xyz','https://*.anthonymorgan.xyz']
DEBUG = True


# digital ocean 
# https://docs.digitalocean.com/products/app-platform/how-to/use-environment-variables/#component-specific-variables
# APP_DOMAIN

# WhiteNoise configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] 

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': conn_str_params['dbname'],
        'HOST': conn_str_params['host'],
        'USER': conn_str_params['user'],
        'PASSWORD': conn_str_params['password'],
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURE_HSTS_SECONDS = 31536000 # 1 year
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# PREPEND_WWW = True