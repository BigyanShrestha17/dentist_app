from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.name} - {self.appointment_date} {self.appointment_time}'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.subject}'
