from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Create admin user

        user, created = User.objects.get_or_create(
            username='django',
            first_name='User',
            last_name='Admin',
            email='test@test.test',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        if created:
            user.save()
            user.set_password('solar')
            for group in Group.objects.all():
                user.groups.add(group)
            user.save()
