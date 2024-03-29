from django.core.management.base import BaseCommand
from emailserver.helpers.fetchtourshelper import FetchTours

class Command(BaseCommand):
    help = "Fetches all tours as defined by the NPS"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        FetchTours(stdout=self.stdout).get_tours()

