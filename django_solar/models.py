import logging
from datetime import datetime, timedelta
from django.db import models
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from . import context


CRON_MINUTE = context.DS_CRON_HOUR * 60
logger = logging.getLogger('django_solar')


class Notification(models.Model):
    is_send = models.BooleanField(default=False)
    send_at = models.DateTimeField(default=datetime.now)
    event = models.CharField(default='', max_length=100)

    class Meta:
        abstract = True

    @property
    def is_time_to_send(self):
        minutes = CRON_MINUTE / 2
        date_now = datetime.now()
        date_prev = date_now - timedelta(minutes=minutes)
        date_next = date_now + timedelta(hours=minutes)

        logger.debug('\nNow: %s\nAt: %s\nNext: %s\n' % (
            date_prev,
            self.send_at,
            date_next
        ))

        if date_prev < self.send_at < date_next:
            logger.debug('Notification have to be send')
            return True
        logger.debug('Notification is not ready to be send')
        return False

    def send(self):
        self.is_send = True
        self.save()


class Mail(Notification):
    mail = models.EmailField(default=None, null=True)
    subject = models.CharField(default='', max_length=100)
    html = models.TextField(default=None)
    text = models.TextField(default='')
    from_mail = models.CharField(
        default=settings.DEFAULT_FROM_EMAIL,
        max_length=100
    )

    def __str__(self):
        return '%s at %s (%s)' % (
            'Send' if self.is_send else 'Not Send',
            str(self.send_at),
            self.mail
        )

    def send(self):
        if self.is_time_to_send:
            if context.DS_SEND_MAIL:
                msg = EmailMultiAlternatives(
                    self.subject,
                    self.text,
                    self.from_mail,
                    [self.mail if not context.DS_SENDER_TEST else context.DS_SENDER_TEST]
                )
                if self.html:
                    msg.attach_alternative(self.html, "text/html")
                msg.send()
            return super().send()
