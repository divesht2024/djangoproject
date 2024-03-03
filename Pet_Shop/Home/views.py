from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    prop = Products.objects.all()

    return render(request, 'home.html', {'prop': prop})


def about(request):
    return render(request, 'about.html')
