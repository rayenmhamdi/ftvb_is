from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView


@login_required(login_url=reverse_lazy('app_teams:team_login'))
def home(request):
    return render(request, 'app_teams/pages/summary/index.html')

