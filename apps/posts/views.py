from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from . import forms
from .models import Post


class PostsView(View):
    def get(self, request, district_id):
        posts = Post.objects.filter(district_id=district_id)
        return render(request, 'posts.html', {'posts': posts})


@method_decorator(login_required, name='dispatch')
class CreatePostView(View):
    def get(self, request):
        form = forms.CreatePostForm()
        return render(request, 'create_post.html', {'form': form})

    def post(self, request):
        form = forms.CreatePostForm(request.POST)

        if form.is_valid():
            form.save(user=request.user)
            return redirect('posts:posts')

        return render(request, 'create_post.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class PostView(View):
    def get(self, request, post_id):
        # connect comments
        return render(request, 'layout/modals/signup.html', {'form': 'form'})