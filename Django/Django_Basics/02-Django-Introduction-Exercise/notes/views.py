from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import title

from notes.models import Note

def dashboard(request):
    query = request.GET.get('q')
    notes = Note.objects.all()
    if query:
        notes = notes.filter(title__icontains=query)

    context = {
        "notes" : notes
    }
    return render(request, "notes/dashboard.html", context)
