from django.core.mail import send_mail
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Sends a test email"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        send_mail("Test Message", "Hello, World", "ijhaggerty@sep.com", ["ijhaggerty@sep.com"], fail_silently=False)
