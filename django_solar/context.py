import os
import json
import pkg_resources
from django.conf import settings


try:
    #  Production part
    VERSION = pkg_resources.get_distribution("django_solar").version
except pkg_resources.DistributionNotFound:
    #  Develop part
    with open(os.path.join(settings.BASE_DIR, 'package.json')) as package:
        data = json.load(package)
        VERSION = data['version']


DS_CRON_HOUR = getattr(settings, "DS_CRON_HOUR", 1)
DS_EVENT_MANAGER = getattr(settings, "DS_EVENT_MANAGER", None)
DS_SEND_MAIL = getattr(settings, "DS_SEND_MAIL", True)
DS_SENDER_TEST = getattr(settings, "DS_SENDER_TEST", None)
