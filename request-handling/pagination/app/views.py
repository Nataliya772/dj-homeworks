import csv
import urllib

from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from urllib.parse import urlencode


def index(request):
    return redirect(reverse(bus_stations))


def read_data(request):
    with open(settings.BUS_STATION_CSV, encoding='cp1251', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        return list(reader)


def bus_stations(request):
    data = read_data(request)
    paginatir = Paginator(data, 10)
    current_page = int(request.GET.get('page', 1))
    page_obj = paginatir.get_page(current_page)
    #u = reverse('bus_stations') + '?page=' + str(current_page + 1)
    u1 = {'page': str(current_page + 1)}
    u2 = reverse('bus_stations') + '?%s' % urllib.parse.urlencode(u1)
    next_page_url = u2
    return render_to_response('index.html', context={
        'bus_stations': page_obj.object_list,
        'current_page': page_obj,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })

