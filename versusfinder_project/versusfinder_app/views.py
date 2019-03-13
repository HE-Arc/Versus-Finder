from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy
from .models import Character, Match, User, UserGameProfile, UserCharacterBanList


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
        context['user_profile'] = UserGameProfile.objects.get(user=request.user.id)
        context['banlist'] = context['user_profile'].banlist.all()
        context['characters'] = Character.objects.all().order_by('name')
        return render(request, 'registration/newprofil.html', context)
    else:
        pass #render error

def searchmatch(request):
    if request.user.is_authenticated:
        context = {}
        context['game'] = None
        context['user_id'] = request.user.id
        context['user_profile'] = UserGameProfile.objects.get(user=request.user.id)
        context['banlist'] = context['user_profile'].banlist.all()
        context['characters'] = Character.objects.all().order_by('name')
        return render(request, 'versusfinder_app/search.html', context)
    else:
        pass #render error

#class GamePageView(generic.TemplateView):
#    template_name = "versusfinder_app/gamepage.html"
#
#   def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#        context['matchs'] = Match.objects.all()
#        return context
def gamepage(request):
    context = {}
    context['matchs'] = Match.objects.all()
    user = UserGameProfile.objects.get(user=1)
    #c1 = Character(game=1, name="test")
    #c1.save()
    #UserCharacterBanList.objects.all().delete()
    #c1 = Character.objects.get(id=1)
    #c1.save()
    #c2 = Character.objects.get(id=2)
    #c1.save()
    #ban1 = UserCharacterBanList(character=c1)
    #ban1.save()
    #ban2 = UserCharacterBanList(character=c2)
    #ban2.save()
    #user.banlist.add(ban1)
    #user.banlist.add(ban2)
    #user.save()
    return render(request, 'versusfinder_app/gamepage.html', context)

#class DashboardView(generic.TemplateView):
#    template_name = "versusfinder_app/dashboard.html"
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context
def dashboard(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'versusfinder_app/dashboard.html', context)
    else:
        pass