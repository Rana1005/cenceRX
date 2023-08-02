from django.db import models

class AppointmentModel(models.Model):
    user_name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    phone = models.CharField(max_length=12)
    is_reminder_sent = models.BooleanField(default=False)