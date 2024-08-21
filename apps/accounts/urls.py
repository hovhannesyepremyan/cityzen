from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views


app_name = 'accounts'
auth_patterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

profile_patterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
]

urlpatterns = [
    path('', include(auth_patterns)),
    path('', include(profile_patterns)),
]