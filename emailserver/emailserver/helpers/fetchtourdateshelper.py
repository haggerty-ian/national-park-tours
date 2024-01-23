
from emailserver.models import Facility, Tour, TourDate
from io import StringIO
from datetime import date
import requests


class FetchTourDates:
    stdout: StringIO

    def __init__(self, stdout: StringIO) -> None:
        self.stdout = stdout

    def get_response(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        return response

    def get_tour_dates(self):
        # TODO: use all facilities
        matching_id_facilities = Facility.objects.filter(external_reference_id=234640)

        for facility in matching_id_facilities:
            tour_dates_url_builder = lambda month, year: f"https://www.recreation.gov/api/ticket/availability/facility/{facility.external_reference_id}/monthlyAvailabilitySummaryView?year={year}&month={month}&inventoryBucket=FIT"
            max_months_out = 6

            for i in range(max_months_out + 1):
                now: date = date.today()
                target_month = ((now.month + (i - 1)) % 12) + 1
                target_year = now.year + ((now.month + (i - 1)) // 12)
                
                tour_date_url = tour_dates_url_builder(target_month, target_year)
                response = self.get_response(tour_date_url)

                if response.status_code != 200:
                    print(f'got error response when requesting tour dates for {facility.external_reference_id} {facility.name} year = {target_year} month = {target_month}')
                    break

                print(response.json())
                # facility_availability_summary_view_by_local_date

                TourDate.objects.all().delete()
                for tour_date, facility_data in response.json()['facility_availability_summary_view_by_local_date']:
                    if facility_data['availability_level'] == 'NA':
                        continue

                    for tour_id, tour_data in facility_data['tour_availability_summary_view_by_tour_id']:
                        if tour_data['availability_level'] == 'NA':
                            continue

                        matching_id_tours = Tour.objects.filter(external_reference_id=tour_id)
                        if len(matching_id_tours) == 0:
                            print(f'could not find referenced tour id {tour_id} for facility {facility.name} {facility.external_reference_id}')
                            continue

                        tour = matching_id_tours[0]

                        # maybe user has associated table of notified dates
                        new_date = TourDate(date=date.fromisoformat(tour_date), facility=facility, tour=tour)
                        new_date.save()
