from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def register(request: HttpRequest) -> HttpResponse:
    return render(request, template_name='accounts/register-page.html')

def login(request: HttpRequest) -> HttpResponse:
    return render(request, template_name='accounts/login-page.html')

def show_profile_details(request: HttpRequest, pk) ->HttpResponse:
    return render(request, template_name='accounts/profile-details-page.html')

def edit_profile(request: HttpRequest, pk) -> HttpResponse:
    return render(request, template_name='accounts/profile-edit-page.html')

def delete_profile(request: HttpRequest, pk) ->HttpResponse:
    return render(request, template_name='accounts/profile-delete-page.html')

