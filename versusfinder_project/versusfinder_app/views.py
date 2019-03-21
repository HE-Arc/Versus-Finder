from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.urls import reverse_lazy
from .models import Game, Character, Match, User, UserGameProfile, UserMatch, Timetable
from datetime import datetime
from datetime import timedelta
from django.forms import Form
from django.contrib import messages
from random import randint


# from django.contrib.auth.models import User
# from .serializers import UserSerializer, SoldierSerializer
# from rest_framework import viewsets

# ------------------------------ WARNING ------------------------------ #
# where : context['gameprofile'] = request.user.get_user_profile()
# reason: Must be included since navbar does not support multiple games
# --------------------------------------------------------------------- #

def home(request):
    context = {}
    if request.user.is_authenticated:
        context['user_id'] = request.user.id
        context['gameprofile'] = request.user.get_user_profile()
    return render(request, 'versusfinder_app/home.html', context)


def dashboard(request, user_id):
    if request.user.is_authenticated:
        context = {}
        context['gameprofile'] = request.user.get_user_profile()
        context['user_timetable'] = context['gameprofile'].timetables.all()
        context['user_id'] = request.user.id

        matchs = Match.objects.all()
        user_matchs = []
        for match in matchs:
            if match.user_profile_one == context['gameprofile'] or match.user_profile_two == context['gameprofile']:
                user_matchs.append(match)

        context['user_matchs'] = user_matchs
        context['today'] = datetime.now().strftime("%Y-%m-%d")

        ref_match = datetime.now() + timedelta(days=730)
        next_match = None
        for match in matchs:
            if match.timetable.date_begin > datetime.now(
                    match.timetable.date_begin.tzinfo) and match.timetable.begin < ref_match:
                next_match = match
                ref_match = match.timetable.date_begin

        if next_match != None:
            context['next_match'] = next_match

        old_matchs = []
        winlose = []
        win = 0
        lose = 0
        for match in user_matchs:
            if match.timetable.date_end < datetime.now(match.timetable.date_end.tzinfo):
                old_matchs.append(match)
                if match.user_profile_one == context['gameprofile'] and match.user_one_score == 3:
                    win += 1
                elif match.user_profile_two == context['gameprofile'] and match.user_two_score == 3:
                    win += 1
                else:
                    lose += 1

        winlose.append(win)
        winlose.append(lose)

        context['user_stats'] = winlose
        context['user_old_matchs'] = old_matchs

        return render(request, 'versusfinder_app/dashboard.html', context)
    else:
        pass


def gameprofile_create(request, user_id, game_id):
    ''' Block the user from creating a new gameprofile for the selected game, si le profil existe, le redirige vers son profil'''
    if request.user.is_authenticated:
        context = {}
        context['user_id'] = request.user.id
        context['game'] = Game.objects.get(id=game_id)
        context['gameprofile'] = request.user.get_user_profile()
        context['characters'] = Character.objects.all().order_by('name')
        return render(request, 'versusfinder_app/gameprofile/new.html', context)
    else:
        pass  # render error


def gameprofile_register(request, user_id, game_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            gameprofile = user.get_user_profile()
            game = gameprofile.game

            # FIXME: to use in case of multi-gameprofiles
            # for gameprofile in gameprofiles:
            #    if gameprofile.game == game_id:
            #        return HttpResponse("Error : only one profile per game is allowed !")

            # Workaround:
            if int(game_id) == int(game.id):
                return redirect('gameprofile.edit', user_id=user.id, gameprofile_id=game.id)

                # Build new gameprofile
            gameprofile = UserGameProfile()
            gameprofile.user = user
            gameprofile.game = game
            gameprofile.mainchar = Character.objects.get(id=request.POST.get('input_character'))
            gameprofile.username = request.POST.get('input_pseudo')
            gameprofile.battletag = randint(1000, 9999)
            gameprofile.skill_level = request.POST.get('input_skill')
            gameprofile.save()

            # update user
            user.gameprofile = gameprofile
            user.save()

            messages.success(request, "Gameprofile successfully created !")
            return redirect('/')


def gameprofile_show(request, user_id, gameprofile_id):
    ''' TODO '''
    if request.user.is_authenticated:
        context = {}
        context['user_id'] = request.user.id
        context['gameprofile'] = request.user.get_user_profile()
        context['game'] = context['gameprofile'].game
        context['characters'] = Character.objects.all().order_by('name')
        return render(request, 'versusfinder_app/gameprofile/show.html', context)
    else:
        pass  # render error


def gameprofile_edit(request, user_id, gameprofile_id):
    ''' TODO '''
    if request.user.is_authenticated:
        context = {}
        context['user_id'] = request.user.id
        context['gameprofile'] = request.user.get_user_profile()
        context['game'] = context['gameprofile'].game
        context['characters'] = Character.objects.all().order_by('name')
        return render(request, 'versusfinder_app/gameprofile/edit.html', context)
    else:
        pass  # render error


def gameprofile_update(request, user_id, gameprofile_id):
    ''' TODO '''
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            gameprofile = user.get_user_profile()
            game = gameprofile.game

            try:
                gameprofile.mainchar = Character.objects.get(id=request.POST.get('input_character'))
                gameprofile.username = request.POST.get('input_pseudo')
                gameprofile.skill_level = request.POST.get('input_skill')
                gameprofile.save()

                messages.success(request, "Gameprofile successfully created !")
                return redirect('/')
            except:
                messages.error(request, "Error occured while updating !")
                return redirect('gameprofile.edit', user_id=user.id, gameprofile_id=game.id)
    else:
        pass  # render error


def match_search(request, user_id, gameprofile_id):
    if request.user.is_authenticated:

        if gameprofile_id == -1:
            ''' User has no gameprofile, redirect '''
            # FIXME:game_id should not be hardcoded
            redirect('gameprofile.new', game_id=1)
        else:
            # TODO:finish me
            context = {}
            context['user_id'] = request.user.id
            context['gameprofile'] = request.user.get_user_profile()
            context['characters'] = Character.objects.all().order_by('name')
            return render(request, 'versusfinder_app/search.html', context)
    else:
        pass  # render error


def match_show(request, user_id, gameprofile_id, match_id):
    if request.user.is_authenticated:
        context = {}
        context['user_id'] = request.user.id
        context['gameprofile'] = request.user.get_user_profile()
        context['match'] = Match.objects.get(id=match_id)
        context['date_begin'] = (context['match'].timetable.date_begin).strftime("%Y-%m-%d %H:%M:%S")
        context['date_end'] = (context['match'].timetable.date_end).strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'versusfinder_app/matchdetail.html', context)


def banlist_modify(request, user_id, gameprofile_id):
    if request.user.is_authenticated:
        context = {}
        context['game'] = None  # FIXME:
        context['user_id'] = request.user.id
        context['gameprofile'] = request.user.get_user_profile()
        context['banlist'] = context['gameprofile'].banlist.all()
        context['characters'] = Character.objects.all().order_by('name')
        return render(request, 'versusfinder_app/alterbanlist.html', context)
    else:
        pass  # render error


def banlist_alter(request, user_id, gameprofile_id, char_id):
    if request.user.is_authenticated:
        try:
            char_to_alter = Character.objects.get(id=char_id)
            profile_to_update = UserGameProfile.objects.get(id=gameprofile_id)

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
            return HttpResponse("Error occured")  # send 404


def game_show(request, game_id):
    if request.user.is_authenticated:
        context = {}
        context['user_id'] = request.user.id
        context['gameprofile'] = request.user.get_user_profile()
        context['matchs'] = Match.objects.all()
    return render(request, 'versusfinder_app/gamepage.html', context)

def timetable(request, user_id, gameprofile_id):
    if request.user.is_authenticated:
        context = {}
        context['user_id'] = request.user.id
        context['gameprofile'] = request.user.get_user_profile()
        return render(request, 'versusfinder_app/timetable.html', context)

def timetable_new(request, user_id, gameprofile_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            gameprofile = user.get_user_profile()

            # Build new timetable
            timetable = Timetable()
            timetable.date_begin = request.POST.get('date_begin')
            timetable.date_end = request.POST.get('date_end')
            timetable.save()

            gameprofile.timetables.add(timetable)
            gameprofile.save()

            user.save()

            messages.success(request, "Timetable successfully created !")
            return redirect("dashboard", user_id=user.id)

def game_search(request):
    if request.user.is_authenticated:
        pass
    else:
        pass
