from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from app_ftvb.Models.Configuration import Season
from app_teams.Models.Player import Player
from users.models import Team


@login_required(login_url=reverse_lazy('app_teams:team_login'))
def players(request):
    players = Player.objects.filter(team=request.user.team)
    context = {'players' : players}
    return render(request, 'app_teams/pages/gestion/players/players.html', context)


@login_required(login_url=reverse_lazy('app_teams:team_login'))
def addPlayerPage(request):
    season = Season.objects.last()
    context = {'season':season}
    return render(request, 'app_teams/pages/gestion/players/addplayers.html', context)

def saveOrUpdatePlayer(request, player_id=None):
    if player_id != None:
        player = Player.objects.get(pk=player_id)
    else:
        player = Player(team=request.user.team)

    player.firstname = request.POST['firstname']
    player.lastname = request.POST['lastname']
    player.birthday = request.POST['birthday']
    player.address = request.POST['address']
    player.nationality = request.POST['nationality']

    if request.POST['category'] in ['SF','JF','CF','MF','EF'] :
        player.sexe = 'F'
    else:
        player.sexe = 'M'


    if player_id != None:
        photo = request.FILES.get('photo', False)
        if photo != False:
            player.deleteUploadedPhotoFile()
            player.photo = photo
        proof = request.FILES.get('proof', False)
        if proof != False:
            player.deleteUploadedProofFile()
            player.proof = proof
    else:
        player.photo = request.FILES['photo']
        player.proof = request.FILES['proof']


    player.save()

    if player.id == None:
        return HttpResponseRedirect(reverse('app_teams:wrong', args=()))
    else:
        return 1

@login_required(login_url=reverse_lazy('app_teams:team_login'))
def savePlayer(request):
    saveOrUpdatePlayer(request)
    return HttpResponseRedirect(reverse('app_teams:players', args=()))


@login_required(login_url=reverse_lazy('app_teams:team_login'))
def deletePlayer(request, player_id):
    player = Player.objects.get(pk=player_id)
    player.delete()
    return HttpResponseRedirect(reverse('app_teams:players', args=()))

@login_required(login_url=reverse_lazy('app_teams:team_login'))
def updatePlayerPage(request, player_id):
    player = Player.objects.get(pk=player_id)
    if player not in request.user.team.players.all():
        return HttpResponseRedirect(reverse('app_teams:players', args=()))
    else:
        context = {'player':player}
        return render(request, 'app_teams/pages/gestion/players/updatePlayer.html', context)

@login_required(login_url=reverse_lazy('app_teams:team_login'))
def modifyPlayer(request, player_id):
    saveOrUpdatePlayer(request, player_id)
    return HttpResponseRedirect(reverse('app_teams:players', args=()))