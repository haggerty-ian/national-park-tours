from django.test import TestCase
from unittest import mock
from emailserver.models import Facility
from emailserver.helpers.fetchfacilitieshelper import FetchFacilities
from io import StringIO
import json

test_response = json.loads("{\r\n    \"results\": [\r\n        {\r\n            \"aggregate_cell_coverage\": 3.5426356589147288,\r\n            \"average_rating\": 4.6934867,\r\n            \"campsite_type_of_use\": [\r\n                \"na\"\r\n            ],\r\n            \"description\": \"From the sweet little farm at the foot of Penn\u2019s Hill to the gentleman\u2019s country estate at Peace field, Adams National Historical Park is the story of \u201Cheroes, statesman, philosophers \u2026 and learned women\u201D whose ideas and actions helped to transform thirteen disparate colonies into one united nation.\",\r\n            \"entity_id\": \"300003\",\r\n            \"entity_type\": \"ticketfacility\",\r\n            \"go_live_date\": \"2019-07-10T10:00:00Z\",\r\n            \"html_description\": \"From the sweet little farm at the foot of Penn\u2019s Hill to the gentleman\u2019s country estate at Peace field, Adams National Historical Park is the story of \u201Cheroes, statesman, philosophers \u2026 and learned women\u201D whose ideas and actions helped to transform thirteen disparate colonies into one united nation.\",\r\n            \"id\": \"300003_ticketfacility\",\r\n            \"latitude\": \"42.25160200000000\",\r\n            \"longitude\": \"-71.00312000000000\",\r\n            \"name\": \"Adams National Historical Park Tours\",\r\n            \"number_of_ratings\": 261,\r\n            \"org_id\": \"128\",\r\n            \"org_name\": \"National Park Service\",\r\n            \"parent_id\": \"2555\",\r\n            \"parent_name\": \"Adams National Historical Park\",\r\n            \"parent_type\": \"recarea\",\r\n            \"preview_image_url\": \"https:\/\/cdn.recreation.gov\/public\/2019\/07\/02\/18\/37\/300003_cc986007-4e7e-49f7-8a6c-5f6b28e4937f_700.jpg\",\r\n            \"reservable\": true,\r\n            \"time_zone\": \"America\/New_York\",\r\n            \"tours_count\": \"1\"\r\n        },\r\n        {\r\n            \"aggregate_cell_coverage\": 2.129153610695866,\r\n            \"average_rating\": 4.766667,\r\n            \"campsite_type_of_use\": [\r\n                \"na\"\r\n            ],\r\n            \"description\": \"African Burial Ground, which is a sacred space in lower Manhattan, is the oldest and largest known excavated burial ground in North America for both freed and enslaved Africans. It protects the historic role slavery played in building New York. \\n The African Burial Ground is widely acknowledged as one of America\u2019s most significant archeological finds of the 20th century. Learn about this once forgotten piece of New York history and how the rediscovery of the burial ground united a community committed to honoring, preserving, and teaching this important history to generations that follow. \\n\",\r\n            \"entity_id\": \"10089005\",\r\n            \"entity_type\": \"ticketfacility\",\r\n            \"go_live_date\": \"2022-04-26T19:47:25.707567Z\",\r\n            \"html_description\": \"<p>African Burial Ground, which is a sacred space in lower Manhattan, is the oldest and largest known excavated burial ground in North America for both freed and enslaved Africans. It protects the historic role slavery played in building New York.<\/p>\\n<p>The African Burial Ground is widely acknowledged as one of America\u2019s most significant archeological finds of the 20th century. Learn about this once forgotten piece of New York history and how the rediscovery of the burial ground united a community committed to honoring, preserving, and teaching this important history to generations that follow.<\/p>\\n\",\r\n            \"id\": \"10089005_ticketfacility\",\r\n            \"latitude\": \"40.71490000000000\",\r\n            \"longitude\": \"-74.00560000000000\",\r\n            \"name\": \"African Burial Ground National Monument Tours\",\r\n            \"number_of_ratings\": 30,\r\n            \"org_id\": \"128\",\r\n            \"org_name\": \"National Park Service\",\r\n            \"parent_id\": \"13906\",\r\n            \"parent_name\": \"African Burial Ground National Monument\",\r\n            \"parent_type\": \"recarea\",\r\n            \"preview_image_url\": \"https:\/\/cdn.recreation.gov\/public\/2022\/04\/27\/16\/10\/10089005_3e5827a3-16ec-441a-a0fb-c293414c834d_700.jpg\",\r\n            \"reservable\": true,\r\n            \"time_zone\": \"America\/New_York\",\r\n            \"tours_count\": \"4\"\r\n        }\r\n]\r\n}")

class FetchFacilitiesTestCase(TestCase):
    command = FetchFacilities(StringIO())

    def setUp(self):
        pass

    def test_database_is_modified_by_web_response(self):
        self.command.get_response = mock.MagicMock(return_value=test_response)

        self.command.get_facilities()

        self.assertEqual(2, len(Facility.objects.all()))

    def test_database_contains_facilities_from_web_response(self):
        self.command.get_response = mock.MagicMock(return_value=test_response)

        self.command.get_facilities()

        first_result = Facility.objects.filter(external_reference_id="300003")
        second_result = Facility.objects.filter(external_reference_id="10089005")

        self.assertEqual(1, len(first_result))
        self.assertEqual(1, len(second_result))