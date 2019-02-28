from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('accounts/newprofil', views.newprofil, name='newprofil'),
    path('dashboard/searchmatch', views.searchmatch, name='searchmatch'),
    #path('profile', views.ProfileView.as_view(), name='profile'),
    #path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    #path('dashboard/timetable', views.TimetableView.as_view(), name='timetable'),
    #path('dashboard/timetable/new', views.TimetableView.as_view(), name='timetable-new'),
    path('gamepage', views.GamePageView.as_view(), name='gamepage'),
]
