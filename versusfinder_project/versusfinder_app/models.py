from django.db import models
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from datetime import datetime

# Add function to User model
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
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    # updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def getDateBeginFormated(self):
        return self.date_begin.strftime("%Y-%m-%dT%H:%M:%S")

    def getDateEndFormated(self):
        return self.date_end.strftime("%Y-%m-%dT%H:%M:%S")

    def __str__(self):
        return "Start at : "+self.date_begin.strftime("%Y-%m-%d %H:%M:%S")+" | end at : "+self.date_end.strftime("%Y-%m-%d %H:%M:%S")

#class UserCharacterBanList(models.Model):
    #    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True, blank=True)
    # updated_at = models.DateTimeField(default=datetime.now, blank=True)
    #
    #def __str__(self):
#   return self.character.name


class UserGameProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    mainchar = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='mainchar')
    banlist = models.ManyToManyField(Character, related_name='banlist')
    timetables = models.ManyToManyField(Timetable, related_name='timetables')
    username = models.CharField(max_length=200)
    battletag = models.CharField(max_length=200)
    skill_level = models.IntegerField()
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    # updated_at = models.DateTimeField(default=datetime.now, blank=True)


class Stat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    win_count = models.IntegerField()
    lose_count = models.IntegerField()
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    # updated_at = models.DateTimeField(default=datetime.now, blank=True)


class Match(models.Model):
    user_profile_one = models.ForeignKey(UserGameProfile, related_name='user_one', on_delete=models.CASCADE)
    user_profile_two = models.ForeignKey(UserGameProfile, related_name='user_two', on_delete=models.CASCADE)
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    state = models.IntegerField()
    user_one_score = models.IntegerField()
    user_two_score = models.IntegerField()
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    # updated_at = models.DateTimeField(default=datetime.now, blank=True)


# Pivots
class UserMatch(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    # updated_at = models.DateTimeField(default=datetime.now, blank=True)


#class UserTimeTable(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#   timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    # updated_at = models.DateTimeField(default=datetime.now, blank=True)
