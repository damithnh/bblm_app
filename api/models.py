from django.db import models

class Player(models.Model):
    league = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    stage = models.CharField(max_length=100)
    player = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    player_GP = models.CharField(max_length=100)
    player_MIN = models.CharField(max_length=100)
    player_FGM = models.CharField(max_length=100)
    player_FGA = models.CharField(max_length=100)
    player_3PM = models.CharField(max_length=100)
    player_3PA = models.CharField(max_length=100)
    player_FTM = models.CharField(max_length=100)
    player_FTA = models.CharField(max_length=100)
    player_TOV = models.CharField(max_length=100)
    player_PF = models.CharField(max_length=100)
    player_ORB = models.CharField(max_length=100)
    player_DRB = models.CharField(max_length=100)
    player_REB = models.CharField(max_length=100)
    player_AST = models.CharField(max_length=100)
    player_STL = models.CharField(max_length=100)
    player_BLK = models.CharField(max_length=100)
    player_PTS = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=100)
    birth_month = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    height_cm = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    weight_kg = models.CharField(max_length=100)

    def __str__(self):
        return str(self.player)
class Team(models.Model):
    team  = models.CharField(max_length=100)
    abbr  = models.CharField(max_length=100)

    def __str__(self):
        return str(self.team)

    def get_team_abbr(self):
        return self.abbr