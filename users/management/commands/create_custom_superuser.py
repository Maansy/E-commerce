from django.core.management.base import BaseCommand
from users.models import User  # Import your custom User model here

class Command(BaseCommand):
    help = 'Create a superuser for the custom User model'

    def handle(self, *args, **options):
        email = input('Enter email address: ')
        password = input('Enter password: ')

        User.objects.create_superuser(email=email, password=password)
        self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
