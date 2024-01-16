# Generated by Django 4.2.6 on 2024-01-16 19:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('emailserver', '0007_tourdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tour',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tourdate',
            name='notification_sent',
            field=models.BooleanField(default=False),
        ),
    ]
