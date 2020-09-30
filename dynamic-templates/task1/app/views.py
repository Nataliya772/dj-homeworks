import csv

from django.shortcuts import render
from django.conf import settings
#
def inflation_view(request):
    template_name = 'inflation.html'
    data = []
    with open(settings.INFLATION_RUS_CSV, encoding='UTF-8', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for i, column in enumerate(reader):
            data.append(column)
    # чтение csv-файла и заполнение контекста
    context = {'Data': data[0], 'Year': data[1:]}

    return render(request, template_name,
                  context)
