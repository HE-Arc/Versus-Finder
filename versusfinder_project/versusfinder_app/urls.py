from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),

    # Dashboard
    path('dashboard/<user_id>', views.dashboard, name='dashboard'),

    # Games
    path('games/<game_id>/show', views.game_show, name='game.show'),
    path('games/<game_id>/search', views.game_search, name='game.search'),

    # Gameprofile
    path('dashboard/<user_id>/gameprofiles/<game_id>/new', views.gameprofile_create, name='gameprofile.new'),
    path('dashboard/<user_id>/gameprofiles/<game_id>/register', views.gameprofile_register, name="gameprofile.register"),
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>', views.gameprofile_show),
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/show', views.gameprofile_show, name="gameprofile.show"),
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/edit', views.gameprofile_edit, name="gameprofile.edit"),
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/update', views.gameprofile_update, name="gameprofile.update"),

    # Banlist
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/banlist/modify', views.banlist_modify, name='banlist.modify'),
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/characters/<char_id>/alter', views.banlist_alter, name="banlist.alter"),

    # Matches
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/matchs/search', views.match_search, name='match.search'),
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/matchs/<match_id>/show', views.match_show, name='match.show'),
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/matchs/<match_id>/alter_score', views.match_alterscore, name='match.alterscore'),

    # Timetables
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/timetable', views.timetable, name='timetable'),
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/timetable/new', views.timetable_new, name='timetable.new'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
