from django.core.management.base import BaseCommand
from helpers.fetchtourshelper import FetchTours

class Command(BaseCommand):
    help = "Fetches all tours as defined by the NPS"
    helper = FetchTours()

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.helper.get_tours()

