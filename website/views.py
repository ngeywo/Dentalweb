from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def contact(request):
    if request.method  == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        
        send_mail(
            name,
            message,
            email,
            ['ngainewt@gmail.com']
        )
        messages.success(request, f'Thank you for contacting us!')
        return render(request, 'contact.html',{'name': name,})

    else:
        return render(request, 'contact.html', {})


def price(request):
    return render(request, 'price.html', {})

def appointment(request):
    if request.method  == "POST":
        fname = request.POST['firstname']
        sname = request.POST['secondname']
        phone = request.POST['phone']
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        
        name = fname + " " + sname

        send_mail(
            'Appointment Request',
            name,
            phone,
            ['ngainewt@gmail.com'],
            email,
            date,
            time,
        )
        messages.success(request, f'Thank you for contacting us!')
        return render(request, 'appointment.html',{'name': name })

    else:
        return render(request, 'appointment.html', {})





def service(request):
    return render(request, 'service.html',  {})



def about(request):
    return render(request, 'about.html',  {})