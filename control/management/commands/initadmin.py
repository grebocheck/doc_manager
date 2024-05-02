from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin = User.objects.create_superuser(email=None, username="admin", password="admin")
        admin.is_active = True
        admin.is_admin = True
        admin.save()