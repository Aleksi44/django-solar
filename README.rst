************
Django Solar
************

.. image:: https://img.shields.io/pypi/v/django_solar
    :target: https://pypi.org/project/django_solar/

.. image:: https://img.shields.io/pypi/pyversions/django_solar
    :target: https://pypi.org/project/django_solar/

Django email automation with cron.

Tested with :

- django==3.0.9

Setup
#####

Install with pip :
::

    pip install django_solar


Add django_solar to django apps installed :
::

    INSTALLED_APPS = [
        ...
        'django_solar',
    ]


Set Django email backend :
::

    # Take a look at https://github.com/anymail/django-anymail

    ANYMAIL = {
        "MAILJET_API_KEY": env.str('MAILJET_API_KEY'),
        "MAILJET_SECRET_KEY": env.str('MAILJET_SECRET_KEY'),
    }
    MAILJET_API_KEY = env.str('MAILJET_API_KEY')
    MAILJET_SECRET_KEY = env.str('MAILJET_SECRET_KEY')

    EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
    DEFAULT_FROM_EMAIL = "hello@snoweb.fr"
    SERVER_EMAIL = "hello@snoweb.fr"


Set django_solar context :
::

    DS_CRON_HOUR = 1  # Period of cron in hours
    DS_EVENT_MANAGER = "tests.manager.EventManager"  #  Class manager of events


Set cron command
::

    0 * * * * python manage.py solar




Defines Events
##############

Example of EventManger :
::

    from django_solar import AEventManager, MailTemplate
    from django_solar.models import Mail
    from datetime import datetime


    class EventManager(AEventManager):

        def event_something(self):
            Mail.objects.create(
                mail='test@exemple.com',  #  Receiver
                send_at=datetime.now(),  #  Datetime send
                html=MailTemplate.get(key='test'),  #  HTML of email
                subject="Test Django Solar"  #  Subject of email
            )
