from decimal import Decimal

from django.db.models import Manager, Count, Avg
from main_app.querysets import RealEstateListingQuerySet, VideoGameQuerySet
# from main_app.models import VideoGame

class RealEstateListingManager(Manager.from_queryset(RealEstateListingQuerySet)):
    def popular_locations(self) ->dict:
        return (self.values('location')
                .annotate(location_count=Count('location'))
                .order_by('-location_count', 'location')
                )[:2]


class VideoGameManager(Manager.from_queryset(VideoGameQuerySet)):
    def highest_rated_game(self) -> 'VideoGame':
        return self.order_by('-rating').first()

    def lowest_rated_game(self) -> 'VideoGame':
        return self.order_by('rating').first()

    def average_rating(self) ->str:
        result = self.aggregate(avg_rating=Avg('rating'))['avg_rating']
        return f"{result:.1f}"

