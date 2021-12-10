from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.settings import BUS_STATION_CSV


def index(request):
   return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [{'Name': row['Name'], 'Street': row['Street'], 'District': row['District']} for row in reader]
        paginator = Paginator(data, 10)
        current_page = request.GET.get('page', 1)
        page = paginator.get_page(current_page)
        context = {
       'bus_stations': page.object_list,
       'page': page,
    }
    return render(request, 'stations/index.html', context)
