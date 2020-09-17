from django.template.loader import get_template


class AEventManager(object):

    def get_event_functions(self):
        functions = []
        for func in dir(self):
            if 'event_' in func:
                functions.append(getattr(self, func, None))
        return functions


class MailTemplate(object):

    @staticmethod
    def get(key, context=None):
        tpl = get_template('django_solar/mail_templates/%s.html' % key)
        return tpl.render(context)
