from rest_framework import serializers
from api.models import Player, Team

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields =  ['league', 'season', 'stage', 'player', 'team', 'player_GP', 'player_MIN', 'player_FGM', 'player_FGA',
        'player_3PM', 'player_3PA', 'player_FTM', 'player_FTA', 'player_TOV', 'player_PF', 'player_ORB', 
        'player_DRB', 'player_REB', 'player_AST', 'player_STL', 'player_BLK', 'player_PTS', 'birth_year', 'birth_month',
        'birth_date', 'height', 'height_cm', 'weight', 'weight_kg']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields =  ['team', 'abbr']