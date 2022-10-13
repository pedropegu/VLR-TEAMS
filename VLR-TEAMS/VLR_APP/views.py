from django.shortcuts import render
from VLR_APP.models import *
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.

class TeamListView(ListView):
    model = team

class TeamListViewDetail(DetailView):
    queryset = team.objects.all()

    