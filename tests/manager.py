from django_solar import AEventManager, MailTemplate
from django_solar.models import Mail
from datetime import datetime


class EventManager(AEventManager):

    def event_something(self):
        Mail.objects.create(
            mail='test@exemple.com',  #  Receiver
            send_at=datetime.now(),  #  Datetime send
            html=MailTemplate.get(key='test'),  #  HTML of email
            subject="Test Django Solar",  #  Subject of email
            event="something"
        )
