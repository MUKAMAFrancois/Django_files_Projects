from django import forms
from .models import Comment

# create form to send an email.

class EmailPostForm(forms.Form):
    yourName=forms.CharField(max_length=255)
    yourEmail=forms.EmailField(help_text='Enter your Email')
    receiver=forms.EmailField(help_text="Receipient's email:")
    comments=forms.CharField(required=False,widget=forms.Textarea)


# commenting form section

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')