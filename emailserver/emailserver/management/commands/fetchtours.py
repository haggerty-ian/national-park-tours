from django.core.management.base import BaseCommand
import requests
from emailserver.models import Facility, Tour

class Command(BaseCommand):
    help = "Fetches all facilities as defined by the NPS"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        
        for facility in Facility.objects.all():
            tours_url = f"https://www.recreation.gov/api/ticket/facility/{facility.external_reference_id}/tour"
            response = requests.get(tours_url, headers=headers)

            if response.status_code != 200:
                print(f'got error response when requesting tours for {facility.external_reference_id} {facility.name}')
                continue

            for tour in response.json():
                print(tour['tour_id'])

