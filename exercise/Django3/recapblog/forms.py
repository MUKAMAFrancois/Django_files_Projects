from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model=CommentModel
        fields=('name','email','content')

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    