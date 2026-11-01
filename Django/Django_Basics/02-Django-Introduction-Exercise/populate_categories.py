import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoIntroduction.settings')
django.setup()

from notes.models import Note
from categories.models import Category
import random

# Sample categories
categories_data = [
    ("Programming", "Technical programming tutorials and coding guides"),
    ("Web Development", "Frontend and backend web development topics"),
    ("Database", "Database design, optimization and management"),
    ("DevOps", "Deployment, CI/CD and infrastructure topics"),
    ("Security", "Cybersecurity and application security practices"),
    ("Testing", "Unit testing, integration testing and QA methodologies"),
    ("Performance", "Application performance optimization techniques"),
    ("API Design", "RESTful API design and best practices"),
    ("Mobile Development", "iOS and Android development guides"),
    ("Cloud Computing", "Cloud services and architecture patterns"),
    ("Machine Learning", "ML algorithms and data science topics"),
    ("UI/UX Design", "User interface and experience design"),
    ("Project Management", "Agile methodologies and project organization"),
    ("Data Science", "Data analysis and visualization techniques"),
    ("Microservices", "Microservices architecture and patterns"),
    ("GraphQL", "GraphQL API development and queries"),
    ("Docker", "Containerization and Docker best practices"),
    ("Kubernetes", "Container orchestration and K8s management"),
    ("Frontend Frameworks", "React, Vue, Angular and other frameworks"),
    ("Backend Frameworks", "Django, Flask, FastAPI and other frameworks")
]

# Clear existing categories
Category.objects.all().delete()
print("Cleared existing categories")

# Create categories
for name, description in categories_data:
    category = Category(
        name=name,
        description=description
    )
    category.save()
    print(f"Created category: {category.name}")

print(f"\nSuccessfully created {Category.objects.count()} categories!")

# Now update notes to have random categories
notes = Note.objects.all()
all_categories = list(Category.objects.all())

for note in notes:
    # Assign a random category to each note
    note.category = random.choice(all_categories)
    note.save()
    print(f"Updated note '{note.title}' with category '{note.category.name}'")

print(f"\nSuccessfully updated {notes.count()} notes with categories!")
