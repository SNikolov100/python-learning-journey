from django.db.models import Prefetch
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from pets.models import Pet
from photos.models import Photo


# Create your views here.
def pet_add_view(request:HttpRequest) ->HttpResponse:
    form = PetCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        first_object = Pet.objects.first()
        return redirect('accounts:details', pk=first_object.pk)
    context = {
        'form': form
    }

    return render(request, 'pets/pet-add-page.html', context)

def pet_details_view(request:HttpRequest, username: str, pet_slug: str) ->HttpResponse:
    pet = Pet.objects.prefetch_related(
        Prefetch(
            'photo_set',
            queryset=Photo.objects.prefetch_related('tagged_pets', 'like_set')
        )
    ).get(slug=pet_slug)

    context = {
        'pet': pet
    }
    return render(request, 'pets/pet-details-page.html', context)

def pet_edit_view(request:HttpRequest, username: str, pet_slug: str) ->HttpResponse:
    pet = get_object_or_404(Pet, slug=pet_slug)
    form = PetEditForm(request.POST or None, instance=pet)
    if form.is_valid():
        form.save()
        return redirect('pets:details', username=username, pet_slug=pet.slug)
    context= {
        'form': form
    }
    return render(request, 'pets/pet-edit-page.html', context)

def pet_delete_view(request:HttpRequest, username: str, pet_slug: str) ->HttpResponse:
    pet = get_object_or_404(Pet, slug=pet_slug)
    form = PetDeleteForm(request.POST or None, instance=pet)
    if request.method == "POST":
        pet.delete()
        first_object = Pet.objects.first()
        if first_object:
            return redirect('accounts:details', pk=first_object.pk)
        return redirect('common:home')
    context = {
        'form': form
    }
    return render(request, 'pets/pet-delete-page.html', context)