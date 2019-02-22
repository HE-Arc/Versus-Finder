from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy

#from django.contrib.auth.models import User
#from .serializers import UserSerializer, SoldierSerializer
#from rest_framework import viewsets

def home(request):
    context = {}
    context['user_id'] = request.user.id
    return render(request, 'versusfinder_app/home.html', context)
