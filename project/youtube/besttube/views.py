from django.shortcuts import get_object_or_404, render
from .models import BestVideo
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'besttube/top.html'
    context_object_name = 'top_video_list'

    def get_queryset(self):
        return video_id.object.order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    model = BestVideo
    template_name = 'besttube/detail.html'


class ResultsView(generic.DetailView):
    model = BestVideo
    template_name = 'besttube/results.html'
