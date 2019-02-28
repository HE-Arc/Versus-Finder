from django.db import models
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from datetime import datetime

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
    mainchar = models.ForeignKey(Character, on_delete=models.CASCADE)
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


# Pivots
class UserMatch(models.Model):
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)


class UserCharacterBanList(models.Model):
    userprofil_id = models.ForeignKey(UserGameProfile, on_delete=models.CASCADE)
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)


class UserTimeTable(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    timetable_id = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
