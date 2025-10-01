from django.shortcuts import render
from .data.features import FEATURES

# Create your views here.
def landing_page(request):
    context = {
        "features": FEATURES
    }
    return render(request, 'myapp/landing.html', context)