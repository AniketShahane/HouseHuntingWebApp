from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from listings.choices import states_choices, price_choices, bedroom_choices
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    return render(request, 'listings/listings.html', {
    'listings': paged_listings
    })

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listings/listing.html',{
    'listing': listing
    })

def search(request):
    queryList = Listing.objects.order_by('-list_date')

    # Filtering has been done below
    #001 Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryList = queryList.filter(description__icontains=keywords)
    #002 City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryList = queryList.filter(city__iexact=city)
    #003 State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryList = queryList.filter(state__iexact=state)
    #004 Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryList = queryList.filter(bedrooms__lte=bedrooms)
    #005 Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryList = queryList.filter(price__lte=price)

    return render(request, 'listings/search.html',{
    'states_choices':states_choices,
    'bedroom_choices':bedroom_choices,
    'price_choices':price_choices,
    'listings': queryList,
    'values': request.GET
    })
