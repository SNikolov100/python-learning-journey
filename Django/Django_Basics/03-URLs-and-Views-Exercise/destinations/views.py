from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from destinations.models import Destination
from reviews.models import Review


def dashboard(request: HttpRequest) ->HttpResponse:
    featured_destinations = Destination.objects.filter(is_active=True).order_by('-created_at')[:3]
    lastest_reviews = Review.objects.filter(is_published=True).order_by('-created_at')[:3]
    context = {
        'featured_destinations': featured_destinations,
        'lastest_reviews': lastest_reviews
    }
    return render(request, 'destinations/dashboard.html', context)


def destinations_list(request: HttpRequest) -> HttpResponse:
    destinations = Destination.objects.all()

    context = {
        'destinations': destinations
    }
    return render(request, 'destinations/list.html', context)

def destination_details(request: HttpRequest, slug) -> HttpResponse:
    destination = get_object_or_404(Destination, slug=slug)
    context ={
        'destination': destination
    }
    return render(request, 'destinations\detail.html', context)