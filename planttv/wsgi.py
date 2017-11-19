"""
WSGI config for planttv project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import logging
import os

from dj_static import Cling

from django.core.wsgi import get_wsgi_application

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planttv.settings")

application = get_wsgi_application()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "path.to.settings.py")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)-8s %(message)s")
