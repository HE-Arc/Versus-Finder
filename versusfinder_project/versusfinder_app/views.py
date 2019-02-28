from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy


# from django.contrib.auth.models import User
# from .serializers import UserSerializer, SoldierSerializer
# from rest_framework import viewsets

def home(request):
    context = {}
    context['user_id'] = request.user.id
    return render(request, 'versusfinder_app/home.html', context)

def newprofil(request):
    if request.user.is_authenticated:
        context = {}
        context['game'] = None
        context['user_id'] = request.user.id
        context['characters'] = {}
        return render(request, 'registration/newprofil.html', context)
    else:
        pass #render error

def search(request):
    if request.user.is_authenticated:
        context = {}
        context['game'] = None
        context['user_id'] = request.user.id
        context['characters'] = {}
        context['banlist'] = {}
        return render(request, 'versusfinder_app/search.html', context)
    else:
        pass #render error
