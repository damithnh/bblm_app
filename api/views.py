from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Player, Team
from api.serializers import PlayerSerializer, TeamSerializer
from rest_framework import serializers

@csrf_exempt
def player_list(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def player_detail(request, pk):
    try:
        player = Player.objects.get(pk=pk)
    except Player.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PlayerSerializer(player)
        return JsonResponse(serializer.data)

@csrf_exempt
def team_list(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def team_detail(request, pk):
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        print(team)
        print(team.abbr)
        serializer = TeamSerializer(team)
        return JsonResponse(serializer.data)
    
@csrf_exempt
def team_players(request, pk):
    try:
        team1 = Team.objects.get(pk=pk)
        print(team1.abbr)
        players = Player.objects.filter(team = team1.abbr).values('player')
        print(players)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        output_list = []
        for player in players:
            output_list.append(player)

        return JsonResponse(output_list, safe=False)

