# Generated by Django 4.2 on 2023-10-29 09:09

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
            name="Games_data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("game_name", models.CharField(max_length=64)),
                ("difficulty", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Missing_truth_story",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("level_no", models.IntegerField()),
                ("prompt", models.TextField()),
                ("Expected_answer", models.TextField()),
                ("points", models.IntegerField()),
                ("hint_text", models.TextField()),
                ("hint_link", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="User_game_details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("curr_level", models.IntegerField()),
                ("next_level", models.IntegerField()),
                ("score", models.IntegerField()),
                ("status", models.CharField(max_length=64)),
                (
                    "gameId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Games.games_data",
                    ),
                ),
                (
                    "userId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Leaderboard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.IntegerField()),
                (
                    "userID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
