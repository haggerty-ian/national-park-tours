# Generated by Django 4.2.6 on 2024-01-16 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailserver', '0008_facility_date_added_tour_date_added_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitorwindow',
            name='facility',
        ),
    ]