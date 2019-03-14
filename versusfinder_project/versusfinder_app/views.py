from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy
from .models import Character, Match, User, UserGameProfile, UserMatch


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
        pass  # render error


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
        pass  # render error


def alterbanlist(request):
    if request.user.is_authenticated:
        context = {}
        context['game'] = None
        context['user_id'] = request.user.id
        context['user_profile'] = UserGameProfile.objects.get(user=request.user.id)
        context['banlist'] = context['user_profile'].banlist.all()
        context['characters'] = Character.objects.all().order_by('name')
        return render(request, 'versusfinder_app/alterbanlist.html', context)
    else:
        pass  # render error


def gamepage(request):
    context = {}
    context['matchs'] = Match.objects.all()
    return render(request, 'versusfinder_app/gamepage.html', context)


def matchdetail(request, match_pk):
    context = {}
    context['match'] = Match.objects.get(id=match_pk)
    context['date_begin'] = (context['match'].timetable.date_begin).strftime("%Y-%m-%d %H:%M:%S")
    context['date_end'] = (context['match'].timetable.date_end).strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'versusfinder_app/matchdetail.html', context)


def alteruserban(request, profile_id, char_id):
    try:

        char_to_alter = Character.objects.get(id=char_id)
        profile_to_update = UserGameProfile.objects.get(id=profile_id)

        if char_to_alter in profile_to_update.banlist.all():
            ''' remove it from the banlist '''
            profile_to_update.banlist.remove(char_to_alter)
            profile_to_update.banlist.save()
        else:
            ''' insert into the banlist '''
            profile_to_update.banlist.add(char_to_alter)
            profile_to_update.banlist.save()

        return HttpResponse("Success")
    except:
        return HttpResponse("Error occured") #send 404


# class MatchDetailView(generic.DetailView):
#    model = Match

def dashboard(request):
    if request.user.is_authenticated:
        userprofile = UserGameProfile.objects.get(user=request.user)
        context = {}
        context['user_timetable'] = userprofile.timetables.all()
        matchs = Match.objects.all()
        user_matchs = []
        for match in matchs:
            if match.user_profile_one == userprofile or match.user_profile_two == userprofile:
                user_matchs.append(match)

        context['user_matchs'] = user_matchs

        return render(request, 'versusfinder_app/dashboard.html', context)
    else:
        pass
