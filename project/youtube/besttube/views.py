from django.shortcuts import render
from .models import *
from django.views import View

# Create your views here.


def top1(request, *args, **kwargs):
    top_list = BestVideo.objects.all()

    return render(request, "besttube/top.html", locals())


class TopView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('hello')

