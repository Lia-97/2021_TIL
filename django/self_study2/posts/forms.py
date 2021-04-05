from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        # fields = '__all__'
        exclude = ['user', 'like_users']


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['content']