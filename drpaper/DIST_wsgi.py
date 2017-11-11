"""
WSGI config for drpaper project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

from os import environ
from os.path import expanduser
from sys import path
from site import addsitedir

addsitedir('/PATH/TO/drpaper/venv_drpaper/lib/python3.4/site-packages')

path.append('/PATH/TO/drpaper/www')
path.append('/PATH/TO/drpaper/www/drpaper')

activate_env = expanduser('/PATH/TO/drpaper/venv_drpaper/bin/activate_this.py')
exec(compile(open(activate_env, 'rb').read(), activate_env, 'exec'),
     dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application  # NOQA

environ.setdefault("DJANGO_SETTINGS_MODULE", "drpaper.settings")
application = get_wsgi_application()
