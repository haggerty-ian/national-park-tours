from django.test import TestCase
from django.core.management import call_command
from emailserver.models import Facility, Tour
from io import StringIO


class TestCommands(TestCase):
    def test_fetch_facilities(self):
        output = StringIO()

        call_command('fetchfacilities', stdout=output)

        self.assertNotEqual(0, len(Facility.objects.all()))
    
    def test_fetch_facilities_prints_when_name_changed(self):
        output = StringIO()

        # TODO: use django stdout attribute in command file to write to stdout in order to correctly capture output for test

        testFacility = Facility(name='testFacility', external_reference_id='300003')
        testFacility.save()

        call_command('fetchfacilities', stdout=output)

        # facility 300003 changed names from testFacility to 

        self.assertIn('facility 300003 changed names from testFacility to ', output.getvalue())
    
    def test_fetch_tours(self):
        testFacility = Facility(name='testFacility', external_reference_id='300003')
        testFacility.save()

        output = StringIO()

        call_command('fetchtours', stdout=output)

        self.assertNotEqual(0, len(Tour.objects.all()))