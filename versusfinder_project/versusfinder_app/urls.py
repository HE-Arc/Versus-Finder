from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('login', views.LoginView.as_view(), name='login'),
    #path('profile', views.ProfileView.as_view(), name='profile'),
    #path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    #path('dashboard/timetable', views.TimetableView.as_view(), name='timetable'),
    #path('dashboard/timetable/new', views.TimetableView.as_view(), name='timetable-new'),
    #path('gamepage', views.GamePageView.as_view(), name='gamepage'),
    #path('searchmatch', views.SearchMatchView.as_view(), name='searchmatch'),
]
