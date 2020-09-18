import os
import environ

# Get env

BASE_DIR = os.environ['BASE_DIR']
env = environ.Env()
environ.Env.read_env(BASE_DIR + '/.env')

#  Django Solar Context

DS_CRON_HOUR = 1  # Period of cron in hours
DS_EVENT_MANAGER = "tests.manager.EventManager"  #  Class manager of events
DS_SEND_MAIL = True
DS_SENDER_TEST = 'hello@snoweb.fr'

#  Don't forget to set django email backend
#  Take a look at https://github.com/anymail/django-anymail

ANYMAIL = {
    "MAILJET_API_KEY": env.str('MAILJET_API_KEY'),
    "MAILJET_SECRET_KEY": env.str('MAILJET_SECRET_KEY'),
}
EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
DEFAULT_FROM_EMAIL = "hello@snoweb.fr"
SERVER_EMAIL = "hello@snoweb.fr"
