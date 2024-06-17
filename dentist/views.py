from django.shortcuts import render,redirect
from .forms import *


def home(request):
    return render(request, "home.html")


def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')


def about(request):
    return render(request, "about.html")

def price(request):
    return render(request, "price.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    return render(request, 'contact_success.html')

def service(request):
    return render(request, "service.html")

def team(request):
    return render(request, "team.html")

def testimonial(request):
    return render(request, "testimonial.html")

