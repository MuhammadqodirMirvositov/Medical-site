from django.shortcuts import render
from my_app.models import Baza_func
from my_app.models import Medic_programs


def my_func(request):
    doctors = Baza_func.objects.all()
    doctor_call = Medic_programs.objects.all()
    data = {
        "doctors" : doctors,
        "doctor_programs" : doctor_call
    }
    return render(request, 'index.html',data)

def about_func(request):
    data = {

    }
    return render(request, 'about.html')

def contact_func(request):
    data = {

    }
    return render(request, 'contact.html')

def price_func(request):
    data = {

    }
    return render(request, 'price.html')

def service_func(request):
    data = {

    }
    return render(request, 'service.html')



