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
    if page_obj.has_next():
        page_obj.next_page_number()
        next_page_url = reverse('bus_stations') + '?%s' % urllib.parse.urlencode(
            {'page': str(current_page + 1)})
    else:
        next_page_url = None
    if page_obj.has_previous():
        page_obj.previous_page_number()
        prev_page_url = reverse('bus_stations') + '?%s' % urllib.parse.urlencode(
            {'page': str(current_page - 1)})
    else:
        prev_page_url = None
    return render_to_response('index.html', context={
            'bus_stations': page_obj.object_list,
            'current_page': page_obj,
            'prev_page_url': prev_page_url,
            'next_page_url': next_page_url,
        })
