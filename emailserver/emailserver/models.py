from django.db import models

class Facility(models.Model):
    name = models.TextField(unique=True)
    external_reference_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Tour(models.Model):
    name = models.TextField()
    external_reference_id = models.IntegerField(unique=True)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class TimeSlot(models.Model):
#     time = models.DateTimeField()
#     tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
#     facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

class Monitor(models.Model):
    email = models.EmailField()
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
