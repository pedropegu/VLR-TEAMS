from django.shortcuts import render
from VLR_APP.models import *
from django.views.generic import ListView

# Create your views here.

class TeamListView(ListView):
    model = team