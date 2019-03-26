from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import generic, View
from django.urls import reverse_lazy
from .models import Game, Character, Match, User, UserGameProfile, UserMatch, Timetable
import datetime
import pytz
import time
from django.forms import Form
from django.contrib import messages
from random import randint
from django.db.models import Q
import re


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
        try:
            context['gameprofile'] = request.user.get_user_profile()
        except:
            pass
    return render(request, 'versusfinder_app/home.html', context)


def dashboard(request, user_id):
    if request.user.is_authenticated:
        if User.objects.get(id=user_id) == request.user:
            context = {}
            context['user'] = request.user
            context['gameprofile'] = request.user.get_user_profile()
            context['game'] = context['gameprofile'].game
            context['user_timetable'] = context['gameprofile'].timetables.all()
            context['user_id'] = request.user.id

            matchs = Match.objects.all()
            user_matchs = []
            for match in matchs:
                if match.user_profile_one == context['gameprofile'] or match.user_profile_two == context['gameprofile']:
                    user_matchs.append(match)

            context['user_matchs'] = user_matchs
            context['today'] = datetime.datetime.now().strftime("%Y-%m-%d")

            ref_match = datetime.datetime.now() + datetime.timedelta(days=730)
            next_match = None
            for match in matchs:
                if match.timetable.date_begin > datetime.datetime.now(
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
                if match.timetable.date_end < datetime.datetime.now(match.timetable.date_end.tzinfo):
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
            messages.warning(request, "Unallowed operation !")
            return redirect("dashboard", user_id=request.user.id)


def gameprofile_create(request, user_id, game_id):
    ''' Block the user from creating a new gameprofile for the selected game, si le profil existe, le redirige vers son profil'''
    if request.user.is_authenticated:
        context = {}
        context['user_id'] = request.user.id
        context['game'] = Game.objects.get(id=game_id)
        context['characters'] = Character.objects.all().order_by('name')
        return render(request, 'versusfinder_app/gameprofile/new_update.html', context)


def gameprofile_register(request, user_id, game_id):
    if request.user.is_authenticated:
        if User.objects.get(id=user_id) == request.user:
            if request.method == 'POST':
                user = request.user
                # gameprofile = user.get_user_profile()
                # game = gameprofile.game

                # FIXME: to use in case of multi-gameprofiles
                # for gameprofile in gameprofiles:
                #    if gameprofile.game == game_id:
                #        return HttpResponse("Error : only one profile per game is allowed !")

                # Workaround:
                # if user.get_user_profile:
                #    return redirect('gameprofile.edit', user_id=user.id, gameprofile_id=game_id)

                # Validate pseudo
                pseudo = request.POST.get('input_pseudo')
                if not re.match('^[a-zA-Z0-9_]+$', pseudo):
                    messages.error(request, "Invalid pseudo ! Must be alphanumerical")
                    return redirect('gameprofile.register', user_id=user.id, game_id=game_id)

                # Validate skill
                skill = int(request.POST.get('input_skill'))
                if skill < 0 or skill > 10:
                    messages.error(request, "Invalid skill ! Must be between 0 and 10 (inclusive)")
                    return redirect('gameprofile.register', user_id=user.id, game_id=game_id)

                # Build new gameprofile
                gameprofile = UserGameProfile()
                gameprofile.user = user
                gameprofile.game = Game.objects.get(id=game_id)
                gameprofile.mainchar = Character.objects.get(id=request.POST.get('input_character'))
                gameprofile.username = pseudo
                gameprofile.battletag = randint(1000, 9999)
                gameprofile.skill_level = skill
                gameprofile.save()

                # update user
                user.gameprofile = gameprofile
                user.save()

                messages.success(request, "Gameprofile successfully created !")
                return redirect('/')
            else:
                messages.warning(request, "Unallowed operation !")
                return redirect("dashboard", user_id=request.user.id)


def gameprofile_show(request, user_id, gameprofile_id):
    ''' TODO '''
    if request.user.is_authenticated:
        context = {}
        context['user_id'] = request.user.id
        context['gameprofile'] = request.user.get_user_profile()
        context['game'] = context['gameprofile'].game
        context['characters'] = Character.objects.all().order_by('name')
        return render(request, 'versusfinder_app/gameprofile/show.html', context)

def gameprofile_edit(request, user_id, gameprofile_id):
    ''' Open the page to edit the gameprofile '''
    if request.user.is_authenticated:
        if User.objects.get(id=user_id) == request.user:
            context = {}
            context['user_id'] = request.user.id
            context['gameprofile'] = UserGameProfile.objects.get(id=gameprofile_id)
            context['game'] = context['gameprofile'].game
            context['characters'] = Character.objects.all().order_by('name')
            return render(request, 'versusfinder_app/gameprofile/new_update.html', context)
        else:
            messages.warning(request, "Unallowed operation !")
            return redirect("dashboard", user_id=request.user.id)

def gameprofile_update(request, user_id, gameprofile_id):
    ''' Update the gameprofile '''
    if request.user.is_authenticated:
        if User.objects.get(id=user_id) == request.user:
            if request.method == 'POST':
                user = request.user
                gameprofile = UserGameProfile.objects.get(id=gameprofile_id)

                try:
                    # Validate pseudo
                    pseudo = request.POST.get('input_pseudo')
                    if not re.match('^[a-zA-Z0-9_]+$', pseudo):
                        messages.error(request, "Invalid pseudo ! Must be alphanumerical")
                        return redirect('gameprofile.register', user_id=user.id, game_id=game_id)

                    # Validate skill
                    skill = int(request.POST.get('input_skill'))
                    if skill < 0 or skill > 10:
                        messages.error(request, "Invalid skill ! Must be between 0 and 10 (inclusive)")
                        return redirect('gameprofile.register', user_id=user.id, game_id=game_id)

                    # Build new gameprofile
                    gameprofile.mainchar = Character.objects.get(id=request.POST.get('input_character'))
                    gameprofile.username = pseudo
                    gameprofile.skill_level = skill
                    gameprofile.save()

                    messages.success(request, "Gameprofile successfully updated !")
                    return redirect('/')
                except:
                    messages.error(request, "Error occured while updating !")
                    return redirect('gameprofile.edit', user_id=user.id, gameprofile_id=gameprofile_id)
        else:
            messages.warning(request, "Unallowed operation !")
            return redirect("dashboard", user_id=request.user.id)


def match_search(request, game_id):
    if request.user.is_authenticated:

        user = request.user
        gameprofile = user.get_user_profile()
        game = Game.objects.get(id=game_id)

        if gameprofile.id == -1:
            # User has no gameprofile, redirect '''
            return redirect('gameprofile.new', game_id=game.id)
        else:
            context = {}
            context['user_id'] = user.id
            context['gameprofile'] = gameprofile
            context['game'] = Game.objects.get(id=game_id)
            return render(request, 'versusfinder_app/search.html', context)


def search_process(request, game_id):
    ''' returns a list of opponents '''
    if request.user.is_authenticated:
        if request.method == 'POST':

            # Get data from uri
            user = request.user
            gameprofile = user.get_user_profile()
            game = gameprofile.game

            # Get data from form
            # skill_min = int(request.POST.get('skill_min'))
            # skill_max = int(request.POST.get('skill_max'))
            skill_min = 0
            skill_max = 10
            time_begin = request.POST.get('input_hour_begin')
            time_end = request.POST.get('input_hour_end')
            date = request.POST.get('input_date')

            # Split time into hour and minutes
            user_begin_time = datetime.time(int(time_begin[:2]), int(time_begin[3:]))
            user_end_time = datetime.time(int(time_end[:2]), int(time_end[3:]))

            # Process date
            user_begin_year = int(date[:4])
            user_begin_month = int(date[5:7])
            user_begin_day = int(date[8:])

            user_end_year = int(date[:4])
            user_end_month = int(date[5:7])
            user_end_day = int(date[8:])

            # Build datetime
            user_date_begin = datetime.datetime(user_begin_year, user_begin_month, user_begin_day, user_begin_time.hour,
                                                user_begin_time.minute)
            user_date_end = datetime.datetime(user_end_year, user_end_month, user_end_day, user_end_time.hour,
                                              user_end_time.minute)

            # Validate time fields
            if user_date_end < user_date_begin:
                messages.error(request, "Error ! time fields are not coherent")
                return redirect('match.search', user_id=user.id, gameprofile_id=game.id)

            # Exclude opponents that banned the user main character
            opponents = list(
                UserGameProfile.objects.filter(game=gameprofile.game).exclude(banlist=gameprofile.mainchar))
            valid_opponents = []

            # Create initial data package
            data = {}
            data['user'] = {}
            data['user']['gameprofile'] = gameprofile
            data['user']['user_date_begin'] = user_date_begin
            data['user']['user_date_end'] = user_date_end
            data['opponents'] = []

            # now fetch opponents
            for opponent in opponents:
                # Remove those who are playing a character banned by the player
                if opponent.mainchar in gameprofile.banlist.all():
                    continue  # User doesn't want to play againt this character

                # Remove those who do not match the skill requirements
                if opponent.skill_level < skill_min or opponent.skill_level > skill_max:
                    continue  # User doesn't want to play againt this character

                # Date
                opponent_timetables = opponent.timetables

                # New opponent entry
                valid_opponent = {}
                valid_opponent['opponent_timetables'] = []
                valid_opponent['opponent_gameprofil'] = opponent

                for opponent_timetable in opponent_timetables:
                    # Check if datetimes are valid
                    if opponent_timetable.date_begin < user_date_end and opponent_timetable.date_end > user_date_begin:
                        valid_opponent['opponent_timetables'].add(opponent_timetable)

                # If any timetable is matching, add it as a valide opponent
                if valid_opponent['opponent_timetables']:
                    data['opponents'].add(valid_opponent)
                    
            # TODO: UPDATE TIMETABLES (depuis la vue des résultats de la recherche)

            if not data['opponents']:
                messages.warning(request, "No opponent found !")
                return redirect('match.search', game_id=game_id)
            else:
                return JsonResponse(data)

    return HttpResponse("Error occured !")


def match_show(request, game_id, match_id):
    if request.user.is_authenticated:
        context = {}
        context['user_id'] = request.user.id
        context['gameprofile'] = request.user.get_user_profile()
        context['game'] = Game.objects.get(id=game_id)
        context['match'] = Match.objects.get(id=match_id)
        context['date_begin'] = (context['match'].timetable.date_begin).strftime("%Y-%m-%d %H:%M:%S")
        context['date_end'] = (context['match'].timetable.date_end).strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'versusfinder_app/matchdetail.html', context)


def match_alterscore(request, game_id, match_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            match = Match.objects.get(id=match_id)
            gameprofile = request.user.get_user_profile()
            if gameprofile.id == match.user_profile_one.id or gameprofile.id == match.user_profile_two.id:
                if match.user_one_score != 3 and match.user_two_score != 3:
                    data = request.POST.copy()
                    score_player_1 = data.get('score_player_1')
                    score_player_2 = data.get('score_player_2')
                    match.user_one_score = score_player_1
                    match.user_two_score = score_player_2
                    match.save()
                    messages.success(request, "Score successfully changed !")
                    return redirect('match.show', game_id=game_id, match_id=match_id)


def banlist_modify(request, user_id, gameprofile_id):
    if request.user.is_authenticated:
        if User.objects.get(id=user_id) == request.user:
            context = {}
            context['user_id'] = request.user.id
            context['gameprofile'] = request.user.get_user_profile()
            context['game'] = context['gameprofile'].game
            context['banlist'] = context['gameprofile'].banlist.all()
            context['characters'] = Character.objects.all().order_by('name')
            return render(request, 'versusfinder_app/alterbanlist.html', context)
        else:
            messages.warning(request, "Unallowed operation !")
            return redirect("dashboard", user_id=request.user.id)


def banlist_alter(request, user_id, gameprofile_id, char_id):
    if request.user.is_authenticated:
        if User.objects.get(id=user_id) == request.user:
            try:
                char_to_alter = Character.objects.get(id=char_id)
                profile_to_update = UserGameProfile.objects.get(id=gameprofile_id)
                character_is_banned = char_to_alter in profile_to_update.banlist.all()

                if character_is_banned:
                    # Remove character to gameprofile's banlist
                    profile_to_update.banlist.remove(char_to_alter)
                    messages.success(request, "Character " + char_to_alter.name + " succesfully unbanned !")
                else:
                    # Add character to gameprofile's banlist
                    profile_to_update.banlist.add(char_to_alter)
                    messages.success(request, "Character " + char_to_alter.name + " succesfully banned !")

                # Save gameprofile
                profile_to_update.banlist.save()

                return redirect('banlist.modify', user_id=user_id, gameprofile_id=gameprofile_id)
            except:
                messages.error(request, "Error occured !")
                return redirect('banlist.modify', user_id=user_id, gameprofile_id=gameprofile_id)
        else:
            messages.warning(request, "Unallowed operation !")
            return redirect("dashboard", user_id=request.user.id)


def game_show(request, game_id):
    if request.user.is_authenticated:
        context = {}
        context['user_id'] = request.user.id
        context['gameprofile'] = request.user.get_user_profile()
        context['game'] = Game.objects.get(id=game_id)
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
        if User.objects.get(id=user_id) == request.user:
            if request.method == 'POST':
                user = request.user
                gameprofile = user.get_user_profile()

                # Check if the new timetable already exist

                isOk = True
                start = request.POST.get('date_begin').replace('T', ' ')
                end = request.POST.get('date_end').replace('T', ' ')
                start_obj = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M')
                end_obj = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M')
                for timetable in gameprofile.timetables.all():
                    start_timetable = timetable.date_begin.strftime('%Y-%m-%d %H:%M:%S')
                    start_timetable_obj = datetime.datetime.strptime(start_timetable, '%Y-%m-%d %H:%M:%S')
                    end_timetable = timetable.date_end.strftime('%Y-%m-%d %H:%M:%S')
                    end_timetable_obj = datetime.datetime.strptime(end_timetable, '%Y-%m-%d %H:%M:%S')

                    condition1 = ((start_obj <= start_timetable_obj) and (end_obj >= end_timetable_obj))
                    condition2 = ((start_obj <= start_timetable_obj) and (end_obj >= start_timetable_obj))
                    condition3 = ((start_obj <= end_timetable_obj) and (end_obj >= end_timetable_obj))
                    condition4 = ((start_obj >= start_timetable_obj) and (end_obj <= end_timetable_obj))

                    if condition1 or condition2 or condition3 or condition4:
                        isOk = False
                        break

                # Build new timetable
                if isOk:
                    timetable = Timetable()
                    timetable.date_begin = start
                    timetable.date_end = end
                    timetable.save()

                    gameprofile.timetables.add(timetable)
                    gameprofile.save()

                    user.save()

                    messages.success(request, "Timetable successfully created !")
                else:
                    messages.error(request, "Timetable already exist")
            else:
                messages.warning(request, "Unallowed operation !")
                return redirect("dashboard", user_id=request.user.id)

        return redirect("dashboard", user_id=user.id)
