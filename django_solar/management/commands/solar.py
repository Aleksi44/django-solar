import importlib
from django.core.management.base import BaseCommand
from django_solar.models import Mail
from django_solar import context


def import_from_string(val):
    """
    Attempt to import a class from a string representation.
    From: django-rest-framework
    """
    try:
        # Nod to tastypie's use of importlib.
        parts = val.split('.')
        module_path, class_name = '.'.join(parts[:-1]), parts[-1]
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except ImportError as e:
        msg = "Could not import '%s' for setting. %s: %s." % (
            val, e.__class__.__name__, e
        )
        raise ImportError(msg)


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Manage Event
        if context.DS_EVENT_MANAGER:
            manager = import_from_string(context.DS_EVENT_MANAGER)()
            for event_function in manager.get_event_functions():
                event_function()

        #  Send Email Notifications
        emails = Mail.objects.filter(is_send=False)
        for email in emails:
            email.send()
