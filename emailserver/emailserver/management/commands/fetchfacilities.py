from django.core.management.base import BaseCommand
import requests
from emailserver.models import Facility

class Command(BaseCommand):
    help = "Fetches all facilities as defined by the NPS"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        params = {
            "exact": "false",
            "size": "500",
            "fq": ["entity_type:(tour OR timedentry_tour)", "entity_type:ticketfacility", "entity_type:timedentry"]
        }
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

        response = requests.get("https://www.recreation.gov/api/search", params=params, headers=headers)
        for facility in response.json()['results']:
            if len(Facility.objects.filter(name=facility['name'])) != 0:
                continue

            matching_id_facilities = Facility.objects.filter(external_reference_id=int(facility['entity_id']))
            if len(matching_id_facilities) != 0:
                old_facility = matching_id_facilities.first()
                print(f'faciliy {old_facility.external_reference_id} changed names from {old_facility.name} to {facility["name"]}')
                old_facility.delete()

            facility_model = Facility(name=facility['name'], external_reference_id=int(facility["entity_id"]))
            facility_model.save()
