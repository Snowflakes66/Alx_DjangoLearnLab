from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment
from taggit.widgets import TagWidget


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tags')
        widgets = {
            'tags': TagWidget(),
        }
