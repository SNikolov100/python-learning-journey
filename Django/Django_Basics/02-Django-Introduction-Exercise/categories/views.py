from django.shortcuts import render
from django.template.defaultfilters import title

from categories.models import Category

def list_categories(request):
    query = request.GET.get('q')
    categories = Category.objects.all()
    if query:
        categories = categories.filter(description__icontains=query)

    context = {
        "categories": categories
    }
    return render(request, "categories/list_categories.html", context)
