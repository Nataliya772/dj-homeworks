import csv

from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse(bus_stations))

def read_data():
    with open('data-398-2018-08-30.csv', newline='', encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
    return reader

read_data()


def bus_stations(request):
    data = read_data()
    paginatir = Paginator(data, 10)
    current_page = int(request.GET.get('page', 1))
    page_obj = paginatir.get_page(current_page)
    next_page_url = 'write your url'
    return render_to_response('index.html', context={
        'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'}],
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })

