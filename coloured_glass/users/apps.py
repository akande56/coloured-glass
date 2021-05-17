from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "coloured_glass.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import coloured_glass.users.signals  # noqa F401
        except ImportError:
            pass
