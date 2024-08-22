from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    name = forms.CharField(required=True)
    image = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Post
        fields = ['name', 'image', 'description']

    def save(self, commit=True, *args, **kwargs):
        post = super().save(commit=False)
        user = kwargs.get('user')
        # import pdb;pdb.set_trace()

        post.user = user
        post.district = user.district

        if commit:
            post.save()

        return post
