import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'URLs_and_Views_Exercise.settings')
django.setup()

from destinations.models import Destination
from reviews.models import Review
import random

# Real destinations data
destinations_data = [
    {
        "name": "Paris",
        "country": "France",
        "description": "The City of Light offers iconic landmarks like the Eiffel Tower, world-class museums including the Louvre, and romantic Seine river cruises. Known for its cuisine, fashion, and rich artistic heritage."
    },
    {
        "name": "Tokyo",
        "country": "Japan",
        "description": "A fascinating blend of ancient traditions and cutting-edge technology. From historic temples and gardens to neon-lit streets and innovative cuisine, Tokyo offers endless exploration opportunities."
    },
    {
        "name": "New York City",
        "country": "United States",
        "description": "The Big Apple features iconic skyscrapers, Central Park, Broadway shows, and diverse neighborhoods. A global hub for culture, finance, and entertainment with something for everyone."
    },
    {
        "name": "Rome",
        "country": "Italy",
        "description": "The Eternal City is an open-air museum with ancient Roman ruins, Vatican City, Renaissance art, and incredible Italian cuisine. Walk through history in every cobblestone street."
    },
    {
        "name": "Barcelona",
        "country": "Spain",
        "description": "Known for Gaudí's architecture, beautiful beaches, vibrant nightlife, and delicious tapas. The Gothic Quarter and Park Güell are must-visit attractions."
    },
    {
        "name": "Sydney",
        "country": "Australia",
        "description": "Famous for its iconic Opera House, Harbour Bridge, beautiful beaches like Bondi, and laid-back lifestyle. Great outdoor activities and stunning coastal views."
    },
    {
        "name": "Dubai",
        "country": "United Arab Emirates",
        "description": "A futuristic city with the world's tallest building, luxury shopping, desert adventures, and innovative architecture. A blend of modern luxury and traditional Arabian culture."
    },
    {
        "name": "London",
        "country": "United Kingdom",
        "description": "Historic landmarks like Big Ben and Tower Bridge, world-class museums, royal palaces, and diverse neighborhoods. A perfect mix of history and modern urban life."
    },
    {
        "name": "Santorini",
        "country": "Greece",
        "description": "Stunning white-washed buildings with blue domes, dramatic cliffs, beautiful sunsets, and crystal-clear waters. One of the most romantic destinations in the Mediterranean."
    },
    {
        "name": "Bali",
        "country": "Indonesia",
        "description": "Tropical paradise with lush rice terraces, ancient temples, yoga retreats, and beautiful beaches. Known for its spiritual atmosphere and warm hospitality."
    },
    {
        "name": "Amsterdam",
        "country": "Netherlands",
        "description": "Famous for its canals, historic architecture, world-class museums like the Rijksmuseum, and liberal culture. Perfect for cycling enthusiasts and art lovers."
    },
    {
        "name": "Prague",
        "country": "Czech Republic",
        "description": "The City of a Hundred Spires offers stunning Gothic and Baroque architecture, charming cobblestone streets, affordable beer, and rich history around every corner."
    },
    {
        "name": "Rio de Janeiro",
        "country": "Brazil",
        "description": "Known for Copacabana Beach, Christ the Redeemer statue, vibrant carnival culture, and stunning mountain views. A city that knows how to celebrate life."
    },
    {
        "name": "Cape Town",
        "country": "South Africa",
        "description": "Beautiful coastal city with Table Mountain, pristine beaches, world-class wine regions nearby, and diverse cultural experiences. A perfect blend of nature and urban sophistication."
    },
    {
        "name": "Edinburgh",
        "country": "Scotland",
        "description": "Historic castle, medieval Old Town, annual festivals, and stunning Georgian architecture. A city of literary heritage and mysterious charm."
    },
    {
        "name": "Vancouver",
        "country": "Canada",
        "description": "Surrounded by mountains and ocean, offering outdoor adventures, diverse neighborhoods, excellent food scene, and one of the world's most livable cities."
    },
    {
        "name": "Singapore",
        "country": "Singapore",
        "description": "A modern city-state with stunning architecture, diverse cuisine, clean streets, and beautiful gardens. A perfect blend of Asian cultures and modern efficiency."
    },
    {
        "name": "Istanbul",
        "country": "Turkey",
        "description": "Straddling Europe and Asia, this historic city offers Byzantine and Ottoman architecture, vibrant bazaars, delicious cuisine, and rich cultural heritage."
    },
    {
        "name": "Marrakech",
        "country": "Morocco",
        "description": "Exotic souks, stunning palaces, beautiful gardens, and the Atlas Mountains nearby. A sensory overload of colors, sounds, and flavors in North Africa."
    },
    {
        "name": "Queenstown",
        "country": "New Zealand",
        "description": "Adventure capital of the world with bungee jumping, skiing, stunning lake and mountain scenery, and outdoor activities for thrill seekers."
    }
]

# Sample review data
review_authors = [
    "John Smith", "Emma Johnson", "Michael Brown", "Sarah Davis", "David Wilson",
    "Emily Taylor", "James Anderson", "Olivia Martinez", "William Garcia", "Sophia Rodriguez",
    "Benjamin Lee", "Ava Clark", "Lucas Walker", "Mia Hall", "Ethan Young",
    "Charlotte King", "Alexander Wright", "Harper Lopez", "Daniel Hill", "Eva Adams"
]

review_bodies = [
    "Absolutely amazing experience! The views were breathtaking and the local culture was fascinating. Highly recommend to anyone looking for an unforgettable trip.",
    "Great destination with lots to see and do. The food was incredible and the people were very friendly. Would definitely visit again.",
    "A bit touristy but still worth it. The main attractions are stunning but expect crowds. Best to visit early morning or late afternoon.",
    "Exceeded all my expectations! The architecture is beautiful and there's so much history to explore. A must-visit destination.",
    "Perfect for a relaxing getaway. The atmosphere is peaceful and the scenery is gorgeous. Great place to unwind and recharge.",
    "Incredible food scene and vibrant nightlife. The city never sleeps and there's always something new to discover. Loved every moment!",
    "Stunning natural beauty and well-preserved historical sites. The guided tours were informative and the locals were welcoming.",
    "A unique blend of old and new. The modern facilities coexist perfectly with traditional architecture. Very photogenic destination.",
    "Worth every penny! The experience was magical and the memories will last a lifetime. Already planning my return trip.",
    "Good for families with kids. Lots of activities and attractions suitable for all ages. Clean and well-organized tourist infrastructure.",
    "The perfect romantic destination. Sunset views are unparalleled and the intimate restaurants are perfect for couples.",
    "Adventure seekers paradise! From hiking to water sports, there's something for every adrenaline junkie. Safety standards are excellent.",
    "Cultural immersion at its finest. The museums, galleries, and local markets offer deep insights into the region's heritage.",
    "Budget-friendly destination with great value for money. Accommodation and food are affordable without compromising quality.",
    "Photographer's dream! Every corner offers a perfect shot. The lighting and architecture create stunning compositions naturally.",
    "Easy to navigate with excellent public transport. The city is very walkable and tourist-friendly with clear signage.",
    "Seasonal destination - best visited during specific months. Check weather conditions before planning your trip for optimal experience.",
    "A hidden gem that deserves more recognition. Less crowded than popular alternatives but equally beautiful and authentic.",
    "Great for solo travelers. Safe environment, friendly locals, and plenty of group activities to meet other travelers.",
    "The ultimate bucket list destination. Living up to all the hype and then some. An experience that changes your perspective."
]

# Clear existing data
Destination.objects.all().delete()
Review.objects.all().delete()
print("Cleared existing destinations and reviews")

# Create destinations
created_destinations = []
for dest_data in destinations_data:
    destination = Destination(
        name=dest_data["name"],
        country=dest_data["country"],
        description=dest_data["description"],
        is_active=True
    )
    destination.save()
    created_destinations.append(destination)
    print(f"Created destination: {destination.name} ({destination.country})")

print(f"\nSuccessfully created {len(created_destinations)} destinations!")

# Create reviews for each destination (2-4 reviews per destination)
for destination in created_destinations:
    num_reviews = random.randint(2, 4)
    for _ in range(num_reviews):
        review = Review(
            author=random.choice(review_authors),
            body=random.choice(review_bodies),
            rating=round(random.uniform(3.5, 5.0), 2),
            is_published=random.choice([True, True, True, False]),  # 75% published
            destination=destination
        )
        review.save()
    print(f"Added {num_reviews} reviews for {destination.name}")

total_reviews = Review.objects.count()
print(f"\nSuccessfully created {total_reviews} reviews across all destinations!")
print(f"Average reviews per destination: {total_reviews / len(created_destinations):.1f}")
