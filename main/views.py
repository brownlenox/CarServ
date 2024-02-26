from django.shortcuts import render, redirect
from .models import Booking
from django.contrib import messages
from django.core.mail import send_mail
from CarRepair import settings
import smtplib
import os


def index(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        service = request.POST.get('service')
        service_date = request.POST.get('service_date')
        special_request = request.POST.get('special_request', '')

        booking = Booking.objects.create(
            user_name=user_name,
            user_email=user_email,
            service=service,
            service_date=service_date,
            special_request=special_request
        )

        messages.success(request, 'Booking has been done succesfully. See you soon.')


        return redirect('index')

    return render(request, 'index.html')

def about(request):
    return render(request, "about.html")

def booking(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        service = request.POST.get('service')
        service_date = request.POST.get('service_date')
        special_request = request.POST.get('special_request', '')

        booking = Booking.objects.create(
            user_name=user_name,
            user_email=user_email,
            service=service,
            service_date=service_date,
            special_request=special_request
        )

        messages.success(request, 'Booking has been done succesfully. See you soon.')


        return redirect('booking')

    return render(request, 'booking.html')

def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        service = request.POST.get('service')
        service_date = request.POST.get('service_date')
        special_request = request.POST.get('special_request', '')

        booking = Booking.objects.create(
            user_name=user_name,
            user_email=user_email,
            service=service,
            service_date=service_date,
            special_request=special_request
        )

        from_email = os.environ.get('EMAIL_HOST_USER')

        message = f"New booking information:\n\nUser Name: {user_name}\nEmail: {user_email}\nService: {service}\nService Date: {service_date}\nSpecial Request: {special_request}"

        send_mail(
            subject='New Booking Notification',
            message=message,
            from_email=from_email,
            recipient_list=['Cleaniq1@gmail.com'],
            fail_silently=True
        )

        messages.success(request, 'Booking has been done succesfully. See you soon.')


        return redirect('contact')

    return render(request, "contact.html")


