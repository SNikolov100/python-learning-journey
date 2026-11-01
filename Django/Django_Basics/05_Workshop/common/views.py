from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from common.models import Like
from photos.models import Photo


def home_page_view(request: HttpRequest) ->HttpResponse:
    all_photos = Photo.objects.prefetch_related('tagged_pets', 'like_set')
    context = {
        'all_photos': all_photos
    }
    return render(request, 'common/home-page.html', context)

def like_functionality_view(request:HttpRequest, photo_id: int) -> HttpResponse:
    like_object = Like.objects.filter(to_photo_id=photo_id).first()

    if like_object:
        like_object.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_id
        )
    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')

def share_functionality(request: HttpRequest, photo_id:int) ->HttpResponse:
    copy(request.META.get('HTTP_REFERER')[:-1] + resolve_url('photos:details', photo_id))
    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')
