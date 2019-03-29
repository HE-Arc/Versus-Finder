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

                  # Matches
                  path('games/<game_id>/matchs/search', views.match_search, name='match.search'),
                  path('games/<game_id>/matchs/search/process', views.search_process, name='search.process'),
                  path('games/<game_id>/matchs/search/show', views.search_show, name='search.show'),
                  path('games/<game_id>/matchs/search/show/validate', views.match_validate, name='match.validate'),
                  path('games/<game_id>/matchs/<match_id>/show', views.match_show, name='match.show'),
                  path('games/<game_id>/matchs/<match_id>/alter_score', views.match_alterscore,
                       name='match.alterscore'),

                  # Gameprofile
                  path('dashboard/gameprofiles/<game_id>/new', views.gameprofile_create, name='gameprofile.new'),
                  path('dashboard/gameprofiles/<game_id>/register', views.gameprofile_register,
                       name="gameprofile.register"),
                  path('dashboard/gameprofiles/<gameprofile_id>', views.gameprofile_show),
                  path('dashboard/gameprofiles/<gameprofile_id>/show', views.gameprofile_show, name="gameprofile.show"),
                  path('dashboard/gameprofiles/<gameprofile_id>/edit', views.gameprofile_edit, name="gameprofile.edit"),
                  path('dashboard/gameprofiles/<gameprofile_id>/update', views.gameprofile_update,
                       name="gameprofile.update"),

                  # Banlist
                  path('dashboard/gameprofiles/<gameprofile_id>/banlist/modify', views.banlist_modify,
                       name='banlist.modify'),
                  path('dashboard/gameprofiles/<gameprofile_id>/characters/<char_id>/alter', views.banlist_alter,
                       name="banlist.alter"),

                  # Timetables
                  path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/timetable', views.timetable,
                       name='timetable'),
                  path('dashboard/<user_id>/gameprofiles/<gameprofile_id>/timetable/new', views.timetable_new,
                       name='timetable.new'),

                  path('dashboard/gameprofiles/<gameprofile_id>/timetable', views.timetable, name='timetable'),
                  path('dashboard/gameprofiles/<gameprofile_id>/timetable/new', views.timetable_new,
                       name='timetable.new'),
                  path('dashboard/gameprofiles/<gameprofile_id>/timetable/<timetable_id>/delete',
                       views.timetable_delete, name='timetable.delete'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
