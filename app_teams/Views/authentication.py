'''
USER_TYPE_CHOICES = (
        (1, 'Admin'),
        (2, 'FTVB_Agent'),
        (3, 'Ligue_Agent'),
        (4, 'Team'),
        (5, 'Player'),
        (5, 'Referee'),
    )

'''
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'app_teams/login.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active and user.user_type == 4:
            login(request, user)
            return HttpResponseRedirect(reverse('app_teams:home', args=()))

        return render(request, self.template_name)


class LogoutView(TemplateView):
    template_name = 'app_teams/login.html'

    def get(self, request, **kwargs):
        logout(request)

        return render(request, self.template_name)