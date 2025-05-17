import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fun_with_flags.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Local")


from django.core.wsgi import get_wsgi_application  # noqa: E402


application = get_wsgi_application()
