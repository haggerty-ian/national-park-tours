from django.core.management.base import BaseCommand
from emailserver.helpers.fetchfacilitieshelper import FetchFacilities

class Command(BaseCommand):
    help = "Fetches all facilities as defined by the NPS"
    helper = FetchFacilities()

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.helper.get_facilities()
