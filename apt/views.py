from django.shortcuts import render
from rest_framework.views import APIView
from .models import AppointmentModel
from rest_framework.response import Response
from .serializers import AppointmentSerializer
from .services import send_sms
from datetime import datetime

# Create your views here.
class AppointmentView(APIView):
    def post(self, request):
        date_format = '%Y-%m-%d %H:%M:%S'
        date_time = request.data['date_time']
        appointment_time = datetime.strptime(date_time,date_format)
        current_time = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), date_format)
        if appointment_time < current_time:
            return Response({
            "status":200,
            "message":"Appointment can not be booked for past date"
        })

        data = request.data
        serializer = AppointmentSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        username = request.data['user_name']
        
        phone = request.data['phone']


        print("Datetime from timestamp:", date_time)
        print("Datetime from current_time:", type(current_time))
        send_sms(username, phone, date_time,0)
        return Response({
            "status":200,
            "message":"Appointment booked successfully"
        })