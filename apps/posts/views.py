from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View

from . import forms
from .models import Post, Comment


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
            return redirect('posts:posts', district_id=request.user.district.id)

        return render(request, 'create_post.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class PostDetailView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post).order_by('-id')
        if request.user.district.id == post.district.id:
            return render(request, 'post_detail.html', {'post': post, 'comments': comments})
        return redirect('posts:posts', district_id=request.user.district.id)

    @csrf_exempt
    def post(self, request, post_id):
        # TODO: Fix the comment submit redirect issue
        post = get_object_or_404(Post, id=post_id)
        comment_text = request.POST.get('comment')
        if comment_text:
            Comment.objects.create(text=comment_text, user=request.user, post=post)
            return JsonResponse({'status': 'ok', 'comment': comment_text, 'user': request.user.full_name})
        return JsonResponse({'status': 'error', 'message': 'No comment provided'})