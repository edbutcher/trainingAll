from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the video index.")


def detail(request, video_name):
    return HttpResponse("You're looking at video %s." % video_name)


def results(request, video_id):
    response = "You're looking at the results of video %s."
    return HttpResponse(response % video_id)


def vote(request, video_id):
    return HttpResponse("You're voting on video %s." % video_id)
