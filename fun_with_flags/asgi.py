import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fun_with_flags.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Local")


from configurations.asgi import get_asgi_application  # noqa: E402

application = get_asgi_application()
