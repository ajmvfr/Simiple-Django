"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import socket

from django.core.wsgi import get_wsgi_application

print(f'host name: {socket.gethostname()}')

settings_module = 'core.settings_azure' if 'WEBSITE_HOSTNAME' in os.environ else 'core.settings'

# match PLATFORM:
#     case "Local":
#         settings_module = 'core.settings'


os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
