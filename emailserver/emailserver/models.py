from django.db import models

class Facility(models.Model):
    name = models.TextField
    tour_lookup_id = models.IntegerField
    schedule_lookup_id = models.IntegerField

    def __str__(self):
        return self.name
