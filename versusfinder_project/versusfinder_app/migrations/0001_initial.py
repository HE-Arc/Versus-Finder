<<<<<<< HEAD
# Generated by Django 2.1.7 on 2019-03-21 10:32
=======
# Generated by Django 2.1.7 on 2019-03-20 10:39
>>>>>>> 97ba4a3957c0b20a87e9b5400487027be1b46221

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField()),
                ('user_one_score', models.IntegerField()),
                ('user_two_score', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='versusfinder_app.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win_count', models.IntegerField()),
                ('lose_count', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='versusfinder_app.Game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_begin', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserGameProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('battletag', models.CharField(max_length=200)),
                ('skill_level', models.IntegerField()),
                ('banlist', models.ManyToManyField(related_name='banlist', to='versusfinder_app.Character')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='versusfinder_app.Game')),
                ('mainchar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainchar', to='versusfinder_app.Character')),
                ('timetables', models.ManyToManyField(related_name='timetables', to='versusfinder_app.Timetable')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='versusfinder_app.Match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='timetable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='versusfinder_app.Timetable'),
        ),
        migrations.AddField(
            model_name='match',
            name='user_profile_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_one', to='versusfinder_app.UserGameProfile'),
        ),
        migrations.AddField(
            model_name='match',
            name='user_profile_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_two', to='versusfinder_app.UserGameProfile'),
        ),
        migrations.AddField(
            model_name='character',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='versusfinder_app.Game'),
        ),
    ]
