from django.db import models
from django.utils import timezone


class Facility(models.Model):
    name = models.TextField(unique=True)
    external_reference_id = models.IntegerField(unique=True)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
    

class Tour(models.Model):
    name = models.TextField()
    external_reference_id = models.IntegerField(unique=True)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class TourDate(models.Model):
    date = models.DateField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    notification_sent = models.BooleanField(default=False)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)


class UserEmail(models.Model):
    email = models.EmailField(unique=True)


class MonitorWindow(models.Model):
    email = models.ForeignKey(UserEmail, on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True)
    date_added = models.DateField(default=timezone.now)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
        
