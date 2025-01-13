from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Bus
from .models import timings, timings2
from django.http import HttpResponse


def index(request):
    buses = Bus.objects.all()
    return render(request, 'frontend.html', {'bus': buses})


def login_view(request):
    return render(request, 'login.html')


def bus_detail(request):
    # Retrieve all buses with bus_no ranging from 1 to 7
    buses = Bus.objects.filter(bus_no__range=(1, 9))

    # Pass the retrieved buses to the template context
    return HttpResponse(request, 'bus_timings.html', {'bus': buses})


def bus_timings_redirect(request):
    return render(request, 'bus_timings.html')


def bus_timings(request):
    buses = Bus.objects.all()
    timings = timings.objects.all()
    timings2 = timings2.objects.all()

    return render(request, 'bus_timings.html', {'buses': buses, 'timings': timings, 'timings2': timings2})


from .models import CombinedBusData

def combined_bus_data_view(request):
    data = CombinedBusData.objects.all()
    return render(request, 'bus_timings.html', {'data': data})

def book_now(request):
    return render(request, 'Booknow.html')