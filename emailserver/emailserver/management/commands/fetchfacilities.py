from django.core.management.base import BaseCommand, CommandError
import requests

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

        # response = requests.get("https://www.recreation.gov/api/search", params)
        response = requests.get("https://www.recreation.gov/api/search", params=params, headers=headers)
        # name, id, parent_id, entity_id


