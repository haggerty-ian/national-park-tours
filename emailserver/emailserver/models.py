from django.db import models

class Facility(models.Model):
    name = models.TextField()
    external_reference_id = models.IntegerField()

    def __str__(self):
        return self.name
