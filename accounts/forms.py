from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                'autofocus': 'autofocus'
            }
        )

        # self.fields['text'].widget = forms.Textarea(
        #     attrs={
        #         'class': 'form-control',
        #         'placeholder': "What's on your mind" ,
        #     }
        # )
    class Meta:
        model = Post
        fields = ('title', 'text',)

class RegisterForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Username',
                'autofocus': 'autofocus'
            }
        )
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Password',
            }
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Password',
            }
        )


class LoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Username',
                'autofocus': 'autofocus'
            }
        )
        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Password',
            }
        )