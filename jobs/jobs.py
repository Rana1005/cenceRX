from django.conf import settings
from apt.models import AppointmentModel
from datetime import datetime, timedelta
from apt.services import send_sms

def schedule_task():
    date_format = '%Y-%m-%d %H:%M:%S'
    current_time = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), date_format)
    remainder_time = current_time + timedelta(minutes= 30)
    appointment_data = list(AppointmentModel.objects.filter(date_time__lte = remainder_time, is_reminder_sent=False))
    print("appointment data is", appointment_data)
    for appointment_obj in appointment_data:
        user_name = appointment_obj.user_name
        phone = appointment_obj.phone
        date_time = appointment_obj.date_time
        send_sms(user_name,phone, date_time, 1)
        appointment_obj.is_reminder_sent = True
        print("Remainder sent")
        appointment_obj.save()
        
    print("hy task schedule", remainder_time)