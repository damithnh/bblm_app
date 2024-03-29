# Generated by Django 3.2.8 on 2021-10-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=100)),
                ('stage', models.CharField(max_length=100)),
                ('player', models.CharField(max_length=100)),
                ('team', models.CharField(max_length=100)),
                ('player_GP', models.CharField(max_length=100)),
                ('player_MIN', models.CharField(max_length=100)),
                ('player_FGM', models.CharField(max_length=100)),
                ('player_FGA', models.CharField(max_length=100)),
                ('player_3PM', models.CharField(max_length=100)),
                ('player_3PA', models.CharField(max_length=100)),
                ('player_FTM', models.CharField(max_length=100)),
                ('player_FTA', models.CharField(max_length=100)),
                ('player_TOV', models.CharField(max_length=100)),
                ('player_PF', models.CharField(max_length=100)),
                ('player_ORB', models.CharField(max_length=100)),
                ('player_DRB', models.CharField(max_length=100)),
                ('player_REB', models.CharField(max_length=100)),
                ('player_AST', models.CharField(max_length=100)),
                ('player_STL', models.CharField(max_length=100)),
                ('player_BLK', models.CharField(max_length=100)),
                ('player_PTS', models.CharField(max_length=100)),
                ('birth_year', models.CharField(max_length=100)),
                ('birth_month', models.CharField(max_length=100)),
                ('birth_date', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('height_cm', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('weight_kg', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=100)),
                ('abbr', models.CharField(max_length=100)),
            ],
        ),
    ]
