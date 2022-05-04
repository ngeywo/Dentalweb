from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('contact.html',views.contact, name = 'contact'),
    path('appointment.html',views.appointment, name = 'appointment'),
    path('service.html',views.service, name = 'service'),
    path('about.html',views.about, name = 'about'),
    path('price.html',views.price, name = 'price'),
    

]
