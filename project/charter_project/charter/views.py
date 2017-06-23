from django.shortcuts import render
from .models import DataBase
import json


def index(request):
    a = json.dumps(list(DataBase.objects.values()))
    context = {'a': a}
    return render(request, 'charter/charts.html', context)
