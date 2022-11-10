from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FitnessConfig(AppConfig):
    name = "django_cutter.fitness"
    verbose_name = _("fitness")

    def ready(self):
        try:
            import django_cutter.fitness  # noqa F401
        except ImportError:
            pass
