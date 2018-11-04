from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    return render(request, 'pages/index.html', {
    'listings':listings
    })

def about(request):
    mvp = Realtor.objects.filter(is_mvp=True)[:1]
    realtors = Realtor.objects.order_by('-hire_date')
    return render(request, 'pages/about.html', {
    'mvp': mvp,
    'realtors': realtors
    })
