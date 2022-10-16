from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Blog

class HomePageView(ListView):
    model = Blog()
    view = "home.html"


# Create your views here.
