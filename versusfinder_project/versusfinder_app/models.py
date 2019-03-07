from django.db import models
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from datetime import datetime

from django.contrib import auth

def get_user_profile(self):
    return UserGameProfile.objects.get(user=self)

auth.models.User.add_to_class('get_user_profile', get_user_profile)

# Create your models here.
# Core class
class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class Character(models.Model):
    # id = models.AutoField(primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

class UserGameProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    mainchar = models.ForeignKey(Character, related_name="mainchar", on_delete=models.CASCADE)
    banned_characters = models.ManyToManyField(Character, related_name="banlist")
    username = models.CharField(max_length=200)
    battletag = models.CharField(max_length=200)
    skill_level = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

class Stat(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    win_count = models.IntegerField()
    lose_count = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)


class Match(models.Model):
    user_one_id = models.ForeignKey(User, related_name='user_one', on_delete=models.CASCADE)
    user_two_id = models.ForeignKey(User, related_name='user_two', on_delete=models.CASCADE)
    timetable_id = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    state = models.IntegerField()
    user_one_score = models.IntegerField()
    user_two_score = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def get_user_one_profile(self):
        return UserGameProfile.objects.get(user=self.user_one_id)

    def get_user_two_profile(self):
        return UserGameProfile.objects.get(user=self.user_two_id)

# Pivots
class UserMatch(models.Model):
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

class UserTimeTable(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    timetable_id = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
