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