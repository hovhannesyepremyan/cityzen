from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from . import forms
from .models import User


class SignupView(View):
    def get(self, request):
        form = forms.SignupForm()
        return render(request, 'layout/modals/signup.html', {'form': form})

    def post(self, request):
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        return render(request, 'layout/modals/signup.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, 'layout/modals/login.html', {'form': form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user, remember_me = form.cleaned_data
            django_login(self.request, user)
            return redirect('core:homepage')

        return render(request, 'layout/modals/login.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.filter(email=request.user.email).first()
        # TODO: connect district
        return render(request, 'accounts/profile.html', {'user': user})



@method_decorator(login_required, name='dispatch')
class VolunteerView(View):
    def get(self, request, *args, **kwargs):
        # TODO: Implement endpoint and create html file
        pass

