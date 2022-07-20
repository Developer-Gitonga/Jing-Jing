from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Image, Comment, Profile

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image','name','caption']
            
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profilePhoto','bio']

class SearchForm(forms.Form):
    name = forms.CharField(max_length=100)

    