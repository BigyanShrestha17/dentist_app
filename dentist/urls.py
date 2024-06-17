from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/',views.about, name="about"),
    path('service/',views.service, name="service"),
    path('contact/',views.contact, name="contact"),
    path('contact_success/',views.contact_success, name="contact_success"),
    path('price/',views.price, name="price"),
    path('testimonial/',views.testimonial, name="testimonial"),
    path('team/',views.team, name="team"),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('appointment_success/', views.appointment_success, name='appointment_success'),

]
