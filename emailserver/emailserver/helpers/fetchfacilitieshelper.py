import requests
from emailserver.models import Facility
from io import StringIO


class FetchFacilities:
    stdout: StringIO

    def __init__(self, stdout: StringIO) -> None:
        self.stdout = stdout

    def get_response(self):
        params = {
            "exact": "false",
            "size": "500",
            "fq": ["entity_type:(tour OR timedentry_tour)", "entity_type:ticketfacility"]
        }
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

        response = requests.get("https://www.recreation.gov/api/search", params=params, headers=headers)

        return response.json()

    def get_facilities(self):
        response = self.get_response()

        for facility in response['results']:
            if len(Facility.objects.filter(name=facility['name'])) != 0:
                continue

            matching_id_facilities = Facility.objects.filter(external_reference_id=int(facility['entity_id']))
            if len(matching_id_facilities) != 0:
                old_facility = matching_id_facilities.first()
                self.stdout.write(f'facility {old_facility.external_reference_id} changed names from {old_facility.name} to {facility["name"]}')
                old_facility.delete()

            facility_model = Facility(name=facility['name'], external_reference_id=int(facility["entity_id"]))
            facility_model.save()
