from django.urls import path, include

from . import views


app_name = 'accounts'
auth_patterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]

profile_patterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('volunteers-list/', views.VolunteersView.as_view(), name='volunteers_list'),
]

urlpatterns = [
    path('', include(auth_patterns)),
    path('', include(profile_patterns)),
]
