# Generated by Django 5.0.6 on 2024-06-15 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0002_alter_booking_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Appointment',
        ),
    ]