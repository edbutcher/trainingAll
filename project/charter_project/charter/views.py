from django.shortcuts import render
from .models import DataBase


def index(request):
    data_list = []
    a = DataBase.objects.filter(region='kyivska')
    for data in a:
        data_list.append(data.value)
    context = {'data_list': data_list}
    return render(request, 'charter/charts.html', context)
