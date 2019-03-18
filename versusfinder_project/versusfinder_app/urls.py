from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),

    # Dashboard
    path('dashboard', views.dashboard, name='dashboard'),

    # Games
    path('games/<game_id>/show', views.game_show, name='game.show'),

    # Gameprofile
    path('dashboard/<user_id>/gameprofiles/new/<game_id>/', views.gameprofile_create, name='gameprofile.new'),
    path('dashboard/<user_id>/gameprofiles/register/<game_id>', views.gameprofile_register, name="gameprofile.register"),
    #path('dashboard/<user_id>/gameprofiles/show/<game_id>', views.gameprofile_show, name="gameprofile.show"),

    # Banlist
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/banlist/modify', views.banlist_modify, name='banlist.modify'),
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/characters/<char_id>/alter', views.banlist_alter, name="banlist.alter"),

    # Matches
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/matchs/search', views.match_search, name='match.search'),
    path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/matchs/<match_id>/show', views.match_show, name='match.show'),

    # Timetables
    #path('dashboard/timetable', views.TimetableView.as_view(), name='timetable'),
    #path('dashboard/timetable/new', views.TimetableView.as_view(), name='timetable-new'),    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
