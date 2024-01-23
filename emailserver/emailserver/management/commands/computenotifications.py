from django.core.management.base import BaseCommand
from emailserver.helpers.computenotificationshelper import ComputeNotifications

class Command(BaseCommand):
    help = "Fetches all facilities as defined by the NPS"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        ComputeNotifications(stdout=self.stdout).compute_notifications()
