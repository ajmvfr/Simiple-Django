import os
from .settings import *
from .settings import BASE_DIR

print(f'DigitalOcean settings')

SECRET_KEY = os.environ['SECRET_KEY']
# print('Secret')
# print(f'secret {SECRET_KEY}')
ALLOWED_HOSTS = ['*','.ajmvfr.xyz','.anthonymorgan.xyz','localhost','127.0.0.1','143.244.151.87']
# ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME'],'.ajmvfr.xyz','.anthonymorgan.xyz']
# print(f"website host: {os.environ['WEBSITE_HOSTNAME']}")
# CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME'],'https://*.ajmvfr.xyz','https://*.anthonymorgan.xyz']
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME'],'https://*.ajmvfr.xyz','https://*.anthonymorgan.xyz','https://localhost','http://localhost','https://127.0.0.1','http://143.244.151.87','https://143.244.151.87']
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


# print(f'NAME {os.environ['DB_NAME']}')
# print(f'HOST {os.environ['DB_HOST']}')
# print(f'USER {os.environ['DB_USER']}')
# print(f'PASSWORD {os.environ['DB_PASSWORD']}')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'HOST': os.environ['DB_HOST'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'PORT': '',
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True 
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

PREPEND_WWW = True

# CORS_REPLACE_HTTPS_REFERER      = False
# HOST_SCHEME                     = "http://"
# SECURE_PROXY_SSL_HEADER         = None
# SECURE_SSL_REDIRECT             = False
# SESSION_COOKIE_SECURE           = False
# CSRF_COOKIE_SECURE              = False
# SECURE_HSTS_SECONDS             = None
# SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
# SECURE_FRAME_DENY               = False