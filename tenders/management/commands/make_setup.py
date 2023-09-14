from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import call_command


class Command(BaseCommand):
    help = "Run makemigrations, migrate, and create a superuser"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Running makemigrations..."))
        call_command("makemigrations")

        self.stdout.write(self.style.SUCCESS("Running migrations..."))
        call_command("migrate")

        username = "demo"
        password = "demo"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, password=password)
            self.stdout.write(self.style.SUCCESS(f"Successfully created superuser: {username}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser already exists: {username}"))
