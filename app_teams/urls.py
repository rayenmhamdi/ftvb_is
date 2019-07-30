from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from app_teams import views
from app_teams.Views.authentication import LoginView, LogoutView
from app_teams.Views.playerViews import players, addPlayerPage, savePlayer, deletePlayer, updatePlayerPage, modifyPlayer

app_name = 'app_teams'
urlpatterns = [
    path('', views.home, name='home'),

    path('players/', players, name='players'),

    path('addplayer/', addPlayerPage, name='addPlayerPage'),
    path('saveplayer/', savePlayer, name='savePlayer'),

    path('deleteplayer/<int:player_id>/', deletePlayer, name='deletePlayer'),

    path('updateplayer/<int:player_id>/', updatePlayerPage, name='updatePlayerPage'),
    path('modifyplayer/<int:player_id>/', modifyPlayer, name='modifyPlayer'),

    path('login_team/', LoginView.as_view(), name='team_login'),
    path('logout_team/', LogoutView.as_view(), name='team_logout'),

    path('wrong/', TemplateView.as_view(template_name='wrong.html'), name='wrong'),
]
