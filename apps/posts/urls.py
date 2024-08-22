from django.urls import path
from . import views


urlpatterns = [
    path('create-post/', views.CreatePostView.as_view(), name='create_post'),
    path('post/<int:post_id>/', views.PostView.as_view(), name='post'), # implement id
    path('<int:district_id>/', views.PostsView.as_view(), name='posts'),
]

app_name = 'posts'
