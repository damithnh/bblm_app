from django.urls import path
from api import views

urlpatterns = [
    path('players/', views.player_list),
    path('players/<int:pk>/', views.player_detail),
    path('teams/', views.team_list),
    path('teams/<int:pk>/', views.team_detail),
    path('teams/players/<int:pk>/', views.team_players),
]