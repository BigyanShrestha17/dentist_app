from django.shortcuts import render,redirect
from .forms import AppointmentForm


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
    return render(request, "contact.html")

def service(request):
    return render(request, "service.html")

def team(request):
    return render(request, "team.html")

def testimonial(request):
    return render(request, "testimonial.html")

